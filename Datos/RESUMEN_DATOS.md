# Resumen de los datos — Proyecto TUG 2

> Exploración de `tug.tar.gz` y del notebook `Avance_1_PDGI_Clasificación.ipynb`.
> Fecha de la revisión: 2026-10-04. Los archivos originales no se modificaron; el
> contenido se extrajo en `datos_extraidos/`.

## Resumen rápido

- **78 archivos JSON**, uno por **grabación** (no por paciente ni por sensor). Cada JSON trae
  **todos los sensores IMU** de esa grabación mezclados en una sola lista.
- **5 IMUs por grabación**: `BASE-SPINE` (L5/espalda), `LEFT-ANKLE`, `RIGHT-ANKLE`, **y además
  `LEFT-HAND` y `RIGHT-HAND`** (las manos no estaban en la descripción del proyecto).
- **No hay ningún dato de la cámara RGB-D** en el comprimido: ni video, ni profundidad, ni esqueletos.
- **Etiqueta de clase**: `patient.patientType` ∈ {`PATIENT`, `CONTROL`}. Hay **63 grabaciones PATIENT,
  8 CONTROL y 7 sin etiqueta** (pruebas técnicas). Por personas únicas son **≈54 pacientes y 7 controles**:
  el desbalance es fuerte.
- **No hay estadios de la enfermedad** (Hoehn & Yahr, UPDRS…), ni anotaciones de fases del TUG.
- Acelerómetro en **g** y giróscopo en **°/s**, a **~50 Hz** (≈49,4 Hz efectivos).
- Hay **2 pares de archivos duplicados idénticos**, **varias grabaciones de la misma persona** con
  códigos distintos, **6 archivos de prueba incompletos** y **grabaciones con pausas que no aparecen
  en el eje de tiempo**.

---

## 1. Estructura general

```
Datos/
├── tug.tar.gz                          (34,8 MB, original, sin tocar)
├── Avance_1_PDGI_Clasificación.ipynb   (notebook, sin tocar)
├── datos_extraidos/                    (nuevo, 293 MB descomprimido)
│   └── anonymized_data/
│       ├── 20260208022404_temp_BV.json
│       ├── ...                         (78 archivos .json, sin subcarpetas)
│       └── 20260820142101_temp_AN.json
└── RESUMEN_DATOS.md                    (este documento)
```

| Ítem | Valor |
|---|---|
| Carpetas | 1 (`anonymized_data/`), sin subcarpetas |
| Archivos | 78, todos `.json` (no hay CSV, video, `.bag`, imágenes ni metadatos aparte) |
| Tamaño | 0,2 MB a 10,6 MB por archivo (293 MB en total) |
| Tipo de prueba | `testType = "TIMED_UP_AND_GO"` en los 78 |
| Rango de fechas | 2026-02-08 → 2026-07-04 (las grabaciones); los nombres de archivo llegan hasta 2026-08-20 |

### Convención de nombres

```
20260625164351_temp_A.json
└─────┬──────┘ └┬─┘ └┬┘
      │         │    └─ Código de anonimización (A, B, …, Z, AA, …, BX)
      │         └────── Prefijo fijo "temp"
      └──────────────── Fecha y hora UTC en que se GUARDÓ el archivo (AAAAMMDDhhmmss)
```

- **Fecha del nombre**: coincide (a segundos o minutos) con `endTimestamp`, o sea, es la hora de
  guardado. En algunos casos el archivo se guardó o sincronizó mucho después de grabarlo: `BH` y
  `S` (~1,5 h), `BA` (~15 h), `B` (11 días) y `AM, P, BI, Z, T, AN` (grabados el 2026-07-04 y guardados
  el 2026-08-20). **Para saber cuándo se grabó hay que usar `timestamp`, no el nombre del archivo.**
- **Código** (`A` … `BX`): se asigna **por archivo/grabación, no por persona**. Una misma persona
  puede tener varios códigos (ver §2), y dos archivos con el mismo código son duplicados (`BA`, `Z`).
- Dentro del JSON los campos `id`, `name`, `lastName` y `patient.id` están vacíos (anonimizados).
  **No hay un identificador de paciente.**

---

## 2. Organización por paciente / sensor

### Un archivo = una grabación con todos los sensores

**No hay un archivo por sensor.** Cada JSON trae una lista `imuData` donde se intercalan las
muestras de todos los IMUs, ordenadas por `timestamp`. El sensor de cada muestra se identifica con
el campo `deviceId`:

| `deviceId` (kit "base") | `deviceId` (kit "K1") | Ubicación | Nombre en el notebook |
|---|---|---|---|
| `BASE-SPINE` | `K1-BASE-SPINE` | L5 / espalda baja | `espina_base` |
| `LEFT-ANKLE` | `K1-LEFT-ANKLE` | Tobillo izquierdo | `izquierda` |
| `RIGHT-ANKLE` | `K1-RIGHT-ANKLE` | Tobillo derecho | `derecha` |
| `LEFT-HAND` | `K1-LEFT-HAND` | Mano/muñeca izquierda | `mano_izquierda` |
| `RIGHT-HAND` | `K1-RIGHT-HAND` | Mano/muñeca derecha | `mano_derecha` |

- Hay **dos kits de sensores**: sin prefijo (41 archivos) y con prefijo `K1-` (37 archivos). Parece que
  se usaron dos juegos de IMUs en paralelo durante las brigadas. Conviene registrar el kit como posible
  variable de confusión.
- 72 de 78 archivos tienen los 5 sensores; los 6 restantes son pruebas técnicas (§6).
- Los relojes de los sensores **arrancan en momentos distintos**: el primer `timestamp` de cada sensor
  dentro del mismo archivo difiere hasta ~1 s (p. ej. `AK`: 1027 ms, `J`: 890 ms, `G`: 874 ms). Todos
  los sensores comparten un mismo origen de tiempo (ms desde el inicio de la grabación), así que **hay
  que alinearlos con el `timestamp` absoluto y no con "el primer dato de cada sensor"**.

### Cómo se identifica la persona

Como no hay ID, la única forma de agrupar grabaciones por persona es con
**(`birthDate`, `sex`, `height`, `patientType`)** y las observaciones clínicas, que se repiten. Así
se encuentran estos grupos:

