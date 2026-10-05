"""
Identificación de personas en el dataset TUG (anonymized_data).

Los archivos no traen ID de paciente (patient.id, name y lastName vienen vacíos) y el
código del nombre del archivo (_temp_A, _temp_BX, ...) es por GRABACIÓN, no por persona.
Este script infiere la persona y muestra la evidencia que respalda la agrupación.

Uso:
    python3 identificar_personas.py [carpeta_json]

Salida:
    - Evidencia en consola (pasos 1 a 5).
    - personas.csv con la persona asignada a cada archivo.
"""
import csv
import datetime
import glob
import hashlib
import itertools
import json
import os
import sys
from collections import defaultdict

CARPETA = sys.argv[1] if len(sys.argv) > 1 else "datos_extraidos/anonymized_data"


def cargar_registros(carpeta):
    registros = []
    for ruta in sorted(glob.glob(os.path.join(carpeta, "*.json"))):
        nombre = os.path.basename(ruta)
        crudo = open(ruta, "rb").read()
        d = json.loads(crudo)
        p = d.get("patient") or {}
        inicio = d.get("timestamp")
        registros.append({
            "archivo": nombre,
            "codigo": nombre.split("_temp_")[1][:-5],
            "md5": hashlib.md5(crudo).hexdigest(),
            "id_campos": [p.get("id"), p.get("name"), p.get("lastName"), d.get("id")],
            "nacimiento": p.get("birthDate"),
            "sexo": p.get("sex"),
            "talla": p.get("height"),
            "tipo": p.get("patientType"),
            "obs_paciente": (p.get("observations") or "").strip(),
            "obs_prueba": (d.get("observations") or "").strip(),
            "kit": "K1" if d["imuData"][0]["deviceId"].startswith("K1-") else "base",
            "inicio": (datetime.datetime.fromtimestamp(inicio / 1000, datetime.timezone.utc)
                       .strftime("%Y-%m-%d %H:%M:%S") if inicio and inicio > 1e12 else ""),
        })
    return registros


def main():
    R = cargar_registros(CARPETA)
    print(f"Archivos analizados: {len(R)}\n")

    # Paso 1: no existe un identificador explícito
    con_id = [r["codigo"] for r in R if any(r["id_campos"])]
    print("PASO 1. Campos de identidad (patient.id, name, lastName, id) no vacíos:",
          con_id or "ninguno -> no hay ID explícito")

    # Paso 2: el código del archivo no identifica personas
    por_codigo = defaultdict(list)
    for r in R:
        por_codigo[r["codigo"]].append(r)
    repetidos = {c: rs for c, rs in por_codigo.items() if len(rs) > 1}
    print(f"\nPASO 2. Códigos distintos: {len(por_codigo)} de {len(R)} archivos. Códigos repetidos:")
    for c, rs in repetidos.items():
        iguales = len({r["md5"] for r in rs}) == 1
        print(f"   {c}: {[r['archivo'] for r in rs]} -> {'MISMO MD5 (duplicado byte a byte)' if iguales else 'contenido distinto'}")

    # Paso 3: agrupar por la llave demográfica (nacimiento + sexo + tipo)
    grupos = defaultdict(list)
    for r in R:
        grupos[(r["nacimiento"], r["sexo"], r["tipo"])].append(r)
    print("\nPASO 3. Grupos con más de un archivo bajo la llave (fecha de nacimiento, sexo, tipo).")
    print("        Columnas de corroboración: talla, kit, hora de inicio (UTC), observaciones.")
    for llave, rs in grupos.items():
        if len(rs) < 2:
            continue
        print(f"\n   {llave}")
        for r in rs:
            print(f"     {r['codigo']:3} talla={r['talla']} kit={r['kit']:4} inicio={r['inicio']} "
                  f"md5={r['md5'][:8]} obs_paciente={r['obs_paciente']!r} obs_prueba={r['obs_prueba']!r}")

    # Paso 4: control de falsos negativos (misma persona con fecha mal digitada)
    print("\nPASO 4. Fechas de nacimiento que difieren en un solo dígito (posible error de digitación):")
    etiquetados = [r for r in R if r["tipo"]]
    hallados = False
    for a, b in itertools.combinations(etiquetados, 2):
        if a["nacimiento"] == b["nacimiento"] or a["sexo"] != b["sexo"]:
            continue
        if sum(x != y for x, y in zip(a["nacimiento"], b["nacimiento"])) == 1:
            hallados = True
            veredicto = "misma talla -> REVISAR" if a["talla"] == b["talla"] else "talla distinta -> personas distintas"
            print(f"   {a['codigo']} ({a['nacimiento']}, {a['talla']} cm, {a['obs_paciente']!r}) vs "
                  f"{b['codigo']} ({b['nacimiento']}, {b['talla']} cm, {b['obs_paciente']!r}) -> {veredicto}")
    if not hallados:
        print("   ninguna")

    # Paso 5: asignar el ID de persona y exportarlo
    ids = {}
    for llave in sorted(grupos, key=lambda k: min(r["archivo"] for r in grupos[k])):
        ids[llave] = f"P{len(ids) + 1:02d}"
    vistos_md5 = set()
    filas = []
    for r in R:
        llave = (r["nacimiento"], r["sexo"], r["tipo"])
        duplicado = r["md5"] in vistos_md5
        vistos_md5.add(r["md5"])
        filas.append({
            "archivo": r["archivo"], "codigo": r["codigo"], "persona_id": ids[llave],
            "tipo": r["tipo"] or "SIN_ETIQUETA", "sexo": r["sexo"], "nacimiento": r["nacimiento"],
            "talla": r["talla"], "kit": r["kit"], "inicio_utc": r["inicio"],
            "duplicado_exacto": duplicado, "obs_paciente": r["obs_paciente"], "obs_prueba": r["obs_prueba"],
        })
    with open("personas.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)

    personas = defaultdict(set)
    for f in filas:
        personas[f["tipo"]].add(f["persona_id"])
    print("\nPASO 5. Resumen")
    print(f"   Archivos: {len(filas)} | duplicados exactos: {sum(f['duplicado_exacto'] for f in filas)}")
    for tipo, ps in sorted(personas.items()):
        n_arch = sum(1 for f in filas if f["tipo"] == tipo)
        print(f"   {tipo:13} archivos={n_arch:2}  personas={len(ps)}")
    print("   (SIN_ETIQUETA son pruebas técnicas; sus 'personas' no son participantes reales)")
    print("\nTabla escrita en personas.csv")


if __name__ == "__main__":
    main()
