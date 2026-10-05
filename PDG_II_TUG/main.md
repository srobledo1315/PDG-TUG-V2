%!TEX program = pdflatex
\documentclass[12pt,a4paper]{article}

%------------------------------------------------------------
% Codificación e idioma
%------------------------------------------------------------
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{textcomp}
\usepackage[spanish,es-tabla,es-lcroman]{babel}

%------------------------------------------------------------
% Paquetes generales
%------------------------------------------------------------
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

%------------------------------------------------------------
% Formato general
%------------------------------------------------------------
\setstretch{1.15}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt plus 2pt minus 1pt}
\setlength{\emergencystretch}{3em}
\sloppy

\definecolor{icesi}{RGB}{0,0,0}

\titleformat{\section}{\Large\bfseries\color{icesi}}{\thesection.}{0.6em}{}
\titleformat{\subsection}{\large\bfseries\color{icesi}}{\thesubsection.}{0.6em}{}
\titleformat{\subsubsection}{\normalsize\bfseries\color{icesi}}{\thesubsubsection.}{0.6em}{}
\titlespacing*{\section}{0pt}{1.5ex plus 1ex}{1ex}
\titlespacing*{\subsection}{0pt}{1.2ex plus 1ex}{0.8ex}

% Tabla de contenido: hasta subsecciones
\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{2}
\addto\captionsspanish{\renewcommand{\contentsname}{Tabla de contenido}}

% Encabezado y pie de página
\setlength{\headheight}{15pt}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape Análisis de Datos de la Prueba TUG en Pacientes con EP}
\fancyhead[R]{\small Proyecto de Grado I}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}