| Persona (nac., sexo) | Archivos | Comentario |
|---|---|---|
| 10/02/2003, F, CONTROL | `AL`, `BC` | Talla 155 vs 156; grabaciones de prueba del equipo (junio) |
| 12/09/1955, M, PATIENT | `BF`, `AR` | DBS, grabaciones consecutivas |
| 29/03/1958, M, PATIENT | `BR`, `AP` | DBS |
| 30/11/1969, M, PATIENT | `BH`, `S` | |
| 23/05/1959, F, PATIENT | `BU`, `K` | DBS |
| 23/06/1955, M, PATIENT | `BT`, `AZ`, `J`, `AQ` | `AZ`, `J`, `AQ` son **doble tarea** (restas, ciudades) |
| 01/05/1953, M, PATIENT | `BA`, `BA` | **Duplicado exacto** (mismo MD5) |
| 14/01/1943, M, PATIENT | `Z`, `Z` | **Duplicado exacto** (mismo MD5) |
| 02/03/2026, —, sin tipo | `N`, `BO`, `BX`, `BJ` | Pruebas técnicas (fecha de nacimiento = fecha de la prueba) |

**Consecuencia para el modelo:** la validación cruzada debe agruparse por persona
(`GroupKFold`/leave-one-subject-out). Si no, grabaciones de la misma persona quedan en train y en
test y la exactitud sale inflada.

### Sitios / brigadas (`tags`)

| Tag | Significado probable | Archivos |
|---|---|---|
| `site` · `SMR` · "Santa Marta" | Brigada en Santa Marta (25–27 jun 2026) | 37 |
| `custom` · `LA` · `CST` | Segunda brigada/sitio (4 jul 2026) | 14 |
| `project` · `INT` + `GRF` (Georef) | Prueba técnica (`BJ`) | 1 |
| *(vacío)* | Sin tag; incluye las 8 pruebas técnicas y 18 grabaciones del kit K1 hechas en Santa Marta los mismos días | 26 |

---

## 3. Contenido de los archivos

### Esquema del JSON (versión más completa, 63 de 78 archivos)

```jsonc
{
  "testType": "TIMED_UP_AND_GO",
  "timestamp": 1782572927735,        // inicio de la grabación, epoch en ms (UTC)
  "endTimestamp": 1782572971667,     // fin, epoch en ms
  "pausedDurationMs": 0,             // tiempo total en pausa
  "hasWarning": false,
  "warningReason": null,             // p. ej. "Dispositivo desconectado durante la prueba"
  "observations": null,              // nota de la prueba (p. ej. "dual task resta de 30")
  "patient": {
    "patientType": "PATIENT",        // ← ETIQUETA: PATIENT | CONTROL
    "sex": "FEMALE", "birthDate": "30/01/1974", "height": "160",   // altura en cm, como string
    "observations": "paciente. levodopa 6am",                      // medicación / estado ON-OFF / DBS
    "id": "", "name": "", "lastName": "", "lastMeasured": null
  },
  "tags": [{"label_type": "site", "acronym": "SMR", "code": "Santa Marta", ...}],
  "imuData": [
    {"deviceId": "K1-LEFT-ANKLE", "sequenceNumber": 0, "timestamp": 771,
     "accelerometer": {"x": 1.0107, "y": 0.0543, "z": 0.0918},
     "gyroscope":     {"x": 0.3052, "y": -0.4272, "z": 0.0610}},
    ...
  ],
  "audioFilePath": null, "dgiResults": null, "praxisHandPosture": null, "uploaded": false
  // "tappingToeCounts": null  (solo en los 8 archivos más recientes)
}
```

Hay **6 variantes del esquema**: los archivos más antiguos (las pruebas técnicas de feb–mar) no traen
`endTimestamp`, `pausedDurationMs`, `observations` ni `sequenceNumber`, y su `patient` no trae `sex`
ni `patientType`. Los 8 más recientes agregan `tappingToeCounts` (siempre `null`). Campos como
`audioFilePath`, `dgiResults` y `praxisHandPosture` existen pero siempre son `null` (son de otras
pruebas de la app *Vimov*).

### Canales y unidades

| Canal | Ejes | Unidad probable | Evidencia |
|---|---|---|---|
| `accelerometer` | x, y, z | **g** (1 g ≈ 9,81 m/s²) | La norma mediana es ≈1,00–1,02 en todos los archivos (gravedad en reposo). Resolución 1/8192 g → rango **±4 g** (16 bits). Solo 5 muestras de tobillo tocan ~4 g (saturación mínima). |
| `gyroscope` | x, y, z | **°/s** | Resolución 0,061 °/s = 1/16,4 → rango **±2000 °/s**. Máximo observado: 785 °/s. |
| `timestamp` (muestra) | — | **ms** desde el inicio de la grabación | Arranca en ~100–1900 ms y crece de 19–20 ms en 19–20 ms. |
| `sequenceNumber` | — | contador por sensor | Consecutivo salvo en las grabaciones con pausa. |

**Orientación de los ejes:** en el sensor de la espalda la gravedad cae sobre el eje **x** en
todas las grabaciones de brigada (desde el 25-jun), así que x ≈ vertical y el giro en el plano
horizontal (*yaw*) se ve sobre todo en `gyroscope.x`. En las pruebas técnicas previas (feb–jun:
`N`, `BJ`, `F`, `AX`, `AL`, `BC`) la gravedad cae sobre **z**: **el sensor se montó con otra
orientación**. Los tobillos en reposo también marcan gravedad en x.

### Frecuencia de muestreo

- Grabaciones de brigada (71 archivos): intervalo mediano de **19 ms**, media de 20,2 ms → **≈49,4 Hz**
  (nominal 50 Hz). Hay jitter: intervalos máximos de 39 ms (una muestra perdida) y, en pocos casos,
  hasta 133 ms (`BE`).
- Pruebas técnicas antiguas (`BV`, `N`, `BO`, `BX`, `BJ`): **~90–107 Hz** e irregular (otra
  configuración del firmware).
- Los sensores **no están sincronizados muestra a muestra**: cada uno tiene su propio reloj de
  ~50 Hz, así que para combinar sensores hay que remuestrear a una malla común.

### Duración de las grabaciones

| Grupo | Mín. | Mediana | Máx. |
|---|---|---|---|
| PATIENT (63) | 12,2 s | 53,8 s | 133,7 s |
| CONTROL (8) | 13,1 s | 28,6 s | 70,6 s |

