# Guía de Estilo y Manual de Maquetación del Proyecto (Estándar LaTeX / pdflatex)

Este documento establece las reglas obligatorias de formato, maquetación tipográfica, jerarquía estructural, nomenclatura y citación para el proyecto de grado, consolidando el nuevo diseño predeterminado implementado en el documento maestro [`main.md`](file:///home/robledo/PDG-TUG-V2/PDG_II_TUG/main.md).

---

## 1. Filosofía y Arquitectura Documental del Proyecto

El proyecto adopta formalmente el estándar **LaTeX nativo** (procesado con motor `pdflatex`), reemplazando el formateo preliminar en Markdown simple y eliminando cualquier residuo de etiquetas HTML (`<div align="center">`, `<br>`).

### Justificación Técnica de la Migración:
1. **Control Tipográfico Determinista:** Microtipografía (`microtype`), control milimétrico de quiebres de línea (`\emergencystretch{3em}`, `\sloppy`), justificación matemática y separación silábica precisa en castellano (`babel` con `spanish`, `es-tabla`, `es-lcroman`).
2. **Estructura Editorial y Paginación Dual:** Soporte formal de numeración romana en minúsculas (`\pagenumbering{roman}`) para preliminares (Tabla de contenido, Acrónimos, Glosario) y numeración arábiga (`\pagenumbering{arabic}`) para el cuerpo capitular.
3. **Formulación Matemática Rigurosa:** Entornos matemáticos de alta resolución (`amsmath`, `amssymb`) para deducciones cinemáticas, integrales temporales, densidades espectrales y filtros digitales.
4. **Estandarización de Referencias y Tablas:** Sangría francesa automática (`\hangindent=1.25cm`) y tablas científicas con calidad de publicación (`booktabs`, `longtable`).

---

## 2. Parámetros Globales y Preámbulo de Configuración

Todo documento formal del proyecto debe configurarse bajo los siguientes parámetros de compilación en su preámbulo:

```latex
%!TEX program = pdflatex
\documentclass[12pt,a4paper]{article}

% Codificación e idioma
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{textcomp}
\usepackage[spanish,es-tabla,es-lcroman]{babel}

% Geometría y márgenes
\usepackage[margin=2.5cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{microtype}
\usepackage{setspace}
\usepackage{enumitem}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{array}
\usepackage{pdflscape}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{xurl}
\usepackage[hidelinks,unicode,bookmarksnumbered]{hyperref}
```

### Especificaciones de Párrafo e Interlineado:
* **Interlineado:** `\setstretch{1.15}` (espaciado 1.15 líneas).
* **Sangría de primera línea:** `\setlength{\parindent}{0pt}` (párrafos en bloque, sin sangría inicial).
* **Espaciado inter-párrafo:** `\setlength{\parskip}{6pt plus 2pt minus 1pt}` (separación neta y homogénea de 6 puntos).
* **Colorimetría Institucional:** `\definecolor{icesi}{RGB}{0,0,0}`.

---

## 3. Jerarquía de Títulos y Secciones (`titlesec`)

La numeración de títulos debe ser jerárquica, correlativa y sobria, controlada mediante el paquete `titlesec` y configurando la profundidad a subsecciones (`secnumdepth = 2`, `tocdepth = 2`):

```latex
\titleformat{\section}{\Large\bfseries\color{icesi}}{\thesection.}{0.6em}{}
\titleformat{\subsection}{\large\bfseries\color{icesi}}{\thesubsection.}{0.6em}{}
\titleformat{\subsubsection}{\normalsize\bfseries\color{icesi}}{\thesubsubsection.}{0.6em}{}
\titlespacing*{\section}{0pt}{1.5ex plus 1ex}{1ex}
\titlespacing*{\subsection}{0pt}{1.2ex plus 1ex}{0.8ex}

\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{2}
\addto\captionsspanish{\renewcommand{\contentsname}{Tabla de contenido}}
```

### Secciones sin Número en el Índice:
Para aquellas secciones preliminares que no llevan numeración arábiga pero deben constar obligatoriamente en la Tabla de Contenido, se define la macro:
```latex
\newcommand{\seccionsinnumero}[1]{%
  \section*{#1}%
  \addcontentsline{toc}{section}{#1}%
}
```

---

## 4. Encabezados y Pies de Página (`fancyhdr`)

A partir del inicio del cuerpo capitular se utiliza el estilo `fancy`, garantizando trazabilidad institucional y del documento:

```latex
\setlength{\headheight}{15pt}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape Análisis de Datos de la Prueba TUG en Pacientes con EP}
\fancyhead[R]{\small Proyecto de Grado I}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
```

* **Encabezado Izquierdo:** Título abreviado del proyecto en cursiva (`\small\itshape`).
* **Encabezado Derecho:** Nombre de la asignatura (`\small Proyecto de Grado I`).
* **Pie de Página:** Foliación arábiga centrada (`\thepage`).
* **Línea de Encabezado:** Filete continuo de `0.4pt`.

---

## 5. Estructura y Protocolo de Páginas

El documento se divide de manera estricta en tres macro-bloques:

### A. Portada Formal (`\begin{titlepage}`)
Ocupa exactamente una página aislada sin encabezados ni números de página (`\thispagestyle{empty}`):
1. **Encabezado:** Institución (`\Large\bfseries Universidad ICESI\par`) y Programas Académicos (`\large Ingeniería Telemática e Ingeniería de Sistemas\par`).
2. **Título del Proyecto:** Enmarcado entre dos reglas horizontales completas de grosor `1.2pt` (`\rule{\textwidth}{1.2pt}`), con tipografía `\LARGE\bfseries\color{icesi}`.
3. **Contexto Curricular:** `\Large\bfseries Proyecto de Grado I\par`.
4. **Autores:** Título en `\large\bfseries Autores\par` seguido de los cuatro autores ordenados alfabéticamente por apellido o consensuados en el grupo.
5. **Tutores:** Título en `\large\bfseries Tutores\par` con los docentes directores (`Domiciano Rincón` y `Andrés Navarro`).
6. **Pie de Portada:** Espaciador vertical expansivo (`\vfill`) y ubicación geográfica (`Cali, Colombia\par`).

### B. Páginas Preliminares (`\pagenumbering{roman}`)
Cada una de las secciones preliminares debe ocupar **su propia página independiente** mediante el comando `\newpage`:
1. **Tabla de Contenido:** Generada automáticamente vía `\tableofcontents`.
2. **Lista de Acrónimos:** Definida mediante `\seccionsinnumero{Lista de Acrónimos}`, empleando el entorno `description` multilínea con alineación rígida a 3.6 cm:
   ```latex
   \newcommand{\acronimo}[2]{\item[#1] #2}
   \begin{description}[style=multiline,leftmargin=3.6cm,font=\bfseries,itemsep=6pt]
     \acronimo{IMU}{Unidad de medición inercial (\emph{Inertial Measurement Unit}).}
     \acronimo{TUG}{Prueba de levantarse, caminar y sentarse (\emph{Timed Up and Go}).}
     ...
   \end{description}
   ```
3. **Glosario de Términos:** Definido mediante `\seccionsinnumero{Glosario de Términos}`, empleando el entorno `description` con quiebre de línea para el término (`style=nextline`):
   ```latex
   \newcommand{\termino}[2]{\item[#1] #2}
   \begin{description}[style=nextline,leftmargin=0.8cm,font=\bfseries,itemsep=8pt]
     \termino{Bradicinesia}{Lentitud del movimiento acompañada de una reducción progresiva...}
     ...
   \end{description}
   ```

### C. Cuerpo Capitular (`\pagenumbering{arabic}`)
Se reinicia la foliación en números arábigos con las secciones numeradas correlativamente:
* `\section{Introducción}\label{sec:introduccion}`
  * `\subsection{Planteamiento del problema}\label{sec:problema}`
* `\section{Objetivos}\label{sec:objetivos}`
  * `\subsection{Objetivo general}\label{sec:objetivo-general}`
  * `\subsection{Objetivos específicos}\label{sec:objetivos-especificos}`
  * `\subsection{Alcance}\label{sec:alcance}`
  * `\subsection{Límites del proyecto}\label{sec:limites}`
* `\section{Antecedentes del proyecto}\label{sec:antecedentes}`
* `\section{Marco teórico}\label{sec:marco-teorico}`
  * `\subsection{Enfermedad de Parkinson (EP)}`
  * `\subsection{Análisis biomecánico motor}`
  * `\subsection{Prueba Timed Up and Go (TUG)}`
  * `\subsection{Unidades de Medición Inercial (IMU)}`
  * `\subsection{Cámaras de Profundidad RGB-D}`
* `\section{Estado del arte}\label{sec:estado-del-arte}`
  * `\subsection{Del TUG convencional al TUG instrumentado}`
  * `\subsection{IMU: segmentación y características}`
  * `\subsection{RGB-D y análisis no invasivo}`
  * `\subsection{Severidad y biomarcadores}`
  * `\subsection{Variables espaciotemporales prioritarias y modelado cinemático mediante IMU}`

---

## 6. Notación Matemática y Deducciones Cinemáticas

Toda formulación física o cinemática debe desarrollarse con rigor matemático mediante LaTeX:
* **Variables y Escalares:** Cursiva estándar ($t$, $f_s$, $T_{\text{total}}$).
* **Vectores y Matrices:** Negrita vertical ($\mathbf{a}(t) = [a_x, a_y, a_z]^T$, $\boldsymbol{\omega}(t) = [\omega_x, \omega_y, \omega_z]^T$).
* **Ecuaciones en Bloque:** Entornos `\[ ... \]`, `equation` o `align` con numeración y etiquetas cuando sean referenciadas en el texto.
* **Unidades Físicas:** Separadas por espacio fino (`\,`), sin cursiva ($50\,\text{Hz}$, $9.81\,\text{m/s}^2$, $180^\circ$, $200\,^\circ/\text{s}$).

### Ejemplo de Deducción Cinemática Estándar (Giro TUG):
$$
\Delta \theta_{\text{turn}} = \int_{t_{\text{start}}}^{t_{\text{end}}} \omega_{\text{yaw}}(t) \, dt \approx \sum_{k=k_{\text{start}}}^{k_{\text{end}}} \omega_{\text{yaw}}[k] \cdot \Delta t
$$
$$
\omega_{\text{peak}} = \max_{t \in [t_{\text{start}}, t_{\text{end}}]} \lvert \omega_{\text{yaw}}(t) \rvert
$$

---

## 7. Diseño de Tablas Científicas (`booktabs` y `longtable`)

Queda estrictamente prohibido el uso de bordes verticales o celdas de colores estridentes. Las tablas deben adherirse al estándar tipográfico de `booktabs`:
1. Filete superior grueso: `\toprule`.
2. Filete intermedio divisorio de encabezados: `\midrule`.
3. Filete inferior de cierre: `\bottomrule`.
4. El paquete `babel` en español con opción `es-tabla` asigna automáticamente el prefijo **Tabla** en lugar de *Cuadro*.
5. Toda tabla debe incluir una nota explicativa al pie detallando abreviaturas y fuentes de respaldo.

---

## 8. Normas de Citación y Referencias Bibliográficas

Las referencias se compilan mediante un entorno dedicado que aplica **sangría francesa de 1.25 cm** y separación entre citas de 8 puntos:

```latex
\newenvironment{referencias}{%
  \setlength{\parindent}{0pt}%
  \setlength{\parskip}{8pt}%
  \begingroup\raggedright\small
}{\endgroup}
\newcommand{\refitem}[1]{\par\hangindent=1.25cm\hangafter=1 #1\par}
```

### Reglas de Citación:
1. **Citación en el Texto:** Sistema Autor-Fecha bajo norma APA 7:
   * Parentética: `(Zampieri et al., 2010)` o `(Molero-Mateo et al., 2026)`.
   * Narrativa: `Zampieri et al. (2010)` o `Caramia et al. (2018)`.
   * En tres o más autores, usar siempre `et al.` desde la primera mención.
2. **Entrada en la Lista de Referencias:**
   * Orden estrictamente alfabético por el apellido del primer autor.
   * Hipervínculos a los identificadores digitales DOI mediante `\url{https://doi.org/...}` gestionados por `xurl` para evitar roturas de línea defectuosas.
   * Ejemplo canónico:
     ```latex
     \refitem{Zampieri, C., Salarian, A., Carlson-Kuhta, P., Aminian, K., Nutt, J. G., \& Horak, F. B. (2010). The instrumented Timed Up and Go test: Potential outcome measure for disease modifying therapies in Parkinson's disease. \emph{Journal of Neurology, Neurosurgery \& Psychiatry, 81}(2), 171--176. \url{https://doi.org/10.1136/jnnp.2009.173740}}
     ```

---

## 9. Compilación y Validación

Para compilar el documento maestro a PDF preservando referencias cruzadas, marcadores e hipervínculos:
```bash
pdflatex main.md && pdflatex main.md
```
*(Dos pasadas consecutivas para consolidar la tabla de contenido y las etiquetas `\label` y `\ref`).*