% Sección sin número pero incluida en la tabla de contenido
\newcommand{\seccionsinnumero}[1]{%
  \section*{#1}%
  \addcontentsline{toc}{section}{#1}%
}

% Entradas del glosario y de la lista de acrónimos
\newcommand{\acronimo}[2]{\item[#1] #2}
\newcommand{\termino}[2]{\item[#1] #2}

% Referencias con sangría francesa
\newenvironment{referencias}{%
  \setlength{\parindent}{0pt}%
  \setlength{\parskip}{8pt}%
  \begingroup\raggedright\small
}{\endgroup}
\newcommand{\refitem}[1]{\par\hangindent=1.25cm\hangafter=1 #1\par}

\begin{document}

%============================================================
% PORTADA (una sola página)
%============================================================
\begin{titlepage}
  \thispagestyle{empty}
  \centering
  \singlespacing
  \vspace*{0.5cm}

  {\Large\bfseries Universidad ICESI\par}
  \vspace{0.4cm}
  {\large Ingeniería Telemática e Ingeniería de Sistemas\par}

  \vspace{1.4cm}
  \rule{\textwidth}{1.2pt}\par
  \vspace{0.6cm}
  {\LARGE\bfseries\color{icesi}
   Análisis de Datos de la Prueba TUG para Variables Espaciotemporales en
   Pacientes con Enfermedad de Parkinson\par}
  \vspace{0.6cm}
  \rule{\textwidth}{1.2pt}\par

  \vspace{1.2cm}
  {\Large\bfseries Proyecto de Grado I\par}

  \vspace{1.2cm}
  {\large\bfseries Autores\par}
  \vspace{0.3cm}
  {\large
   Juan José Arias Gallego\par
   Esteban Guarin Valencia\par
   Santiago Gómez Robledo\par
   Heiner Danit Rincón Carrillo\par}

  \vspace{0.7cm}
  {\large\bfseries Tutores\par}
  \vspace{0.3cm}
  {\large
   Domiciano Rincón\par
   Andrés Navarro\par}

  \vfill
  {\large Cali, Colombia\par}
\end{titlepage}

%============================================================
% TABLA DE CONTENIDO (página propia)
%============================================================
\pagenumbering{roman}
\tableofcontents
\newpage

%============================================================
% LISTA DE ACRÓNIMOS (página propia)
%============================================================
\seccionsinnumero{Lista de Acrónimos}

\begin{description}[style=multiline,leftmargin=3.6cm,font=\bfseries,itemsep=6pt]
  \acronimo{AUC}{Área bajo la curva (\emph{Area Under the Curve}).}
  \acronimo{EP}{Enfermedad de Parkinson.}
  \acronimo{FFT}{Transformada rápida de Fourier (\emph{Fast Fourier Transform}).}
  \acronimo{I2T}{Grupo de Investigación en Informática y Telecomunicaciones.}
  \acronimo{IMU}{Unidad de medición inercial (\emph{Inertial Measurement Unit}).}
  \acronimo{iTUG}{Prueba de levantarse, caminar y sentarse instrumentada (\emph{Instrumented Timed Up and Go}).}
  \acronimo{L5}{Quinta vértebra lumbar (ubicación anatómica del sensor inercial).}
  \acronimo{MDS}{Sociedad de Trastornos del Movimiento (\emph{Movement Disorder Society}).}
  \acronimo{MDS-UPDRS}{Escala Unificada de Evaluación de la Enfermedad de Parkinson de la MDS (\emph{MDS - Unified Parkinson's Disease Rating Scale}).}
  \acronimo{RGB-D}{Cámara de color y profundidad (\emph{Red, Green, Blue - Depth}).}
  \acronimo{TUG}{Prueba de levantarse, caminar y sentarse (\emph{Timed Up and Go}).}
\end{description}
\newpage

%============================================================
% GLOSARIO DE TÉRMINOS (página propia)
%============================================================
\seccionsinnumero{Glosario de Términos}

\begin{description}[style=nextline,leftmargin=0.8cm,font=\bfseries,itemsep=8pt]
  \termino{Bradicinesia}{Lentitud del movimiento acompañada de una reducción progresiva en su velocidad o amplitud durante tareas repetitivas; es el síntoma motor principal de la enfermedad de Parkinson.}
  \termino{Cadencia}{Número de pasos realizados por unidad de tiempo (usualmente pasos por minuto) durante la marcha.}
  \termino{Congelamiento de la marcha (\emph{Freezing of Gait})}{Incapacidad breve e involuntaria para iniciar o mantener la marcha, en la que los pies parecen quedar temporalmente <<pegados al suelo>>.}
  \termino{Doble apoyo}{Intervalo dentro del ciclo de marcha en el que ambos pies permanecen simultáneamente en contacto con la superficie.}
  \termino{Energía espectral}{Distribución de la energía o potencia de una señal a lo largo de las distintas frecuencias, obtenida mediante transformaciones al dominio frecuencial (como la FFT).}
  \termino{Escala de Hoehn y Yahr}{Sistema de clasificación clínica utilizado para categorizar el estadio de progresión y compromiso motor en la enfermedad de Parkinson.}
  \termino{Estimación de pose}{Técnica de visión por computador y aprendizaje profundo utilizada para identificar y rastrear la posición tridimensional de las articulaciones y segmentos corporales a partir de datos ópticos o de profundidad.}
  \termino{Fase de apoyo}{Intervalo del ciclo de marcha en el cual el pie se encuentra en contacto directo con el suelo soportando el peso corporal.}
  \termino{Fase de balanceo}{Intervalo del ciclo de marcha en el que el pie no toca el suelo y el miembro avanza para preparar el siguiente paso.}
  \termino{Fases de la prueba TUG}{Etapas funcionales que componen la ejecución completa de la prueba: levantamiento, primera marcha, giro, segunda marcha (regreso) y sentada.}
  \termino{Festinación}{Patrón de marcha anormal caracterizado por pasos breves, rápidos y acelerados involuntariamente, con tendencia a inclinar el centro de gravedad hacia adelante.}
  \termino{Filtro pasabajas Butterworth}{Algoritmo de filtrado digital empleado en el preprocesamiento de señales inerciales para suavizar la señal y atenuar el ruido de alta frecuencia, preservando la forma de onda del movimiento.}
  \termino{Guiñada (\emph{Yaw})}{Velocidad angular o rotación sobre el eje vertical del cuerpo, clave para la detección y caracterización cinemática de los giros.}
  \termino{Inestabilidad postural}{Deficiencia en los reflejos de equilibrio que dificulta el mantenimiento de una postura erguida estable e incrementa el riesgo de caídas.}
  \termino{Ingeniería de características}{Proceso de selección, extracción y transformación de variables cuantitativas a partir de las señales para alimentar los algoritmos de clasificación o análisis estadístico.}
  \termino{Métrica biomecánica}{Parámetro cuantitativo (espacial, temporal, cinemático o cinético) utilizado para describir el comportamiento del cuerpo humano durante el movimiento.}
  \termino{Pipeline de procesamiento}{Secuencia automatizada y estructurada de etapas de software (filtrado, detección de picos, umbralización y segmentación) para el tratamiento de señales inerciales o imágenes de profundidad.}
  \termino{Segmentación de señales}{Proceso de dividir una señal continua en partes o intervalos discretos que representan distintas fases o eventos dentro de un movimiento.}
  \termino{Velocidad angular}{Tasa de variación de la orientación respecto al tiempo, registrada principalmente por los giroscopios de los sensores inerciales.}
\end{description}
\newpage

%============================================================
% CUERPO DEL DOCUMENTO
%============================================================
\pagenumbering{arabic}

%------------------------------------------------------------
\section{Introducción}\label{sec:introduccion}

La enfermedad de Parkinson (EP) es un trastorno neurodegenerativo progresivo cuya expresión clínica incluye bradicinesia, rigidez, temblor en reposo y alteraciones del control postural. Estas manifestaciones afectan la movilidad funcional y pueden modificar la marcha, las transiciones posturales y la capacidad de girar de manera segura. Aunque la evaluación clínica continúa siendo indispensable, la cuantificación objetiva del movimiento puede complementar las escalas médicas al describir cambios sutiles y específicos de la ejecución motora (Postuma et al., 2015; Russo et al., 2025).

La prueba \emph{Timed Up and Go} (TUG) es una herramienta funcional que consta de cinco fases: levantamiento, primera marcha, giro de 180 grados, segunda marcha de retorno y sentada. Su resultado clínico convencional es el tiempo total de ejecución. En personas con EP, la prueba TUG posee utilidad clínica y propiedades psicométricas aceptables; sin embargo, un único tiempo global no identifica qué componente funcional explica un desempeño alterado ni cuantifica de forma directa la calidad del movimiento (Mollinedo \& Cancela, 2020).

La instrumentación de la prueba TUG permite extraer variables biomecánicas específicas por fase. Para este propósito se utiliza la fusión de dos modalidades de captura: unidades de medición inercial (IMU) y cámaras de profundidad RGB-D. El objetivo de las IMU (ubicadas en la región lumbar y en los tobillos) es capturar datos cinemáticos de alta resolución temporal, como la aceleración y la velocidad angular, mientras que la cámara RGB-D tiene como objetivo modelar de forma no invasiva las trayectorias espaciales corporales. La literatura demuestra que la combinación de estas tecnologías, especialmente durante los giros y las transiciones posturales, contiene información crítica para la evaluación de alteraciones motoras (Vervoort et al., 2016; Zampieri et al., 2010).

La adquisición de datos para este proyecto se llevó a cabo durante brigadas médicas en la Clínica Valle del Lili. En estas jornadas se capturaron muestras de aproximadamente 70 participantes (entre pacientes con Parkinson y sujetos de control). Es fundamental destacar que se empleó un esquema de fusión sensorial simultánea: a cada paciente se le equiparon los sensores IMU al mismo tiempo que era grabado por la cámara RGB-D. De esta manera se obtuvo una misma muestra bimodal (inercial y óptica) unificada para cada ejecución de la prueba.

Este proyecto se fundamenta en dicha base de datos recolectada para segmentar las muestras, analizar la información conjunta procedente de las IMU y las cámaras, e implementar algoritmos de clasificación de patrones motores que apoyen la caracterización objetiva de la enfermedad.

\subsection{Planteamiento del problema}\label{sec:problema}

En la práctica clínica, el tiempo total del TUG es una medida simple, útil y de rápida aplicación; no obstante, resume en un solo valor acciones motoras con demandas diferentes.

Dos personas pueden obtener tiempos semejantes y, aun así, presentar alteraciones de distinta naturaleza: una puede requerir más tiempo para levantarse, otra puede mostrar giros lentos y fragmentados y otra puede caminar con menor longitud de paso o mayor variabilidad. Por tanto, el tiempo global no es suficiente para describir la heterogeneidad biomecánica del desempeño funcional en EP.

La evidencia muestra que el TUG instrumentado permite descomponer el desempeño en subfases y extraer métricas más sensibles que el tiempo total. Sin embargo, persisten desafíos relacionados con la heterogeneidad de protocolos, la selección de características, la comparación entre modalidades de censado y la validación de clasificadores sobre bases de datos clínicas (Ortega-Bastidas et al., 2023). En particular, la integración analítica de información IMU y RGB-D para estudiar fases individuales del TUG representa una oportunidad para generar indicadores cuantitativos de movilidad que complementen la evaluación clínica.

En consecuencia, el problema central de ingeniería radica en la ausencia de un marco analítico y algorítmico que permita la extracción e identificación objetiva de patrones motores a partir de las subfases de la prueba TUG instrumentada. Esta carencia metodológica tiene como causa la complejidad de procesar datos crudos bimodales (IMU y RGB-D) frente a la insuficiencia clínica del tiempo global de la prueba convencional, lo cual genera como consecuencia una limitación para clasificar automáticamente a pacientes con enfermedad de Parkinson frente a sujetos de control, dificultando así el apoyo tecnológico para un diagnóstico objetivo.

%------------------------------------------------------------
\section{Objetivos}\label{sec:objetivos}

\subsection{Objetivo general}\label{sec:objetivo-general}

Desarrollar un algoritmo de clasificación para diferenciar pacientes con enfermedad de Parkinson y sujetos de control a partir de variables biomecánicas extraídas de cada fase de la prueba \textit{Timed Up and Go} (TUG) mediante el análisis conjunto de señales inerciales (IMU) y cámaras de profundidad (RGB-D), integrándolo en la plataforma VIMOV como herramienta de apoyo al diagnóstico clínico objetivo.

\subsection{Objetivos específicos}\label{sec:objetivos-especificos}

\begin{itemize}[itemsep=4pt]
\item Realizar la exploración del conjunto de datos bimodal (señales inerciales IMU y video RGB-D) conformado por aproximadamente 70 muestras de diferentes participantes adquiridas en brigadas de la prueba TUG, identificando patrones motores y variables biomecánicas relevantes de acuerdo con la literatura científica.
  \item Validar el algoritmo de segmentación de fases del proyecto predecesor sobre el conjunto de datos adquiridos en brigadas, ajustándolo a la última versión de los sistemas de adquisición de datos.
  \item Desarrollar un algoritmo de clasificación que diferencie los patrones motores de pacientes con Parkinson y sujetos de control, extrayendo para cada fase las variables biomecánicas priorizadas en la exploración de datos.
  \item Integrar los algoritmos de segmentación y clasificación de la prueba TUG en la plataforma VIMOV,  facilitando la ingesta, ejecución computacional y persistencia de las métricas obtenidas.

\end{itemize}

\subsection{Alcance}\label{sec:alcance}

El alcance de este proyecto comprende el desarrollo y evaluación de un algoritmo computacional capaz de clasificar patrones de movilidad entre pacientes con enfermedad de Parkinson y sujetos de control, analizando de forma independiente cada fase de la prueba \emph{Timed Up and Go} (TUG). Este proceso abarca el preprocesamiento del conjunto de datos estructurado, la validación de la segmentación de fases, la ingeniería de características biomecánicas y la validación del modelo de clasificación.

El entregable principal es un algoritmo funcional e implementado dentro del ecosistema tecnológico de los sistemas T-motion y VIMOV, el cual permitirá, como mínimo, clasificar de manera automática a pacientes y controles según los datos inerciales de cada fase de la prueba.

\subsection{Límites del proyecto}\label{sec:limites}

El producto de este proyecto funcionará exclusivamente como un componente de apoyo tecnológico para la cuantificación objetiva de la movilidad. El sistema desarrollado no pretende reemplazar el diagnóstico médico neurológico, el criterio de los especialistas ni las escalas clínicas establecidas (como la MDS-UPDRS). Los resultados arrojados por el algoritmo de clasificación deben interpretarse como una herramienta de asistencia sujeta a la validación e interpretación del personal de salud.

%------------------------------------------------------------
\section{Antecedentes del proyecto}\label{sec:antecedentes}

El grupo I2T mantiene colaboración con el servicio de neurología de la Fundación Valle del Lili desde 2010 y ha desarrollado herramientas para el análisis de marcha, movilidad y deterioro cognitivo. El macroproyecto busca construir tecnologías de apoyo para el diagnóstico, seguimiento y estudio de enfermedades neurodegenerativas y envejecimiento, articulando personal clínico, investigadores y estudiantes de pregrado y posgrado.

El proyecto predecesor directo, <<Timed Up and Go con unidades inerciales>>, implementó una arquitectura para procesamiento asíncrono y persistencia de señales, integrada a componentes como MinIO, PostgreSQL y la plataforma Vimov. En la dimensión analítica, desarrolló un \emph{pipeline} para segmentar fases del TUG a partir de IMU ubicadas en L5 y ambos tobillos. El procedimiento combinó filtrado pasabajas Butterworth, detección de picos, umbrales sobre energía espectral y análisis FFT para reconocer las transiciones entre levantarse, marcha de ida, giro, marcha de regreso y sentarse.

La principal brecha que deja el proyecto predecesor es el uso sistemático de las fases segmentadas para extraer características, contrastarlas con información clínica y construir modelos de análisis o clasificación. TUG 2 responde a esa brecha y añade el análisis de datos provenientes de cámara RGB-D. Esta continuidad permite concentrar el esfuerzo en la validación y la generación de evidencia sobre el desempeño del sistema, en lugar de reiniciar la infraestructura de adquisición y segmentación.

%------------------------------------------------------------
\section{Marco teórico}\label{sec:marco-teorico}

\subsection{Enfermedad de Parkinson (EP)}\label{sec:ep}

La EP es una enfermedad neurodegenerativa progresiva vinculada con disfunción de circuitos dopaminérgicos de los ganglios basales. Los criterios diagnósticos de la \emph{Movement Disorder Society} establecen el parkinsonismo como bradicinesia asociada con temblor en reposo o rigidez; la evaluación clínica también considera criterios de exclusión, señales de alerta y criterios de apoyo (Postuma et al., 2015).

La bradicinesia no equivale únicamente a menor velocidad: incluye reducción progresiva de la amplitud o de la velocidad del movimiento y puede expresarse como vacilaciones o interrupciones durante tareas repetitivas. En la movilidad funcional, estas alteraciones se asocian con menor automaticidad de la marcha, pasos más cortos, reducción de la velocidad, mayor tiempo de doble apoyo, variabilidad entre pasos, menor balanceo de brazos y dificultades en transiciones y giros (Russo et al., 2025).

La marcha parkinsoniana es heterogénea. En estadios tempranos, algunas alteraciones pueden ser discretas y confundirse con cambios asociados al envejecimiento o con otras condiciones. En fases más avanzadas pueden aparecer festinación, inestabilidad postural y congelamiento de la marcha, especialmente durante el inicio de la marcha, los giros, los pasos estrechos o las tareas que incrementan la demanda atencional. Por ello, medir múltiples dimensiones del desempeño motor resulta más informativo que utilizar una única variable temporal.

La escala de Hoehn y Yahr y la MDS-UPDRS son referentes clínicos frecuentes para describir severidad y compromiso motor. Sin embargo, las escalas no proporcionan una descripción detallada de cada componente biomecánico. La medición instrumentada puede complementar estas evaluaciones al generar indicadores cuantitativos, reproducibles y potencialmente sensibles a cambios en la movilidad.

\subsection{Análisis biomecánico motor}\label{sec:biomecanico}

El análisis biomecánico motor estudia el movimiento humano a partir de variables temporales, espaciales, cinemáticas y cinéticas. En el análisis de marcha, las variables espaciotemporales incluyen velocidad, cadencia, longitud de paso, longitud de zancada, tiempo de paso y duración del doble apoyo. Las variables cinemáticas describen posiciones, trayectorias, ángulos, rangos de movimiento, aceleraciones y velocidades angulares. Las variables cinéticas se relacionan con fuerzas, momentos y potencias articulares, y suelen requerir plataformas de fuerza o sistemas de laboratorio especializados.

La marcha es un patrón cíclico compuesto por fase de apoyo y fase de balanceo. La fase de apoyo corresponde al intervalo en que el pie mantiene contacto con el suelo; la fase de balanceo ocurre cuando el miembro avanza para preparar el siguiente contacto. Los periodos de doble apoyo corresponden a los instantes en que ambos pies están en contacto con el suelo y reflejan la transferencia del peso corporal. Cambios en estas fases pueden indicar estrategias compensatorias, inestabilidad o alteraciones del control motor.

En la EP, la literatura describe disminución de la velocidad, menor longitud de paso y de zancada, incremento del doble apoyo y modificaciones de la coordinación intersegmentaria. Además, se han reportado cambios en el rango de movimiento de tobillo, rodilla, cadera, pelvis y tronco, así como alteraciones de momentos y potencias articulares (Russo et al., 2025). La identificación de tales características permite representar de forma más completa la movilidad del participante.

Dentro del TUG, el análisis debe diferenciar al menos cuatro dominios biomecánicos: transiciones posturales, marcha recta, giros y control de la sentada. Las transiciones informan sobre la producción de impulso y el control del tronco; la marcha permite estimar periodicidad, velocidad y regularidad; los giros reflejan reorientación corporal y estabilidad dinámica; y la sentada permite observar la desaceleración y el control postural. Esta diferenciación es especialmente pertinente en la EP, donde los giros y las transiciones pueden deteriorarse de manera desproporcionada frente al tiempo global.

\subsection{Prueba de \emph{Timed Up and Go} (TUG)}\label{sec:tug}

El TUG es una prueba de movilidad funcional en la que el resultado tradicional es el tiempo requerido para completar una secuencia de levantarse, caminar, girar y sentarse (Podsiadlo \& Richardson, 1991). Su utilidad práctica reside en que reúne tareas funcionales cotidianas y puede implementarse con recursos mínimos en un entorno clínico.

En la EP, el TUG es pertinente porque demanda planificación motora, equilibrio dinámico, coordinación, cambio de dirección y control de transiciones. La revisión sistemática de Mollinedo y Cancela (2020) encontró evidencia de confiabilidad de moderada a buena y validez adecuada del TUG en personas con EP. No obstante, los autores advirtieron heterogeneidad en los protocolos y evidencia limitada sobre la sensibilidad al cambio. Estas observaciones no invalidan el TUG; muestran que la interpretación del tiempo total debe complementarse con medidas más granulares.

La introducción del TUG instrumentado se justifica porque transforma una medida global en una evaluación por componentes. En vez de registrar únicamente cuánto tarda una persona en realizar el ensayo, permite examinar dónde se origina la dificultad funcional. Este enfoque facilita la extracción de variables específicas por fase y ofrece una base para analizar patrones de movilidad mediante métodos estadísticos y de aprendizaje automático.

En este contexto, la instrumentación de la prueba (iTUG) incorpora sensores y algoritmos para identificar automáticamente los eventos que componen la prueba. Una segmentación útil comprende: levantarse de la silla, marcha de ida, giro de 180°, marcha de regreso, giro o aproximación final y sentarse. El número exacto de subfases puede variar según el protocolo, pero debe mantenerse consistente dentro del conjunto de datos y documentarse de manera explícita.

Cada subfase posee una firma cinemática distinta. El levantamiento se asocia con cambios marcados de aceleración y rotación del tronco; la marcha presenta patrones repetitivos relacionados con el ciclo de paso; los giros generan picos o cambios de velocidad angular de guiñada; y la sentada se caracteriza por la desaceleración y el control de la flexión del tronco. Estas firmas permiten detectar eventos, estimar la duración de las fases y calcular variables específicas.

Vervoort et al. (2016) analizaron datos de una IMU lumbar durante el TUG y mostraron que un conjunto de características de marcha, giro y transición postural permitió diferenciar grupos de edad con un AUC de 0.947. Aunque su población no fue exclusivamente parkinsoniana, el estudio es relevante porque demuestra que las subfases del TUG contienen información discriminativa y que el análisis multivariado de señales inerciales puede superar la interpretación basada únicamente en los segundos totales.

En pacientes con EP, Zampieri et al. (2010) mostraron que el iTUG puede aportar medidas de resultado útiles en enfermedad temprana, especialmente al considerar componentes como los giros y las transiciones posturales. Asimismo, la revisión de Ortega-Bastidas et al. (2023) identificó que los sensores inerciales predominan en las aplicaciones de iTUG y que la segmentación automática constituye un paso central para estimar variables relevantes para la movilidad y el riesgo de caídas.

\subsection{Unidad de Medición Inercial (IMU)}\label{sec:imu}

Las unidades de medición inercial integran, como mínimo, acelerómetros y giroscopios triaxiales. Los acelerómetros miden aceleración lineal, mientras que los giroscopios registran velocidad angular. En el TUG, una IMU ubicada en la región lumbar puede capturar de manera eficiente movimientos globales del tronco y cambios asociados con levantarse, caminar, girar y sentarse. Sensores adicionales en tobillos o pies permiten caracterizar de forma más detallada eventos del paso y simetrías entre miembros.

Entre las ventajas de las IMU se encuentran su portabilidad, frecuencia de muestreo, costo relativamente bajo y aplicabilidad en entornos clínicos o domiciliarios. Sus limitaciones incluyen sensibilidad a la posición y orientación del sensor, ruido, errores de fijación y deriva cuando se integran señales. Por esta razón, los algoritmos deben incluir procedimientos de preprocesamiento, control de calidad y segmentación robusta.

\subsection{Cámaras de Profundidad RGB-D}\label{sec:rgbd}

Las cámaras RGB-D combinan imagen de color con información de profundidad, lo que permite estimar la posición tridimensional aproximada de segmentos y articulaciones corporales sin adherir sensores al paciente. A partir de la estimación de pose pueden derivarse trayectorias, desplazamiento corporal, duración de fases, velocidad de marcha, oscilación del tronco, balanceo de brazos y variables espaciales relacionadas con el paso y el giro.

La principal ventaja de RGB-D es su naturaleza no invasiva y su capacidad de observar el cuerpo completo. Sin embargo, la precisión puede verse afectada por oclusiones, distancia, posición relativa del participante, iluminación, ropa, campo de visión y errores del algoritmo de estimación esquelética. Por tanto, una alta repetibilidad de una modalidad no implica que sus métricas sean intercambiables con las de una IMU; cada sensor observa dimensiones diferentes del movimiento y debe validarse según su propósito.

Estudios con Kinect han demostrado la viabilidad de automatizar el TUG y caracterizar variables de marcha en población con EP. Tan et al. (2019) analizaron la marcha y el TUG modificado con Kinect en personas con EP, mientras que van Kersbergen et al. (2021) reportaron diferencias entre pacientes y controles en variables como la longitud de paso y la velocidad de marcha. Choi et al. (2022) mostraron que las subtareas del TUG pueden segmentarse mediante aprendizaje profundo a partir de cámaras RGB-D. Estos trabajos sustentan el uso de cámaras de profundidad como alternativa o complemento a la instrumentación inercial.

El estudio de Molero-Mateo et al. (2026) es especialmente relevante para este proyecto porque examinó el TUG instrumentado en 79 participantes (38 con EP y 41 controles) mediante IMU sincronizadas con fotogrametría optoelectrónica. El trabajo identificó marcadores biomecánicos en estadios tempranos de Hoehn y Yahr y muestra que el análisis por fases puede contribuir a la discriminación de alteraciones motoras tempranas. En consecuencia, TUG 2 debe priorizar la extracción de características interpretables por fase, el contraste con etiquetas clínicas disponibles y la evaluación cuidadosa de la generalización.

%------------------------------------------------------------
\section{Estado del arte}\label{sec:estado-arte}

El estado del arte se organiza por aporte metodológico y no como una enumeración de artículos. Se seleccionaron trabajos que sustentan una decisión concreta del proyecto: la pertinencia del TUG en EP, la segmentación por fases, la selección de variables biomecánicas, el uso de IMU, la captura RGB-D y la evaluación de clasificación. Se excluyen referencias que no aportan directamente al problema de análisis instrumentado del TUG.

\subsection{Del TUG convencional al TUG instrumentado}\label{sec:ea-tug}

Mollinedo y Cancela (2020) revisaron las propiedades psicométricas y las aplicaciones clínicas del TUG en EP. Su principal aporte consiste en confirmar su utilidad clínica, pero también señalar que la heterogeneidad de protocolos y la limitada evidencia de respuesta al cambio restringen la interpretación de un único tiempo total. Esta conclusión sustenta el uso de instrumentación y de variables por fase en lugar de reemplazar la prueba convencional.

Ortega-Bastidas et al. (2023) realizaron una revisión sistemática sobre iTUG y destacaron el predominio de sensores inerciales y de estrategias de segmentación automática. Este trabajo es relevante como mapa metodológico: ayuda a definir qué fases, sensores, variables y métodos de detección son recurrentes, y advierte que la diversidad de configuraciones dificulta las comparaciones directas entre estudios.

\subsection{IMU: segmentación y características}\label{sec:ea-imu}

Vervoort et al. (2016) analizaron datos inerciales durante el TUG mediante un enfoque multivariado. El estudio reportó que características de giros, marcha y transiciones posturales permitieron discriminar efectos relacionados con la edad con un AUC de 0.947. Para TUG 2, este artículo aporta un referente concreto de ingeniería de características y de evaluación de modelos a partir de fases, no solo del tiempo total.

Zampieri et al. (2010) evaluaron el iTUG como posible medida de resultado en EP y mostraron que las variables por componente pueden identificar deterioro motor sutil. Su aporte justifica el análisis de giros y transiciones posturales como dominios prioritarios de extracción de características.

Caramia et al. (2018) estudiaron cómo la ubicación de las IMU y la selección de características influyen en la clasificación de EP a partir de la marcha. El valor de este trabajo radica en advertir que el rendimiento de un clasificador depende de decisiones de adquisición y preprocesamiento; por ello, TUG 2 debe documentar la ubicación de los sensores, la frecuencia de muestreo, la selección de variables y la partición de datos.

\subsection{RGB-D y análisis no invasivo}\label{sec:ea-rgbd}

Dubois et al. (2018) demostraron la automatización del TUG mediante cámara de profundidad. Su aporte es validar la posibilidad de medir de manera objetiva la prueba sin sensores adheridos. Tan et al. (2019) extendieron esta línea a personas con EP y relacionaron medidas derivadas de Kinect con desenlaces físicos clínicos, reforzando el valor de las medidas ópticas para la caracterización funcional.

Van Kersbergen et al. (2021) evaluaron medidas objetivas de marcha basadas en cámara en personas con EP y controles. El estudio aporta evidencia de que variables ópticas como la velocidad y la longitud de paso pueden reflejar diferencias relacionadas con la enfermedad. Choi et al. (2022), por su parte, aplicaron aprendizaje profundo para segmentar subtareas del TUG con RGB-D, aportando una referencia directa para futuros enfoques automáticos de segmentación visual.

\subsection{Severidad y biomarcadores}\label{sec:ea-severidad}

Welzel et al. (2021) reportaron que la longitud de paso es un posible marcador de progresión en EP. Su aporte para el proyecto es clínico: muestra que una característica espaciotemporal puede tener mayor valor que medidas temporales aisladas para estudiar la severidad. Esta variable debe considerarse entre las características candidatas cuando la calidad de los datos RGB-D o IMU permita estimarla de manera confiable.

Molero-Mateo et al. (2026) analizaron marcadores biomecánicos del TUG en estadios tempranos de Hoehn y Yahr mediante IMU y fotogrametría optoelectrónica. Este artículo representa el antecedente más cercano a TUG 2 por tres razones: estudia EP, segmenta tareas funcionales del TUG y se interesa por la diferenciación de estadios tempranos. Su evidencia respalda explorar, solo si la base de datos lo permite, modelos que vayan más allá de paciente frente a control.

\subsection{Variables espaciotemporales prioritarias y modelado cinemático mediante IMU}\label{sec:ea-variables}

La instrumentación del test TUG mediante sensores inerciales permite desacoplar la cinemática de cada subfase funcional, superando la insensibilidad diagnóstica inherente a la métrica de tiempo total. Como establecen Mollinedo y Cancela (2020) y Zampieri et al. (2010), un registro temporal escalar global enmascara las deficiencias específicas asociadas a la bradicinesia, la rigidez axial y la inestabilidad postural. Por consiguiente, la literatura contemporánea prioriza la descomposición del movimiento en cinco fases discretas (incorporación, marcha de ida, giro intermedio, marcha de retorno y descenso a la silla), cuantificando descriptores biomecánicos objetivos a partir de aceleraciones lineales tridimensionales ($\mathbf{a}(t) = [a_x, a_y, a_z]^T$) y velocidades angulares triaxiales ($\boldsymbol{\omega}(t) = [\omega_x, \omega_y, \omega_z]^T$). La identificación rigurosa de estas variables cinemáticas permite construir vectores de características altamente discriminantes para diferenciar entre pacientes con enfermedad de Parkinson y sujetos de control pareados demográficamente.

La cinemática del giro intermedio de 180° constituye el dominio cinemático con mayor sensibilidad diagnóstica para evidenciar el compromiso extrapiramidal temprano. Vervoort et al. (2016) y Molero-Mateo et al. (2026) demostraron que la pérdida de disociación entre la cintura escapular y pélvica obliga a los pacientes con Parkinson a ejecutar rotaciones axiales fragmentadas, comúnmente denominadas <<giros en bloque>>. Desde el marco inercial de una IMU dispuesta en la columna lumbar (L5/\texttt{BASE-SPINE}), el giro se proyecta predominantemente sobre el eje vertical como una deflexión pronunciada de la velocidad angular de guiñada (\emph{yaw}), $\omega_{\text{yaw}}(t)$. La rotación angular total acumulada $\Delta \theta_{\text{turn}}$ se obtiene mediante la integral temporal de dicha velocidad:
\[
\Delta \theta_{\text{turn}} = \int_{t_{\text{start}}}^{t_{\text{end}}} \omega_{\text{yaw}}(t) \, dt \approx \sum_{k=k_{\text{start}}}^{k_{\text{end}}} \omega_{\text{yaw}}[k] \cdot \Delta t
\]
donde los límites de integración $t_{\text{start}}$ y $t_{\text{end}}$ se definen a partir del instante en que $\lvert \omega_{\text{yaw}}(t) \rvert$ cruza un umbral dinámico $\gamma_{\text{turn}}$ ajustado al nivel basal de ruido, cumpliéndose la restricción geométrica de inversión de marcha $\lvert \Delta \theta_{\text{turn}} \rvert \ge \pi\,\text{rad}$ ($180^\circ$). A partir de este intervalo se derivan la \textbf{duración del giro} ($\Delta t_{\text{turn}} = t_{\text{end}} - t_{\text{start}}$), la \textbf{velocidad angular pico de guiñada} ($\omega_{\text{peak}} = \max_{t \in [t_{\text{start}}, t_{\text{end}}]} \lvert \omega_{\text{yaw}}(t) \rvert$) y el \textbf{número de pasos de giro} ($N_{\text{steps\_turn}}$), cuantificado mediante la detección de picos de impacto vertical en las IMU de los tobillos (\texttt{LEFT-ANKLE} y \texttt{RIGHT-ANKLE}) dentro de la ventana de rotación. Mientras los sujetos sanos completan el giro de manera continua en 1 a 3 pasos con elevadas velocidades pico ($\omega_{\text{peak}} > 200\,^\circ/\text{s}$), los pacientes con EP demandan tiempos prolongados, cadencias cortas multidireccionales y una marcada atenuación de la velocidad angular pico ($\omega_{\text{peak}} < 120\,^\circ/\text{s}$).

Las transiciones posturales de incorporación (\emph{Sit-to-Stand}) y sentado (\emph{Stand-to-Sit}) permiten evaluar la transferencia de energía mecánica y el control del centro de masa corporal. Zampieri et al. (2010) y Ortega-Bastidas et al. (2023) señalan que los pacientes parkinsonianos manifiestan severas dificultades para vencer la inercia en reposo debido a la bradicinesia axial y al déficit en los músculos extensores de cadera. Para cuantificar la inclinación del tronco en el plano sagital durante la Fase 1, la velocidad angular de cabeceo (\emph{pitch}), $\omega_{\text{pitch}}(t)$, se integra y fusiona con el ángulo acelerométrico cuasi-estático mediante un filtro complementario que previene la deriva matemática:
\[
\theta_{\text{pitch}}[k] = \alpha \left( \theta_{\text{pitch}}[k-1] + \omega_{\text{pitch}}[k] \cdot \Delta t \right) + (1 - \alpha) \arctan \left( \frac{a_{\text{AP}}[k]}{\sqrt{a_{\text{V}}[k]^2 + a_{\text{ML}}[k]^2}} \right)
\]
donde $\alpha \in [0.95, 0.98]$ balancea la alta resolución dinámica del giróscopo con la estabilidad a bajas frecuencias de la aceleración gravitacional. Esta formulación permite deducir el rango de movimiento del tronco ($\text{ROM}_{\text{pitch}} = \max \theta_{\text{pitch}} - \min \theta_{\text{pitch}}$), la velocidad angular pico de flexión ($\omega_{\text{flex\_peak}} = \max \omega_{\text{pitch}}$) y la duración de la transición a bípedo ($\Delta t_{\text{STS}}$). Análogamente, en la Fase 5, el impacto vertical al sentarse ($a_{\text{impact}}$) se registra a partir del pico de deceleración vertical en L5 ($a_{\text{impact}} = \max \lvert a_{\text{V}}(t) \rvert$); en personas sanas este impacto es amortiguado por contracción muscular excéntrica controlada, mientras que en pacientes con déficit postural se observa un colapso abrupto contra la silla (\emph{plopping}).

La caracterización de la locomoción rectilínea (Fases 2 y 4) exige cuantificar la estabilidad dinámica, la regularidad periódica y la variabilidad espaciotemporal del paso. Caramia et al. (2018) y Welzel et al. (2021) demuestran que la reducción de la longitud de paso y la pérdida de automaticidad constituyen sellos patológicos cardinales de la enfermedad. Para extraer la regularidad armónica a partir de la aceleración vertical centrada de la espina lumbar $x[n] = a_{\text{V}}[n] - \bar{a}_{\text{V}}$, se computa la función de autocorrelación normalizada e insesgada sobre la ventana de marcha de $N$ muestras:
\[
R_{xx}[m] = \frac{1}{(N - m) \cdot \sigma_x^2} \sum_{n=0}^{N - m - 1} x[n] \cdot x[n + m]
\]
El primer pico no nulo $R_{xx}[m_1]$ en el retardo temporal $m_1 > 0$ cuantifica la regularidad del paso (\emph{step regularity}), correspondiente al semiciclo entre pasos alternos (contacto izquierdo-derecho), mientras que el segundo pico dominante $R_{xx}[m_2]$ en $m_2 \approx 2m_1$ mide la regularidad de la zancada (\emph{stride regularity}), correspondiente al ciclo de marcha completo del mismo miembro inferior. La simetría armónica de la marcha se formula como el cociente $\text{Simetría} = R_{xx}[m_1] / R_{xx}[m_2]$. Simultáneamente, a partir de la detección de los instantes discretos de contacto inicial del talón (\emph{Heel Strike}) $\{t_1, t_2, \dots, t_K\}$, se define el intervalo de tiempo de paso $\Delta t_k = t_{k+1} - t_k$, a partir del cual se extrae la variabilidad del tiempo de paso mediante el coeficiente de variación porcentual ($CV_{\text{step}}$):
\[
CV_{\text{step}} = \left( \frac{\sigma_{\Delta t}}{\mu_{\Delta t}} \right) \times 100\% = \left( \frac{\sqrt{\frac{1}{K-2}\sum_{k=1}^{K-1} (\Delta t_k - \mu_{\Delta t})^2}}{\frac{1}{K-1}\sum_{k=1}^{K-1} \Delta t_k} \right) \times 100\%
\]
En sujetos de control, $CV_{\text{step}} < 3\%$, mientras que en la EP se incrementa significativamente ($CV_{\text{step}} > 6\%$), reflejando inestabilidad en la marcha y riesgo inminente de caídas.

El análisis espectral de acelerometría y la cinemática de miembros superiores completan el perfil multivariado al capturar episodios paroxísticos y asimetrías tempranas del movimiento. Russo et al. (2025) y van Kersbergen et al. (2021) resaltan que el congelamiento de la marcha (\emph{Freezing of Gait}, FoG) y la reducción unilateral del braceo son biomarcadores de alto valor pronóstico. El índice de congelamiento de la marcha ($\text{FoG Index}$) se formula analíticamente a partir de la densidad espectral de potencia $P_{xx}(f)$ de la aceleración anteroposterior o vertical, estimada mediante el método de Welch:
\[
\text{FoG Index} = \frac{\int_{3\,\text{Hz}}^{8\,\text{Hz}} P_{xx}(f) \, df}{\int_{0.5\,\text{Hz}}^{3\,\text{Hz}} P_{xx}(f) \, df}
\]
donde el denominador captura la potencia en la banda fundamental de locomoción voluntaria ($0.5 - 3\,\text{Hz}$) y el numerador integra la energía de temblor patológico y parálisis motora ($3 - 8\,\text{Hz}$). Por su parte, la inclusión de sensores inerciales en ambas muñecas (LEFT-HAND y RIGHT-HAND) permite cuantificar la amplitud angular de balanceo para cada hemicuerpo ($\theta_{\text{swing}}^{\text{izq}}, \theta_{\text{swing}}^{\text{der}}$) integrando la velocidad angular sagital, derivando el índice de asimetría de balanceo de brazos ($ASA$):
\[
ASA = \frac{\lvert \theta_{\text{swing}}^{\text{izq}} - \theta_{\text{swing}}^{\text{der}} \rvert}{\max(\theta_{\text{swing}}^{\text{izq}}, \theta_{\text{swing}}^{\text{der}})} \times 100\%
\]
Este parámetro presenta una destacada capacidad discriminante en estadios precoces de Hoehn y Yahr, donde la afectación neurodegenerativa de la vía nigroestriatal suele debutar con asimetría unilateral en las extremidades superiores antes de propagarse simétricamente a los miembros inferiores.

La Tabla~\ref{tab:variables} sintetiza las quince variables cinemáticas y biomecánicas seleccionadas a partir del estado del arte, detallando su fase de extracción en el test TUG, su modelado matemático con sensores IMU, su comportamiento clínico reportado en pacientes con Parkinson y el artículo científico que respalda su pertinencia analítica.

\begin{landscape}
\small
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.3}
\begin{longtable}{>{\centering\arraybackslash}p{0.8cm} >{\raggedright\arraybackslash}p{4.2cm} >{\centering\arraybackslash}p{1.6cm} >{\raggedright\arraybackslash}p{6.2cm} >{\centering\arraybackslash}p{2.6cm} >{\centering\arraybackslash}p{2.2cm} >{\raggedright\arraybackslash}p{4.4cm}}
\caption{Variables espaciotemporales, cinemáticas y biomecánicas clave del test TUG instrumentado identificadas en la literatura científica}\label{tab:variables}\\
\toprule
\textbf{No.} & \textbf{Variable biomecánica / cinemática} & \textbf{Fase TUG} & \textbf{Expresión matemática / algoritmo inercial} & \textbf{Sensor requerido} & \textbf{Alteración en EP} & \textbf{Estudio de respaldo} \\
\midrule
\endfirsthead
\toprule
\textbf{No.} & \textbf{Variable biomecánica / cinemática} & \textbf{Fase TUG} & \textbf{Expresión matemática / algoritmo inercial} & \textbf{Sensor requerido} & \textbf{Alteración en EP} & \textbf{Estudio de respaldo} \\
\midrule
\endhead
\midrule
\multicolumn{7}{r}{\emph{Continúa en la página siguiente}} \\
\endfoot
\bottomrule
\endlastfoot
1 & \textbf{Duración del giro 180°} (\emph{Turn Duration}) & F3 & $\Delta t_{\text{turn}} = t_{\text{end}} - t_{\text{start}} \quad (\lvert \Delta \theta \rvert \ge \pi)$ & \texttt{BASE-SPINE} & Aumenta ($\uparrow$) & Zampieri et al. (2010); Molero-Mateo et al. (2026) \\
2 & \textbf{Velocidad pico de guiñada} (\emph{Peak Yaw Velocity}) & F3 & $\omega_{\text{peak}} = \max_{t \in \text{F3}} \lvert \omega_{\text{yaw}}(t) \rvert$ & \texttt{BASE-SPINE} & Disminuye ($\downarrow$) & Vervoort et al. (2016) \\
3 & \textbf{Pasos durante el giro} (\emph{Turn Step Count}) & F3 & $N_{\text{steps\_turn}} = \sum \mathbf{1}_{\{t_k \in [t_{\text{start}}, t_{\text{end}}]\}}$ & Tobillos L/R & Aumenta ($\uparrow$) & Molero-Mateo et al. (2026) \\
4 & \textbf{Velocidad de marcha} (\emph{Gait Speed}) & F2, F4 & $v_{\text{gait}} = d_{\text{path}} / \Delta t_{\text{marcha}} = 3.0\,\text{m} / \Delta t$ & L5 / Tobillos & Disminuye ($\downarrow$) & Caramia et al. (2018); van Kersbergen et al. (2021) \\
5 & \textbf{Longitud de paso estimada} (\emph{Step Length}) & F2, F4 & $L_{\text{step}} = 2\sqrt{2 \cdot l_{\text{leg}} \cdot h_{\text{CoM}} - h_{\text{CoM}}^2}$ & \texttt{BASE-SPINE} & Disminuye ($\downarrow$) & Welzel et al. (2021); Caramia et al. (2018) \\
6 & \textbf{Variabilidad del tiempo de paso} (\emph{Step Time CV}) & F2, F4 & $CV_{\text{step}} = (\sigma_{\Delta t} / \mu_{\Delta t}) \times 100\%$ & Tobillos L/R & Aumenta ($\uparrow$) & Molero-Mateo et al. (2026) \\
7 & \textbf{Regularidad de marcha} (\emph{Harmonic Regularity}) & F2, F4 & $R_{xx}[m_1] = \frac{1}{(N-m_1)\sigma_x^2}\sum x[n]x[n+m_1]$ & \texttt{BASE-SPINE} & Disminuye ($\downarrow$) & Ortega-Bastidas et al. (2023) \\
8 & \textbf{Duración transición a bípedo} (\emph{STS Duration}) & F1 & $\Delta t_{\text{STS}} = t_{\text{stand\_stable}} - t_{\text{flex\_start}}$ & \texttt{BASE-SPINE} & Aumenta ($\uparrow$) & Zampieri et al. (2010); Molero-Mateo et al. (2026) \\
9 & \textbf{Velocidad pico flexión de tronco} (\emph{Peak Flexion Velocity}) & F1 & $\omega_{\text{flex\_peak}} = \max_{t \in \text{F1}} \omega_{\text{pitch}}(t)$ & \texttt{BASE-SPINE} & Disminuye ($\downarrow$) & Zampieri et al. (2010) \\
10 & \textbf{Impacto vertical al sentarse} (\emph{Peak Deceleration}) & F5 & $a_{\text{impact}} = \max_{t \in \text{F5}} \lvert a_{\text{V}}(t) \rvert$ & \texttt{BASE-SPINE} & Aumenta ($\uparrow$) & Ortega-Bastidas et al. (2023) \\
11 & \textbf{Asimetría de balanceo de brazos} (\emph{Arm Swing Asymmetry}) & F2, F4 & $ASA = \frac{\lvert \theta_{\text{sw\_izq}} - \theta_{\text{sw\_der}} \rvert}{\max(\theta_{\text{sw\_izq}}, \theta_{\text{sw\_der}})} \times 100\%$ & Muñecas L/R & Aumenta ($\uparrow$) & van Kersbergen et al. (2021); Russo et al. (2025) \\
12 & \textbf{Índice de congelamiento} (\emph{FoG Index}) & F2, F3, F4 & $\text{FoG Index} = \frac{\int_{3}^{8} P_{xx}(f)df}{\int_{0.5}^{3} P_{xx}(f)df}$ & Tobillos / L5 & Aumenta ($\uparrow$) & Weiss et al. (2020); Russo et al. (2025) \\
13 & \textbf{Ancho de paso} (\emph{Step Width}) & F2, F4 & Descartada en IMU pura (requiere cámara) & Óptico RGB-D & Aumenta ($\uparrow$) & Russo et al. (2025) \\
14 & \textbf{Duración total del TUG} (\emph{Total TUG Time}) & Global & $T_{\text{total}} = t_{\text{sit\_end}} - t_{\text{STS\_start}}$ & L5 / Tobillos & Aumenta ($\uparrow$) & Podsiadlo \& Richardson (1991); Zampieri et al. (2010) \\
15 & \textbf{Rango de inclinación de tronco} (\emph{Trunk Pitch ROM}) & F1, F5 & $\text{ROM}_{\text{pitch}} = \max \theta_{\text{pitch}} - \min \theta_{\text{pitch}}$ & \texttt{BASE-SPINE} & Disminuye ($\downarrow$) & Molero-Mateo et al. (2026) \\
\end{longtable}
{\small\emph{Nota.} F1: levantarse; F2: marcha de ida; F3: giro de 180°; F4: marcha de regreso; F5: sentarse. Adaptado y sintetizado a partir de los estudios de Zampieri et al. (2010), Vervoort et al. (2016), Caramia et al. (2018), Molero-Mateo et al. (2026), Ortega-Bastidas et al. (2023), van Kersbergen et al. (2021) y Russo et al. (2025).}
\end{landscape}

%============================================================
% REFERENCIAS
%============================================================
\newpage
\seccionsinnumero{Referencias}

\begin{referencias}
\refitem{Caramia, C., Torricelli, D., Schmid, M., Muñoz-González, A., González-Vargas, J., Grandas, F., \& Pons, J. L. (2018). IMU-based classification of Parkinson's disease from gait: A sensitivity analysis on sensor location and feature selection. \emph{IEEE Journal of Biomedical and Health Informatics, 22}(6), 1765--1774. \url{<https://doi.org/10.1109/JBHI.2018.2865218}}>

\refitem{Choi, Y., Bae, Y., Cha, B., \& Ryu, J. (2022). Deep learning-based subtask segmentation of Timed Up-and-Go test using RGB-D cameras. \emph{Sensors, 22}(17), Article 6323. \url{<https://doi.org/10.3390/s22176323}}>

\refitem{Dubois, A., Bihl, T., \& Bresciani, J.-P. (2018). Automating the Timed Up and Go test using a depth camera. \emph{Sensors, 18}(1), Article 14. \url{<https://doi.org/10.3390/s18010014}}>

\refitem{Molero-Mateo, P., Trigo, C., Torres-Pardo, A., Fernández-Vázquez, D., Torricelli, D., Akgün, İ., Gómez-García, J. A., Algaba-Vidoy, M., Carratalá-Tejada, M., García-Diego-Martínez, S., Navarro-López, V., González-Zamorano, Y., Alguacil-Diego, I. M., \& Molina-Rueda, F. (2026). Instrumented Timed Up and Go analysis identifies biomechanical markers across early Hoehn and Yahr stages of Parkinson's disease. \emph{Sensors, 26}(16), Article 5177. \url{<https://doi.org/10.3390/s26165177}}>

\refitem{Mollinedo, I., \& Cancela, J. M. (2020). Evaluation of the psychometric properties and clinical applications of the Timed Up and Go test in Parkinson disease: A systematic review. \emph{Journal of Exercise Rehabilitation, 16}(4), 302--312. \url{<https://doi.org/10.12965/jer.2040532.266}}>

\refitem{Ortega-Bastidas, P., Gómez, B., Aqueveque, P., \& Leiva, S. (2023). Instrumented Timed Up and Go test (iTUG)---More than assessing time to predict falls: A systematic review. \emph{Sensors, 23}(7), Article 3426. \url{<https://doi.org/10.3390/s23073426}}>

\refitem{Patiño Zambrano, J., Mueses Zúñiga, D., \& Montezuma Sevillano, J. (s. f.). \emph{Timed Up and Go con unidades inerciales} [Proyecto de grado]. Universidad Icesi. Documento interno del macroproyecto.}

\refitem{Podsiadlo, D., \& Richardson, S. (1991). The Timed ``Up \& Go'': A test of basic functional mobility for frail elderly persons. \emph{Journal of the American Geriatrics Society, 39}(2), 142--148. \url{<https://doi.org/10.1111/j.1532-5415.1991.tb01616.x}}>

\refitem{Postuma, R. B., Berg, D., Stern, M., Poewe, W., Olanow, C. W., Oertel, W., Obeso, J., Marek, K., Litvan, I., Lang, A. E., Halliday, G., Goetz, C. G., Gasser, T., Dubois, B., Chan, P., Bloem, B. R., Adler, C. H., \& Deuschl, G. (2015). MDS clinical diagnostic criteria for Parkinson's disease. \emph{Movement Disorders, 30}(12), 1591--1601. \url{<https://doi.org/10.1002/mds.26424}}>

\refitem{Russo, M., Amboni, M., Pisani, N., Volzone, A., et al. (2025). Biomechanics parameters of gait analysis to characterize Parkinson's disease: A scoping review. \emph{Sensors, 25}(2), Article 338. \url{<https://doi.org/10.3390/s25020338}}>

\refitem{Tan, D., Pua, Y.-H., Balakrishnan, S., Scully, A., Bower, K. J., Prakash, K. M., Tan, E.-K., Chew, J.-S., Poh, E., Tan, S.-B., \& Clark, R. A. (2019). Automated analysis of gait and modified Timed Up and Go using the Microsoft Kinect in people with Parkinson's disease: Associations with physical outcome measures. \emph{Medical \& Biological Engineering \& Computing, 57}(2), 369--377. \url{<https://doi.org/10.1007/s11517-018-1868-2}}>

\refitem{van Kersbergen, J., Otte, K., de Vries, N. M., Bloem, B. R., Röhling, H. M., Mansow-Model, S., van der Kolk, N. M., Overeem, S., Zinger, S., \& van Gilst, M. M. (2021). Camera-based objective measures of Parkinson's disease gait features. \emph{BMC Research Notes, 14}, Article 329. \url{<https://doi.org/10.1186/s13104-021-05744-z}}>

\refitem{Vervoort, D., Vuillerme, N., Kosse, N., Hortobágyi, T., \& Lamoth, C. J. C. (2016). Multivariate analyses and classification of inertial sensor data to identify aging effects on the Timed-Up-and-Go test. \emph{PLOS ONE, 11}(6), Article e0155984. \url{<https://doi.org/10.1371/journal.pone.0155984}}>

% PENDIENTE: agregar aquí la referencia de Weiss et al. (2020), citada en la Tabla 1 (variable 12).
% Va en orden alfabético, entre Vervoort y Welzel (Weiss va después de Welzel: Wel < Wei? No: "Wei" < "Wel", por lo tanto Weiss va ANTES de Welzel).

\refitem{Welzel, J., Wendtland, D., Warmerdam, E., Romijnders, R., Elshehabi, M., Geritz, J., Berg, D., Hansen, C., \& Maetzler, W. (2021). Step length is a promising progression marker in Parkinson's disease. \emph{Sensors, 21}(7), Article 2292. \url{<https://doi.org/10.3390/s21072292}}>

\refitem{Zampieri, C., Salarian, A., Carlson-Kuhta, P., Aminian, K., Nutt, J. G., \& Horak, F. B. (2010). The instrumented Timed Up and Go test: Potential outcome measure for disease modifying therapies in Parkinson's disease. \emph{Journal of Neurology, Neurosurgery \& Psychiatry, 81}(2), 171--176. \url{<https://doi.org/10.1136/jnnp.2009.173740}}>
\end{referencias}

\end{document}