Un TUG dura 7–15 s en sanos y 10–30 s en Parkinson, así que **la mayoría de los archivos contiene
varias repeticiones del TUG seguidas**. Integrando la velocidad angular vertical del sensor de
espalda (giros mayores de 100°) se detectan entre **2 y 6 giros por grabación, casi siempre 4**.
Como cada TUG tiene 2 giros (el de 180° en el cono y el de antes de sentarse), lo más frecuente
parece ser **2 repeticiones por archivo** (a veces 1 o 3). Es una estimación heurística: no hay
anotaciones que lo confirmen y en algunos archivos el detector no encontró giros (`A`, `BD`, `M`,
`O`, `AI`, `BI`, `Z`), así que hay que revisarlos uno por uno.

### Muestra de contenido

`20260627150939_temp_R.json`: paciente, mujer, nacida en 1974, kit K1, 10 739 muestras en total
(≈2 130–2 170 por sensor), 43,9 s, sin pausa, "paciente. levodopa 6am", sitio Santa Marta. Las
primeras muestras del tobillo izquierdo en reposo marcan acc ≈ (1,01; 0,05; 0,09) g y gyro < 0,5 °/s.

---

## 4. Distribución de clases

La etiqueta está en **`patient.patientType`**. En los nombres de archivo no hay nada que indique la clase.

### Por archivo

| Clase | Archivos | Notas |
|---|---|---|
| `PATIENT` | **63** | Incluye 2 duplicados exactos (`BA`, `Z`) → 61 grabaciones distintas |
| `CONTROL` | **8** | `AL`, `BC`, `AG`, `AY`, `B`, `P`, `T`, `AN` |
| Sin etiqueta | **7** | `BV`, `N`, `BO`, `BX`, `BJ`, `F`, `AX` (pruebas técnicas) |

### Por persona única (agrupando por nacimiento + sexo)

| Clase | Personas | Sexo | Edad (mediana; rango) |
|---|---|---|---|
| PATIENT | **54** | 39 H / 15 M | 65,5 años; 41–83 (más un valor inválido de 0 años, ver §6) |
| CONTROL | **7** | 1 H / 6 M | 64 años; 23–71 |

- **Desbalance ≈ 8:1** (54 vs 7). Un clasificador que diga siempre "Parkinson" acierta ~89 %. Hay que
  reportar *balanced accuracy*, F1 o AUC, y considerar ponderar clases o reunir más controles.
- **Confusión por sexo**: los pacientes son 72 % hombres y los controles 86 % mujeres. El modelo
  podría aprender a separar por sexo en vez de por Parkinson.
- Uno de los controles (`AL`/`BC`, 23 años) es mucho más joven que el resto y fue grabado en sesiones
  de prueba, no en brigada.
- **Diagnóstico dudoso**: `AN` es CONTROL pero dice "Por confirmar diagnóstico"; `Y` y `BI` son PATIENT
  pero dicen "Por confirmar". `U` dice "diagnosticado ayer".
- **No hay estadios** (H&Y, MDS-UPDRS). Lo único clínico es texto libre en `patient.observations` y
  `observations`, de donde se podría extraer:
  - **Medicación**: levodopa (la mayoría, a veces con la hora de la última dosis), amantadina,
    Stalevo, Mirapex, biperideno; varios "no medicado".
  - **Estado ON/OFF**: explícito solo en pocos casos (`BW` "en on", `BN` "estado off", `G`/`X` "estado on").
  - **DBS (estimulación cerebral profunda)**: `BF`/`AR`, `BR`/`AP`, `BU`/`K`, `L`, `AU`.
  - **Doble tarea**: `AZ`, `J`, `AQ` (misma persona que `BT`). Es otra condición experimental y no
    debería mezclarse con el TUG simple.

---

## 5. Explicación del notebook `Avance_1_PDGI_Clasificación.ipynb`

El notebook (60 celdas, pensado para Google Colab) tiene **dos partes muy distintas**:

1. **"Código PDG Predecesor"** (celdas 1–47): lo escribió el equipo anterior para **otro formato
   de datos** (archivos `20250709001.json`, `20250709003.json`, … y archivos de fases
   `20250709003.2.json`). **Ninguno de esos archivos está en el comprimido.**
2. **"Código PDG Actual"** (celdas 48–59): un **adaptador** que convierte el formato nuevo
   (`imuData`, el de `tug.tar.gz`) al formato antiguo, una validación de calidad y una primera
   visualización.

### 5.1 El formato antiguo que esperaba el código predecesor

```jsonc
{ "pruebas": {
    "<timestamp>": {                       // varias pruebas por archivo
      "derecha":     [ {"t": ms, "x":…, "y":…, "z":…, "a":…, "b":…, "g":…}, … ],
      "izquierda":   [ … ],
      "espina_base": [ … ]
} } }
```
- `x, y, z` = acelerómetro en cuentas crudas; `a, b, g` = giróscopo (α, β, γ); `t` en ms.
- `derecha`/`izquierda` = **tobillos**; `espina_base` = L5. No había sensores de mano.
- Las **fases etiquetadas a mano** venían en un archivo aparte `XXXX.2.json`, con claves como
  `caminataIda`, `caminataVuelta` y `giro`, cada una con `inicio`/`fin` en ms. **En el dataset
  actual no hay archivos de fases.**

### 5.2 Recorrido por secciones

