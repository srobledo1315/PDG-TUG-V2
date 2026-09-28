# Guía de Estilo y Formato (Basado en Normas APA 7ª Edición)

Este documento establece las reglas obligatorias de presentación, estructura y citación para el proyecto de grado, con el fin de garantizar un estándar académico y un tono altamente profesional.

---

## 1. Formato General del Documento

Aunque la redacción se realice en Markdown (`.md`), el documento final (exportado a PDF o Word) debe cumplir con los siguientes parámetros técnicos de la **APA 7ª edición**:

* **Tipografía recomendada:** Times New Roman (12 pt), Arial (11 pt) o Calibri (11 pt).
* **Interlineado:** Doble espacio (2.0) en todo el texto, incluyendo la portada, resumen, citas en bloque y lista de referencias. (En Markdown, esto se logra configurando la exportación o dejando una línea en blanco entre párrafos).
* **Alineación:** Alineado a la izquierda. **No** se debe justificar el texto.
* **Sangría:** Sangría de primera línea en cada párrafo de 1.27 cm (0.5 pulgadas). 
* **Márgenes:** 2.54 cm (1 pulgada) en los cuatro lados de la página.

---

## 2. Estructura de la Portada Profesional

La portada actual del proyecto tiene etiquetas residuales (`[]{#_bookmark...}`) y formato de cita en bloque (`>`). Debe limpiarse y reestructurarse así:

1. **Título del Proyecto:** Centrado, en negrita. Capitalización de título (cada palabra principal en mayúscula). Debe ir a unas 3 o 4 líneas desde el margen superior.
2. **Espacio en blanco:** Una línea en blanco a doble espacio.
3. **Autores:** Centrado. Nombres completos de los estudiantes separados por comas o "y" (ej. Juan José Arias Gallego, Esteban Guarin Valencia, Santiago Gómez Robledo y Heiner Danit Rincón Carrillo).
4. **Afiliación:** Centrado. Programas académicos y universidad (ej. *Ingeniería Telemática e Ingeniería de Sistemas, Universidad Icesi*).
5. **Curso / Contexto:** Centrado. (ej. *Proyecto de Grado I*).
6. **Tutores:** Centrado. (ej. *Tutores: Domiciano Rincón y Andrés Navarro*).
7. **Fecha:** Centrado. (ej. *Mes y Año*).

---

## 3. Niveles de Títulos (Jerarquía APA)

Para mantener el rigor en Markdown, los títulos deben seguir esta jerarquía al exportar:

* **Nivel 1 (Equivalente a `# Nivel 1` en MD):** Centrado, **Negrita**. El texto comienza en un nuevo párrafo. (Usado para los capítulos principales como *Introducción*, *Marco Teórico*, *Objetivos*).
* **Nivel 2 (Equivalente a `## Nivel 2` en MD):** Alineado a la izquierda, **Negrita**. El texto comienza en un nuevo párrafo. (Usado para subsecciones como *Planteamiento del problema*).
* **Nivel 3 (Equivalente a `### Nivel 3` en MD):** Alineado a la izquierda, **Negrita y *Cursiva***. El texto comienza en un nuevo párrafo.
* **Nivel 4 (Equivalente a `#### Nivel 4` en MD):** Con sangría, **Negrita**, terminando con punto final. El texto comienza en la misma línea.

*(Evitar numerar los títulos de forma manual ej. "1.1.", "1.1.1." a menos que el formato específico de la universidad lo exija sobre el formato APA).*

---

## 4. Citación en el Texto

Toda afirmación técnica, estadística o médica (como la definición de la prueba TUG o síntomas de Parkinson) debe estar respaldada mediante el sistema **Autor, Fecha**.

**A. Cita Parentética (Idea general apoyada por un autor):**
> La marcha arrastrada es uno de los biomarcadores más tempranos en pacientes con la enfermedad (Molero-Mateo et al., 2026).

**B. Cita Narrativa (El autor hace parte del hilo conductor):**
> Como demostraron Zampieri et al. (2010), el TUG instrumentado ofrece una ventaja medible frente a la prueba clásica con cronómetro.

**Reglas de Autores:**
* 1 o 2 autores: (Podsiadlo & Richardson, 1991).
* 3 o más autores: Siempre usar "et al." desde la primera mención (Vervoort et al., 2016).

---

## 5. Lista de Referencias

* El título **Referencias** debe ir centrado y en negrita (Nivel 1).
* **Sangría Francesa:** La primera línea de cada referencia va alineada a la izquierda y las líneas subsiguientes tienen una sangría de 1.27 cm.
* **Orden:** Alfabético según el apellido del primer autor.

**Ejemplo de formato para un Artículo Científico (Paper):**
> Apellido, A. A., Apellido, B. B. & Apellido, C. C. (Año). Título del artículo sin capitalización. *Nombre de la Revista en Cursiva*, *Volumen en Cursiva*(Número), páginas. https://doi.org/xxxx

---

## 6. Tablas y Figuras

Deben integrarse de forma limpia, prescindiendo de capturas de pantalla de baja calidad. En Markdown:

* **Etiqueta y número:** Negrita, arriba de la tabla/figura (ej. **Tabla 1**).
* **Título:** En cursiva, debajo del número, a doble espacio (ej. *Fases de la prueba Timed Up and Go*).
* **Notas:** Si es extraída de otro artículo, debe llevar una nota debajo indicando la fuente. (ej. *Nota.* Adaptado de Zampieri et al. (2010)).

---

## Conclusión para la Migración del Documento Actual

Para que `main.md` adquiera un tono profesional inmediato, se recomienda:
1. Eliminar todos los *tags* de exportación corruptos de Word a Markdown (como `[]{#_bookmark...}`).
2. Limpiar el índice generado automáticamente con números sucios.
3. Asegurar que cada párrafo esté separado por una línea en blanco limpia (doble espacio).
4. Reemplazar listas con bloque `> ` usadas erróneamente en la portada por formato de texto estándar centrado.