| Celdas | Sección | Qué hace |
|---|---|---|
| 0–2 | Título | Autores (predecesores y equipo actual). |
| 3, 12 | Montaje de Drive | `drive.mount('/content/drive')` (la celda 3 está vacía pero conserva la salida). |
| 4 | `cargar_datos_json` | `json.load` con manejo de errores. |
| 6 | **Graficar señales base** | `plot_json_data_with_phases`: recorre `prueba[lado]` y grafica los 6 canales contra `t`, sombreando las fases (`axvspan`). |
| 8 | **FFT** | `fft_json_data`: `np.fft.fft` de cada canal y espectro de magnitud de las frecuencias positivas, con `fs=50`. |
| 9 | Energía + fases | `graficar_energia_y_derivada_con_fases`: **llama a `analisis_fourier_ventana_deslizante` y `agregar_fases_al_grafico`, que no están definidas en el notebook** y hace `fs=25` por defecto. |
| 11 | Muestra | Carga `/20250709003.json` y su `.2.json` (ruta absoluta en `/`, no funcionaría). |
| 14 | **"Domiciano": pipeline base** | Define las piezas que usa todo lo demás (ver 5.3). |
| 17–18 | **Levantarse y sentarse (marcado como OK)** | Señal `b` (gyro Y) de `espina_base` → pipeline de energía → `detectar_fases_tug`. |
| 20 | Caminata ida/vuelta | El mismo pipeline sobre el tobillo izquierdo, señal `g`. |
| 22–32 | Señales cortadas (ida/vuelta) | `extraer_fase` recorta la señal según `inicio`/`fin` del `.2.json` y aplica el pipeline de energía al segmento, en cada tobillo. |
| 34–36 | **Giro (marcado como OK)** | Señal `g` (gyro Z) de `espina_base`. En la celda 36 se cruzan archivos: señal de `…001.json` con fases de `…008.2.json` (dice "REVISAR CON PROFE"). |
| 38 | Swing/Stance manual | `x` (acc) de cada tobillo, filtrado; picos = inicio de STANCE, valles = inicio de SWING (`find_peaks`, prominencia 0,2·max, distancia 0,4 s); calcula la duración media de cada fase. |
| 39 | Autocorrelación | Solo texto explicativo (estimar el periodo del paso). |
| 42 | **Cortes de giro** | Señal `a` (gyro X) de `espina_base`: los flancos de la señal binaria dan los intervalos de giro (`intervalos_giro`). |
| 43 | Endpoints de Vimov | Documentación de la API `https://i2thub.icesi.edu.co:5443/pdvimov/api` (`/patients`, `/patients/{id}/tests/{joint}`, `/tests/{id}`). Así se descargarían los datos desde la plataforma. |
| 45 | Conteo de pasos | Igual que la celda 38, con distancia mínima de 1 s y prominencia 0,35. |
| 47 | **"JOANDGOAG": segmentación completa** | Arma las 5 fases a partir de lo anterior (ver 5.4) y detecta swing/stance solo en las caminatas. |
| 51 | *Actual*: cargar datos | `buscar_archivos_tug()` → `glob` de `*.json` en `/content/drive/MyDrive/TUG_Data/`. |
| 53 | *Actual*: **adaptador** | `adaptar_esquema_json` (ver 5.5). |
| 55 | *Actual*: validación | `validar_y_filtrar_prueba` (ver 5.6). |
| 57 | *Actual*: resultado | Procesa los 78 archivos: **72 aceptados y 6 descartados**. |
| 59 | *Actual*: visualización | Intenta segmentar `20260618075259_temp_BC.json`, pero **falla**: `name 'cargar_datos_json_local' is not defined`. |

### 5.3 Procesamiento de señal (celda 14, "Domiciano")

```
señal cruda (un canal, un sensor)
  → normalizar: s / max|s|                          (queda en [-1, 1])
  → filtro Butterworth pasa-bajos, fc = 3 Hz, orden 20, filtfilt (fase cero), fs = 50
  → "energy_spectrum": ventana de 50 muestras (1 s) con Hanning, paso de 1 muestra,
       energía = Σ x²  (a pesar del nombre es energía en el tiempo, no una FFT)
       y normalizada al máximo
  → promediomovil: media móvil de 50 muestras (1 s), normalizada al máximo
  → binary_threshold: 1 si ≥ 0,2, si no 0               (movimiento / quietud)
```

### 5.4 Cómo se segmentan las fases del TUG

| Fase TUG | Sensor / canal | Regla |
|---|---|---|
| **Levantarse** | `espina_base`, `b` (gyro Y, flexión del tronco) | `detectar_fases_tug`: tramos donde la señal binaria vale 1 durante ≥ 0,5 s; **el primero** = levantarse |
| **Sentarse** | igual | **el último** tramo = sentarse |
| **Giros** | `espina_base`, `a` (gyro X) / `g` (gyro Z) | Flancos 0→1 y 1→0 de la binaria = `intervalos_giro`; se usan el giro 1 (cono) y el giro 2 (antes de sentarse) |
| **Marcha de ida** | tobillos | de `fin(levantarse)` a `inicio(giro1)` |
| **Marcha de regreso** | tobillos | de `fin(giro1)` a `inicio(giro2)` |
| Swing / Stance | tobillos, `x` (acc) | Dentro de cada caminata: picos → STANCE, valles → SWING |

Alternativamente, las fases se tomaban del archivo manual `.2.json` (`caminataIda`, `caminataVuelta`, `giro`).

### 5.5 Adaptador al formato nuevo (celda 53)

- Agrupa `imuData` por `deviceId` con un mapeo por subcadenas (`"spine"`/`"base"` → `espina_base`,
  `"right-ankle"` → `derecha`, `"left-ankle"` → `izquierda`, manos → `mano_*`). Funciona con y sin
  el prefijo `K1-`.
- Ordena cada sensor por `timestamp`, lo **reinicia a 0 en su propia primera muestra** y lo
  **remuestrea a 50 Hz** por interpolación lineal.
- Vuelve a las "unidades antiguas" multiplicando el acelerómetro por 4096 y el giróscopo por 1000 y
  truncando a `int`. Mapea `x,y,z` ← acelerómetro y `a,b,g` ← giróscopo.
- Devuelve `{"pruebas": {timestamp: {sensor: [...]}}, "meta": {...}}` con **una sola prueba por
  archivo**. El código antiguo usaba `indice_muestra = 1, 2, 3` (varias pruebas por archivo), así
  que con datos nuevos hay que usar `indice_muestra = 0`.

**Relación con los archivos reales:** el adaptador sí corresponde al esquema que encontré
(`imuData`, `deviceId` con o sin `K1-`, ms). Pero **no considera** que un archivo trae **varias
repeticiones de TUG**, ni las **pausas**, ni la **orientación distinta del sensor** en las pruebas
antiguas.

### 5.6 Validación (celdas 55–57)

Descarta una grabación si falta alguno de `izquierda`, `derecha` o `espina_base`, si algún sensor
tiene menos de 10 muestras o dura menos de 5 s, si la fs se aleja más de 5 Hz de 50, o si algún eje
tiene varianza 0. Con los 78 archivos (verificado replicando la lógica):

| Descartado | Motivo |
|---|---|
| `BV` | Solo tiene `RIGHT-HAND` → falta `izquierda` |
| `N` | Dura 4,9 s |
| `BO` | Dura 3,7 s (además tiene la advertencia "Dispositivo desconectado") |
| `BX` | Sin `RIGHT-ANKLE` |
| `BJ` | Sin `RIGHT-ANKLE` |
| `AX` | Sin `LEFT-ANKLE` |

La validación **no detecta** duplicados, grabaciones sin etiqueta (`F` pasa como aceptada), doble
tarea, pausas ni grabaciones repetidas de una misma persona. Además, el chequeo de fs no sirve
después del remuestreo, porque la fs siempre sale ≈50 Hz.

---

## 6. Problemas e inconsistencias detectados

### 6.1 Datos faltantes

1. **No hay datos de la cámara RGB-D** en el comprimido. Si existen, están en otro lado y hay que
   pedirlos y emparejarlos por fecha y hora (`timestamp`).
2. **No hay anotaciones de fases** (los `.2.json` del proyecto anterior no están) ni datos
   crudos del formato antiguo (`20250709*.json`). No se pueden validar los segmentadores contra
   una referencia.
3. **No hay estadios clínicos** (H&Y/UPDRS), solo texto libre.
4. **Faltan sensores** en las pruebas técnicas: `BV` (solo `RIGHT-HAND`), `BX` y `BJ` (sin
   `RIGHT-ANKLE` ni `RIGHT-HAND`) y `AX` (sin `LEFT-ANKLE`).
5. **Muy pocos controles**: 7 personas, frente a los "~70 participantes" esperados: hay 61 personas
   etiquetadas.

### 6.2 Duplicados y grabaciones repetidas

6. **Duplicados exactos** (mismo MD5, nombres que difieren en 1 s):
   - `20260626133915_temp_BA.json` = `20260626133916_temp_BA.json`
   - `20260820142005_temp_Z.json` = `20260820142006_temp_Z.json`
7. **Varias grabaciones de la misma persona con códigos distintos** (tabla §2): `BF/AR`,
   `BR/AP`, `BH/S`, `BU/K`, `BT/AZ/J/AQ`, `AL/BC`. El código de anonimización **no sirve como ID de
   paciente**.

### 6.3 Archivos que no son pruebas reales

8. **7 grabaciones sin `patientType`**: `BV`, `N`, `BO`, `BX`, `BJ` (fecha de nacimiento = fecha de
   la prueba, 2026), `F` ("Test", nacido en 2004) y `AX` (nacido en 2019). Hay que excluirlas.
9. **`BO` y `BX`** tienen `warningReason = "Dispositivo desconectado durante la prueba"`.
10. Las pruebas técnicas tienen **otro esquema JSON** (sin `sequenceNumber` ni `endTimestamp`),
    **otra fs (~100 Hz)** y **otra orientación del sensor de espalda** (gravedad en z en vez de x).

### 6.4 Metadatos erróneos o ambiguos

11. **`AB`**: PATIENT con `birthDate = 12/02/2026` (edad 0), un error de captura.
12. **`AL` vs `BC`**: misma persona con talla 155 y 156 cm.
13. **Diagnóstico por confirmar**: `AN` (CONTROL), `Y` y `BI` (PATIENT).
14. `height` está guardado como **string**; `birthDate` está en formato `dd/mm/aaaa`.
15. Tags inconsistentes: el acrónimo `"LA "` tiene un espacio al final y 18 grabaciones del kit K1
    hechas en Santa Marta no tienen tag de sitio.
16. Las **observaciones clínicas** son texto libre, mezclado entre `observations` y
    `patient.observations`, con abreviaturas variadas ("dbs", "DBS", "Dbs").

### 6.5 Problemas de señal / tiempo

17. **Pausas comprimidas**: en 10 grabaciones `pausedDurationMs > 0` (`AK`, `AA`, `BW`, `BK`, `BR`,
    `BH`, `AU`, `BG`, `B`, `AM`). El `timestamp` de las muestras **no deja hueco** durante la pausa
    (el salto máximo es de 39 ms), pero `sequenceNumber` sí salta (hasta 137 saltos en `BW`).
    Por eso **la señal tiene discontinuidades "pegadas"** que pueden parecer movimientos. En `BW`
    se pausaron 55,6 s de 117 s. También hay unos pocos `timestamp` no monótonos (repetidos) en esos archivos.
18. **Desalineación entre sensores**: el primer `timestamp` de cada sensor difiere hasta ~1 s, y
    el adaptador del notebook pone **cada sensor en 0 en su propia primera muestra**. Eso
    desalinea espalda y tobillos hasta 1 s, lo que es grave si las fases se detectan en la espalda
    y se aplican a los tobillos (celda 47).
19. **fs real ≈ 49,4 Hz**, con jitter y muestras perdidas (huecos de 39–133 ms). Usar fs = 50
    fija sin remuestrear introduce un error pequeño, pero acumulable.
20. **Varias repeticiones del TUG por archivo** (duraciones de 12 a 134 s; ~4 giros por grabación).
    `detectar_fases_tug` toma **el primer tramo como "levantarse" y el último como "sentarse"**, así
    que en un archivo con 2–3 repeticiones mezclaría repeticiones distintas. Antes de segmentar
    las fases hay que **separar las repeticiones**.
21. Saturación del acelerómetro (±4 g): solo 5 muestras de tobillo, despreciable.

### 6.6 Problemas del notebook

22. **Funciones no definidas**: `analisis_fourier_ventana_deslizante`, `agregar_fases_al_grafico`
    (celda 9) y `cargar_datos_json_local` (celdas 53/59, por eso la visualización final falla).
23. **Dependencia del orden de ejecución**: `filter_signal`, `energy_spectrum`, `promediomovil`,
    `fases_detectadas` e `intervalos_giro` se definen en celdas anteriores y se redefinen
    después. Ninguna celda tiene `execution_count`, así que el notebook no se ha corrido de
    principio a fin.
24. **Butterworth de orden 20 con `filtfilt(b, a)`**: un filtro tan alto en forma de función de
    transferencia (b, a) suele ser numéricamente inestable. Conviene usar `butter(..., output='sos')` +
    `sosfiltfilt` y un orden 4–6. **No lo verifiqué ejecutándolo** (en este equipo no está scipy),
    pero hay que revisarlo antes de confiar en las señales filtradas.
25. **fs inconsistente**: `fs=50` en casi todo, pero `fs=25` en la celda 9 y en la llamada de la
    celda 11.
26. **Escalas arbitrarias en el adaptador**: el acelerómetro ×4096 (la resolución nativa es 8192
    LSB/g) y el giróscopo ×1000 (la nativa es 16,4 LSB/°/s), con truncamiento a `int`. No
    afecta mucho porque luego se normaliza por el máximo, pero las amplitudes en "unidades antiguas"
    no son comparables con las del dataset anterior.
27. **Normalización por el máximo de cada grabación**: borra la información de amplitud absoluta
    (velocidad del giro, intensidad del paso), que es justamente lo que diferencia Parkinson de
    controles. Para clasificar conviene trabajar en unidades físicas (g, °/s).
28. **Ejes hardcodeados**: la señal `b`/`a`/`g` elegida para cada fase asume una orientación del
    sensor que **no coincide** con la de las pruebas antiguas (gravedad en z en vez de x).
29. Rutas fijas (`/content/drive/MyDrive/TUG_Data/`, `/20250709003.json`) y dependencias de Colab
    (`google.colab.data_table`), así que no corre localmente sin cambios.

### 6.7 Recomendaciones inmediatas

- Crear una **tabla maestra** (CSV) con archivo, persona inferida, clase, sitio, kit, condición
  (simple / doble tarea), DBS, medicación, pausa y si se incluye o no. Así se excluyen de forma
  reproducible los duplicados (`BA`, `Z`), las pruebas técnicas (7) y los casos dudosos.
- Validar **por persona** (GroupKFold) y usar métricas balanceadas. Revisar el desbalance de
  clases y de sexo.
- Para el preprocesamiento: alinear los sensores por `timestamp` absoluto, remuestrear a 50 Hz
  común, cortar o marcar las pausas usando `sequenceNumber`, y **separar las repeticiones del TUG**
  antes de segmentar las fases.
- Pedir al equipo de campo: los datos de la cámara RGB-D, los archivos de fases anotadas (`.2.json`)
  si existen, el estadio clínico (H&Y/UPDRS) y la confirmación de los diagnósticos "por confirmar".

---

## Anexo A. Inventario completo de archivos

`Kit`: `base` = sensores sin prefijo, `K1` = prefijo `K1-`. `fs`: frecuencia media por sensor.
`Dur. señal`: duración del eje de tiempo de las muestras (sin pausas). `Sensores`: "5" = los cinco.

| # | Archivo | Código | Tipo | Sexo | Nac. | Talla | Kit | Sensores | fs (Hz) | Dur. señal (s) | Pausa (ms) | Sitio | Observaciones |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `20260208022404_temp_BV.json` | BV | — | — | 05/02/2026 | — | base | 1: RIGHT-HAND | 88.3 | 18.6 | — | — | — |
| 2 | `20260303043120_temp_N.json` | N | — | — | 02/03/2026 | 155 | base | 5 | 91.3 | 5.0 | — | — | — |
| 3 | `20260303043532_temp_BO.json` | BO | — | — | 02/03/2026 | 155 | base | 5 | 101.3 | 3.7 | — | — | — |
| 4 | `20260303044505_temp_BX.json` | BX | — | — | 02/03/2026 | 155 | base | 3: BASE-SPINE, LEFT-ANKLE, LEFT-HAND | 107.3 | 2.5 | — | — | — |
| 5 | `20260303134630_temp_BJ.json` | BJ | — | — | 02/03/2026 | 155 | base | 3: BASE-SPINE, LEFT-ANKLE, LEFT-HAND | 107.4 | 6.7 | — | INT, GRF | — |
| 6 | `20260307234249_temp_F.json` | F | — | — | 02/12/2004 | 183 | base | 5 | 49.6 | 15.0 | — | — | Test |
| 7 | `20260308232420_temp_AX.json` | AX | — | — | 28/11/2019 | 155 | base | 4: BASE-SPINE, LEFT-HAND, RIGHT-ANKLE, RIGHT-HAND | 49.7 | 30.4 | 0 | — | — |
| 8 | `20260611235032_temp_AL.json` | AL | CONTROL | F | 10/02/2003 | 155 | base | 5 | 49.7 | 22.4 | 0 | — | — |
| 9 | `20260618075259_temp_BC.json` | BC | CONTROL | F | 10/02/2003 | 156 | K1 | 5 | 49.6 | 13.1 | 0 | — | control |
| 10 | `20260625140746_temp_BF.json` | BF | PATIENT | M | 12/09/1955 | 173 | base | 5 | 48.3 | 22.8 | 0 | SMR | paciente DBS |
| 11 | `20260625140851_temp_AR.json` | AR | PATIENT | M | 12/09/1955 | 173 | base | 5 | 49.5 | 41.6 | 0 | SMR | paciente DBS |
| 12 | `20260625144044_temp_D.json` | D | PATIENT | M | 25/12/1965 | 160 | base | 5 | 49.4 | 89.3 | 0 | SMR | — |
| 13 | `20260625145018_temp_AB.json` | AB | PATIENT | M | 12/02/2026 | 180 | base | 5 | 49.4 | 44.9 | 0 | SMR | Paciente |
| 14 | `20260625150353_temp_AK.json` | AK | PATIENT | M | 22/12/1948 | 166 | base | 5 | 49.5 | 73.7 | 6015 | SMR | paciente amantadina 7am |
| 15 | `20260625152019_temp_AA.json` | AA | PATIENT | M | 24/10/1963 | 175 | base | 5 | 49.7 | 41.4 | 9877 | SMR | paciente 2016, levodopa y amantadina 6am |
| 16 | `20260625153756_temp_V.json` | V | PATIENT | M | 26/10/1960 | 177 | base | 5 | 49.4 | 69.2 | 0 | SMR | Paciente levodopa 8am |
| 17 | `20260625164351_temp_A.json` | A | PATIENT | F | 16/11/1962 | 153 | base | 5 | 49.4 | 81.4 | 0 | SMR | paciente |
| 18 | `20260625171352_temp_BW.json` | BW | PATIENT | M | 03/08/1960 | 170 | base | 5 | 50.3 | 60.2 | 55642 | SMR | paciente en on toma 10am |
| 19 | `20260625180613_temp_AG.json` | AG | CONTROL | M | 11/11/1955 | 165 | base | 5 | 49.4 | 70.6 | 0 | SMR | — |
| 20 | `20260625183434_temp_BK.json` | BK | PATIENT | M | 30/12/1957 | 160 | base | 5 | 49.8 | 66.8 | 28564 | SMR | paciente levodopa 2pm |
| 21 | `20260625193811_temp_BD.json` | BD | PATIENT | M | 16/09/1949 | 185 | base | 5 | 49.4 | 60.8 | 0 | SMR | paciente |
| 22 | `20260625195406_temp_BR.json` | BR | PATIENT | M | 29/03/1958 | 150 | base | 5 | 49.9 | 50.6 | 30907 | SMR | DBS; dbs |
| 23 | `20260625195426_temp_AP.json` | AP | PATIENT | M | 29/03/1958 | 150 | base | 5 | 49.4 | 12.2 | 0 | SMR | DBS |
| 24 | `20260625204358_temp_BN.json` | BN | PATIENT | M | 31/01/1964 | 170 | base | 5 | 49.4 | 54.7 | 0 | SMR | paciente, levodopa. estado off. toma a las 3pm |
| 25 | `20260625212453_temp_G.json` | G | PATIENT | M | 27/03/1954 | 165 | base | 5 | 49.4 | 63.9 | 0 | SMR | paciente levodopa, dosis a las 3pm. estado on |
| 26 | `20260625214451_temp_BH.json` | BH | PATIENT | M | 30/11/1969 | 173 | K1 | 5 | 49.6 | 66.0 | 17020 | — | paciente amantadina. |
| 27 | `20260625214518_temp_S.json` | S | PATIENT | M | 30/11/1969 | 173 | K1 | 5 | 49.4 | 101.8 | 0 | — | paciente amantadina. |
| 28 | `20260625215046_temp_X.json` | X | PATIENT | M | 21/01/1962 | 168 | K1 | 5 | 49.4 | 53.9 | 0 | — | levodopa. 10am, estado on |
| 29 | `20260626133915_temp_BA.json` | BA | PATIENT | M | 01/05/1953 | 167 | K1 | 5 | 49.4 | 50.2 | 0 | — | paciente levodopa 5pm |
| 30 | `20260626133916_temp_BA.json` | BA | PATIENT | M | 01/05/1953 | 167 | K1 | 5 | 49.4 | 50.2 | 0 | — | paciente levodopa 5pm |
| 31 | `20260626141246_temp_AC.json` | AC | PATIENT | F | 09/04/1952 | 148 | base | 5 | 49.5 | 53.8 | 0 | SMR | paciente. amantadina, 4.30am |
| 32 | `20260626144433_temp_AV.json` | AV | PATIENT | M | 04/06/1947 | 165 | base | 5 | 49.4 | 73.2 | 0 | SMR | paciente. levodopa 8:30 |
| 33 | `20260626145512_temp_AO.json` | AO | PATIENT | F | 24/07/1953 | 166 | K1 | 5 | 49.4 | 76.5 | 0 | — | levodopa. 7am |
| 34 | `20260626150532_temp_M.json` | M | PATIENT | F | 31/01/1946 | 172 | base | 5 | 49.4 | 82.0 | 0 | SMR | levodopa. 9pm día anterior |
| 35 | `20260626151711_temp_BQ.json` | BQ | PATIENT | F | 12/02/1976 | 154 | K1 | 5 | 49.4 | 70.9 | 0 | — | levodopa, 8am |
| 36 | `20260626152553_temp_U.json` | U | PATIENT | M | 03/07/1979 | 170 | base | 5 | 49.4 | 41.6 | 0 | SMR | paciente, diagnosticado ayer |
| 37 | `20260626153637_temp_AJ.json` | AJ | PATIENT | F | 22/11/1961 | 162 | base | 5 | 49.4 | 49.2 | 0 | SMR | paciente. levodopa 10am |
| 38 | `20260626154758_temp_O.json` | O | PATIENT | F | 20/10/1953 | 163 | base | 5 | 49.5 | 63.3 | 0 | SMR | paciente, levodopa. 10am |
| 39 | `20260626160554_temp_BU.json` | BU | PATIENT | F | 23/05/1959 | 158 | base | 5 | 49.3 | 62.5 | 0 | SMR | Dbs, paciente. levodopa 9am. |
| 40 | `20260626160620_temp_K.json` | K | PATIENT | F | 23/05/1959 | 158 | base | 5 | 49.4 | 19.6 | 0 | SMR | Dbs, paciente. levodopa 9am. |
| 41 | `20260626170623_temp_BT.json` | BT | PATIENT | M | 23/06/1955 | 166 | K1 | 5 | 49.4 | 89.7 | 0 | — | paciente. No medicado |
| 42 | `20260626170733_temp_AZ.json` | AZ | PATIENT | M | 23/06/1955 | 166 | K1 | 5 | 49.4 | 31.5 | 0 | — | paciente. No medicado; dual task resta de 30 |
| 43 | `20260626170919_temp_J.json` | J | PATIENT | M | 23/06/1955 | 166 | K1 | 5 | 49.4 | 14.4 | 0 | — | paciente. No medicado; dual task desde 30 menos 3 |
| 44 | `20260626170956_temp_AQ.json` | AQ | PATIENT | M | 23/06/1955 | 166 | K1 | 5 | 49.4 | 15.6 | 0 | — | paciente. No medicado; ciudades dual task |
| 45 | `20260626194407_temp_BM.json` | BM | PATIENT | F | 05/10/1949 | 150 | K1 | 5 | 49.4 | 49.3 | 0 | — | paciente, no toma levodopa. |
| 46 | `20260626202515_temp_BS.json` | BS | PATIENT | M | 21/02/1957 | 157 | K1 | 5 | 49.4 | 133.7 | 0 | — | paciente, levodopa, amantadina. 10am levo |
| 47 | `20260626204728_temp_AW.json` | AW | PATIENT | M | 28/09/1960 | 171 | K1 | 5 | 49.3 | 38.4 | 0 | — | levodopa, 10am, siguiente 4pm |
| 48 | `20260626211937_temp_AH.json` | AH | PATIENT | M | 30/09/1958 | 165 | K1 | 5 | 49.4 | 51.0 | 0 | — | paciente, amantadina, viperidel. tomado 12m |
| 49 | `20260626213214_temp_AT.json` | AT | PATIENT | F | 06/12/1963 | 163 | K1 | 5 | 49.4 | 47.4 | 0 | — | levodopa, 3pm, media de 250mg |
| 50 | `20260626215053_temp_AE.json` | AE | PATIENT | F | 06/01/1969 | 157 | K1 | 5 | 49.4 | 46.0 | 0 | — | paciente. no toma levodopa, tenía stalevo y amantadina. |
| 51 | `20260626222007_temp_BL.json` | BL | PATIENT | M | 24/12/1966 | 173 | K1 | 5 | 49.4 | 66.8 | 0 | — | levodopa, amantadina, mirapex. 2pm levo |
| 52 | `20260627133637_temp_AS.json` | AS | PATIENT | M | 28/06/1950 | 167 | K1 | 5 | 49.5 | 48.5 | 0 | SMR | paciente, levodopa 7am |
| 53 | `20260627135010_temp_BP.json` | BP | PATIENT | M | 28/03/1982 | 170 | base | 5 | 49.4 | 64.8 | 0 | SMR | paciente levodopa, amantadina. 9am |
| 54 | `20260627135720_temp_AD.json` | AD | PATIENT | M | 24/12/1972 | 165 | K1 | 5 | 49.4 | 73.7 | 0 | SMR | paciente, levodopa 6am. |
| 55 | `20260627143518_temp_BB.json` | BB | PATIENT | M | 03/05/1958 | 175 | K1 | 5 | 49.4 | 48.4 | 0 | SMR | paciente, no medicado. |
| 56 | `20260627150939_temp_R.json` | R | PATIENT | F | 30/01/1974 | 160 | K1 | 5 | 49.4 | 43.9 | 0 | SMR | paciente. levodopa 6am |
| 57 | `20260627152358_temp_W.json` | W | PATIENT | M | 18/01/1968 | 170 | K1 | 5 | 49.4 | 47.1 | 0 | SMR | amantadina, vipiridene. 5am, 9am |
| 58 | `20260627155804_temp_I.json` | I | PATIENT | M | 26/07/1967 | 175 | K1 | 5 | 49.2 | 41.1 | 0 | SMR | paciente, levodopa 8am |
| 59 | `20260627161148_temp_Q.json` | Q | PATIENT | M | 25/12/1971 | 165 | base | 5 | 49.4 | 58.2 | 0 | SMR | levodopa, 8am |
| 60 | `20260627162118_temp_AU.json` | AU | PATIENT | M | 04/04/1954 | 182 | K1 | 5 | 49.6 | 77.1 | 6276 | SMR | paciente, levodopa 125, 10am; dbs activo |
| 61 | `20260627163836_temp_L.json` | L | PATIENT | M | 23/08/1954 | 179 | base | 5 | 49.4 | 56.5 | 0 | SMR | paciente, no levodopa. DBS dos electrodos |
| 62 | `20260627171353_temp_H.json` | H | PATIENT | M | 11/10/1976 | 175 | K1 | 5 | 49.4 | 39.4 | 0 | SMR | levodopa, 10am |
| 63 | `20260627180847_temp_AI.json` | AI | PATIENT | F | 04/12/1954 | 153 | K1 | 5 | 49.4 | 102.2 | 0 | SMR | levodopa, 11am |
| 64 | `20260627205326_temp_C.json` | C | PATIENT | F | 17/02/1979 | 153 | K1 | 5 | 49.5 | 43.2 | 0 | SMR | paciente, 3:30pm |
| 65 | `20260704154505_temp_AF.json` | AF | PATIENT | M | 28/03/1963 | 173 | base | 5 | 49.3 | 44.2 | 0 | LA | paciente, levodopa 6:30am |
| 66 | `20260704155929_temp_BE.json` | BE | PATIENT | M | 28/05/1963 | 163 | base | 5 | 49.3 | 40.5 | 0 | LA | paciente, levodopa, 6am |
| 67 | `20260704165749_temp_E.json` | E | PATIENT | M | 17/12/1985 | 180 | base | 5 | 49.4 | 39.3 | 0 | LA | — |
| 68 | `20260704172020_temp_Y.json` | Y | PATIENT | M | 21/09/1968 | 170 | base | 5 | 49.5 | 42.0 | 0 | LA | Por confirmar |
| 69 | `20260704194015_temp_AY.json` | AY | CONTROL | F | 23/06/1965 | 165 | base | 5 | 49.5 | 31.3 | 0 | LA | — |
| 70 | `20260704194635_temp_BG.json` | BG | PATIENT | M | 19/10/1971 | 175 | base | 5 | 49.4 | 68.1 | 3645 | LA | paciente, levodopa 6am |
| 71 | `20260715052203_temp_B.json` | B | CONTROL | F | 03/07/1962 | 147 | K1 | 5 | 50.5 | 26.0 | 27550 | LA | Control |
| 72 | `20260820141830_temp_AM.json` | AM | PATIENT | M | 04/04/1960 | 158 | K1 | 5 | 49.7 | 43.3 | 5681 | LA | — |
| 73 | `20260820141849_temp_P.json` | P | CONTROL | F | 03/02/1962 | 159 | K1 | 5 | 49.5 | 46.3 | 0 | LA | — |
| 74 | `20260820141919_temp_BI.json` | BI | PATIENT | F | 18/04/1964 | 160 | K1 | 5 | 49.5 | 54.5 | 0 | LA | Por confirmar |
| 75 | `20260820142005_temp_Z.json` | Z | PATIENT | M | 14/01/1943 | 160 | K1 | 5 | 49.5 | 57.2 | 0 | LA | Levodopa Día anterior 12 pm |
| 76 | `20260820142006_temp_Z.json` | Z | PATIENT | M | 14/01/1943 | 160 | K1 | 5 | 49.5 | 57.2 | 0 | LA | Levodopa Día anterior 12 pm |
| 77 | `20260820142037_temp_T.json` | T | CONTROL | F | 11/08/1956 | 150 | K1 | 5 | 49.5 | 24.6 | 0 | LA | — |
| 78 | `20260820142101_temp_AN.json` | AN | CONTROL | F | 08/11/1963 | 158 | K1 | 5 | 49.5 | 65.3 | 0 | LA | Por confirmar diagnóstico |
