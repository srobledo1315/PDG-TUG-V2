<div align="center">

# Análisis de Datos de la Prueba TUG para Variables Espaciotemporales en Pacientes con Enfermedad de Parkinson

<br><br>

**Juan José Arias Gallego, Esteban Guarin Valencia, Santiago Gómez Robledo y Heiner Danit Rincón Carrillo**

<br>

Ingeniería Telemática e Ingeniería de Sistemas, Universidad Icesi

Proyecto de Grado I

Tutores: Domiciano Rincón y Andrés Navarro

</div>

<div style="page-break-after: always;"></div>

# Lista de Acrónimos

**TUG** Prueba de levantarse,
caminar y sentarse (***T**imed **U**p and **G**o)*
**ITUG** Prueba de levantarse, caminar y sentarse instrumentada
(Instrumented ***T**ime d **U**p and **G**o)*
**IMU** Unidad de medición inercial (***I**nertial **M**easurement
**U**nit*)
**AUC** Área Bajo la Curva (*Area Under the Curve*)

**EP** Enfermedad de Parkinson

**FFT** Transformada Rápida de Fourier (*Fast Fourier Transform*)

**I2T** Grupo de Investigación en Informática y Telecomunicaciones

**L5** Quinta vértebra lumbar (ubicación anatómica del sensor inercial)

**MDS** Sociedad de Trastornos del Movimiento (*Movement Disorder
Society*)
**MDS-UPDRS** Escala Unificada de Evaluación de la Enfermedad de
Parkinson de la MDS (*MDS - Unified Parkinson\'s Disease Rating
Scale*)
**RGB-D** Cámara de Color y Profundidad (*Red, Green, Blue - Depth*)

# Glosario de Términos

**Fases de la prueba TUG**: Etapas que componen la ejecución de la
prueba: levantamiento, caminata, giro, regreso y sentada.

**Métrica biomecánica**: Parámetro cuantitativo utilizado para describir
el comportamiento del cuerpo humano durante el movimiento.

**Segmentación de señales**: Proceso de dividir una señal continua en
partes que representan distintas fases o eventos dentro de un
movimiento.

**Bradicinesia:** Lentitud del movimiento acompañada de una reducción
progresiva en su velocidad o amplitud durante tareas repetitivas; es el
síntoma motor principal de la enfermedad de Parkinson.

**Cadencia:** Número de pasos realizados por unidad de tiempo
(usualmente pasos por minuto) durante la marcha.

**Congelamiento de la marcha (*Freezing of Gait*):** Incapacidad breve
e involuntaria para iniciar o mantener la marcha, en la que los pies
parecen quedar temporalmente \"pegados al suelo\".

**Doble apoyo:** Intervalo dentro del ciclo de marcha en el que ambos
pies permanecen simultáneamente en contacto con la superficie.

**Energía espectral:** Distribución de la energía o potencia de una
señal a lo largo de las distintas frecuencias, obtenida mediante
transformaciones al dominio frecuencial (como FFT).

**Escala de Hoehn y Yahr:** Sistema de clasificación clínica utilizado
para categorizar el estadio de progresión y compromiso motor en la
enfermedad de Parkinson.

**Estimación de pose:** Técnica de visión por computador y aprendizaje
profundo utilizada para identificar y rastrear la posición
tridimensional de las articulaciones y segmentos corporales a partir de
datos ópticos o de profundidad.

**Fase de apoyo:** Intervalo del ciclo de marcha en el cual el pie se
encuentra en contacto directo con el suelo soportando el peso corporal.

**Fase de balanceo:** Intervalo del ciclo de marcha en el que el pie no
toca el suelo y el miembro avanza para preparar el siguiente paso.

**Fases de la prueba TUG:** Etapas funcionales que componen la ejecución
completa de la prueba: levantamiento, primera marcha, giro, segunda
marcha y sentada.

**Festinación:** Patrón de marcha anormal caracterizado por pasos
breves, rápidos y acelerados involuntariamente con tendencia a inclinar
el centro de gravedad hacia adelante.

**Filtro pasabajas Butterworth:** Algoritmo de filtrado digital empleado
en el preprocesamiento de señales inerciales para suavizar la señal y
atenuar el ruido de alta frecuencia preservando la forma de onda del
movimiento.

**Guiñada (*Yaw*):** Velocidad angular o rotación sobre el eje vertical
del cuerpo, clave para la detección y caracterización cinemática de los
giros.

**Inestabilidad postural:** Deficiencia en los reflejos de equilibrio
que dificulta el mantenimiento de una postura erguida estable e
incrementa el riesgo de caídas.

**Ingeniería de características:** Proceso de selección, extracción y
transformación de variables cuantitativas a partir de las señales para
alimentar los algoritmos de clasificación o análisis estadístico.

**Métrica biomecánica:** Parámetro cuantitativo (espacial, temporal,
cinemático o cinético) utilizado para describir el comportamiento del
cuerpo humano durante el movimiento.

**Pipeline de procesamiento:** Secuencia automatizada y estructurada de
etapas de software (filtrado, detección de picos, umbralización y
segmentación) para el tratamiento de señales inerciales o imágenes de
profundidad.

**Segmentación de señales:** Proceso de dividir una señal continua en
partes o intervalos discretos que representan distintas fases o eventos
dentro de un movimiento.

**Velocidad angular:** Tasa de variación de la orientación respecto al
tiempo, registrada principalmente por los giroscopios de los sensores
inerciales.

# Introducción

La enfermedad de Parkinson (EP) es un trastorno neurodegenerativo progresivo cuya expresión clínica incluye bradicinesia, rigidez, temblor en reposo y alteraciones del control postural. Estas manifestaciones afectan la movilidad funcional y pueden modificar la marcha, las transiciones posturales y la capacidad de girar de manera segura. Aunque la evaluación clínica continúa siendo indispensable, la cuantificación objetiva del movimiento puede complementar las escalas médicas al describir cambios sutiles y específicos de la ejecución motora (Postuma et al., 2015; Russo et al., 2025).

La prueba *Timed Up and Go* (TUG) es una herramienta funcional que consta de cinco fases: levantamiento, primera marcha, giro de 180°, segunda marcha de retorno y sentada. Su resultado clínico convencional es el tiempo total de ejecución. En personas con EP, la prueba TUG posee utilidad clínica y propiedades psicométricas aceptables; sin embargo, un único tiempo global no identifica qué componente funcional explica un desempeño alterado ni cuantifica de forma directa la calidad del movimiento (Mollinedo & Cancela, 2020).

La instrumentación de la prueba TUG permite extraer variables biomecánicas específicas por fase. Para este propósito, se utiliza la fusión de dos modalidades de captura: Unidades de Medición Inercial (IMU) y cámaras de profundidad RGB-D. El objetivo de las IMU (ubicadas en la región lumbar y tobillos) es capturar datos cinemáticos de alta resolución temporal, como la aceleración y la velocidad angular, mientras que la cámara RGB-D tiene como objetivo modelar de forma no invasiva las trayectorias espaciales corporales. La literatura demuestra que la combinación de estas tecnologías, especialmente durante los giros y transiciones posturales, contiene información crítica para la evaluación de alteraciones motoras (Vervoort et al., 2016; Zampieri et al., 2010).

La adquisición de datos para este proyecto se llevó a cabo durante brigadas médicas en la Clínica Valle del Lili. En estas jornadas, se capturaron muestras de aproximadamente 70 participantes (entre pacientes con Parkinson y sujetos de control). Es fundamental destacar que se empleó un esquema de fusión sensorial simultánea: a cada paciente se le equiparon los sensores IMU al mismo tiempo que era grabado por la cámara RGB-D. De esta manera, se obtuvo una misma muestra bimodal (inercial y óptica) unificada para cada ejecución de la prueba.

Este proyecto se fundamenta en dicha base de datos recolectada para segmentar las muestras, analizar la información conjunta procedente de las IMU y cámaras, e implementar algoritmos de clasificación de patrones motores que apoyen la caracterización objetiva de la enfermedad.

# Planteamiento del problema

En la práctica clínica, el tiempo total del TUG es una medida simple,
útil y de rápida aplicación; no obstante, resume en un solo valor
acciones motoras con demandas diferentes.

Dos personas pueden obtener tiempos semejantes y, aun así, presentar
alteraciones de distinta naturaleza: una puede requerir más tiempo para
levantarse, otra puede mostrar giros lentos y fragmentados y otra puede
caminar con menor longitud de paso o mayor variabilidad. Por tanto, el
tiempo global no es suficiente para describir la heterogeneidad
biomecánica del desempeño funcional en EP.

La evidencia muestra que el TUG instrumentado permite descomponer el
desempeño en subfases y extraer métricas más sensibles que el tiempo
total. Sin embargo, persisten desafíos relacionados con la
heterogeneidad de protocolos, la selección de características, la
comparación entre modalidades de censado y la validación de
clasificadores sobre bases de datos clínicas (Ortega-Bastidas et al.,
2023). En particular, la integración analítica de información IMU y
RGB-D para estudiar fases individuales del TUG representa una
oportunidad para generar indicadores cuantitativos de movilidad que
complementen la evaluación clínica.

En consecuencia, el problema central de ingeniería radica en la ausencia de un marco analítico y algorítmico que permita la extracción e identificación objetiva de patrones motores a partir de las subfases de la prueba TUG instrumentada. Esta carencia metodológica tiene como causa la complejidad de procesar datos crudos bimodales (IMU y RGB-D) frente a la insuficiencia clínica del tiempo global de la prueba convencional, lo cual genera como consecuencia una limitación para clasificar automáticamente a pacientes con enfermedad de Parkinson frente a sujetos de control, dificultando así el apoyo tecnológico para un diagnóstico objetivo.

# Objetivos

## Objetivo general

Desarrollar un algoritmo de clasificación para diferenciar pacientes con enfermedad de Parkinson y sujetos de control a partir de variables biomecánicas extraídas de cada fase de la prueba *Timed Up and Go* (TUG) mediante el análisis conjunto de señales inerciales (IMU) y cámaras de profundidad (RGB-D), integrándolo en la plataforma VIMOV como herramienta de apoyo al diagnóstico clínico objetivo.

## Objetivos específicos

- **OE1:** Realizar la exploración del conjunto de datos bimodal (señales inerciales IMU y video RGB-D) conformado por aproximadamente 70 muestras de diferentes participantes (pacientes con enfermedad de Parkinson y sujetos de control) adquiridas en brigadas durante la prueba *Timed Up and Go* (TUG), identificando patrones de movimiento y variables biomecánicas relevantes de acuerdo con la literatura científica.

- **OE2:** Validar el algoritmo de segmentación de fases del proyecto predecesor sobre el conjunto de datos adquirido en brigadas, ajustando el procesamiento a la última versión de los sistemas de adquisición de datos.

- **OE3:** Extraer las variables biomecánicas (espaciotemporales y cinemáticas) priorizadas durante la exploración de datos, desarrollando el algoritmo de clasificación para la diferenciación de patrones motores entre pacientes con enfermedad de Parkinson y sujetos de control.

- **OE4:** Integrar los algoritmos de segmentación y clasificación de la prueba TUG en la plataforma VIMOV, facilitando la ingesta, ejecución computacional y persistencia de las métricas obtenidas.

# Alcance

El alcance de este proyecto comprende el desarrollo y evaluación de un
algoritmo computacional capaz de clasificar patrones de movilidad entre
pacientes con enfermedad de Parkinson y sujetos de control, analizando
de forma independiente cada fase de la prueba *Timed Up and Go* (TUG).
Este proceso abarca el preprocesamiento del conjunto de datos
estructurado, la validación de la segmentación de fases, la ingeniería
de características biomecánicas y la validación del modelo de
clasificación.

El entregable principal es un algoritmo funcional e implementado dentro
del ecosistema tecnológico de los sistemas T-motion y VIMOV, el cual
permitirá, como mínimo, clasificar de manera automática a pacientes y
controles según los datos inerciales de cada fase de la prueba.

# Límites del proyecto

El producto de este proyecto funcionará exclusivamente como un
componente de apoyo tecnológico para la cuantificación objetiva de la
movilidad. El sistema desarrollado no pretende reemplazar el diagnóstico
médico neurológico, el criterio de los especialistas ni las escalas
clínicas establecidas (como la MDS-UPDRS). Los resultados arrojados por
el algoritmo de clasificación deben interpretarse como una herramienta
de asistencia sujeta a la validación e interpretación del personal de
salud.

# Antecedentes del proyecto

El grupo I2T mantiene colaboración con el servicio de neurología de la
Fundación Valle del Lili desde 2010 y ha desarrollado herramientas para
el análisis de marcha, movilidad y deterioro cognitivo. El macroproyecto
busca construir tecnologías de apoyo para el diagnóstico, seguimiento y
estudio de enfermedades neurodegenerativas y envejecimiento, articulando
personal clínico, investigadores y estudiantes de pregrado y posgrado.

El proyecto predecesor directo, "Timed Up and Go con unidades
inerciales", implementó una arquitectura para procesamiento asíncrono y
persistencia de señales, integrada a componentes como MinIO, PostgreSQL
y la plataforma Vimov. En la dimensión analítica, desarrolló un pipeline
para segmentar fases del TUG a partir de IMU ubicadas en L5 y ambos
tobillos. El procedimiento combinó filtrado pasabajas Butterworth,
detección de picos, umbrales sobre energía espectral y análisis FFT para
reconocer las transiciones entre levantarse, marcha de ida, giro, marcha
de regreso y sentarse.

La principal brecha que deja el proyecto predecesor es el uso
sistemático de las fases segmentadas para extraer características,
contrastarlas con información clínica y construir modelos de análisis o
clasificación. TUG 2 responde a esa brecha y añade el análisis de datos
provenientes de cámara RGB-D. Esta continuidad permite concentrar el
esfuerzo en la validación y la generación de evidencia sobre el
desempeño del sistema, en lugar de reiniciar la infraestructura de
adquisición y segmentación.

# Marco teórico

## Enfermedad de Parkinson (EP)

La EP es una enfermedad neurodegenerativa progresiva vinculada con
disfunción de circuitos dopaminérgicos de los ganglios basales. Los
criterios diagnósticos de la Movement Disorder Society establecen el
parkinsonismo como bradicinesia asociada con temblor en reposo o
rigidez; la evaluación clínica también considera criterios de exclusión,
señales de alerta y criterios de apoyo (Postuma et al., 2015).

La bradicinesia no equivale únicamente a menor velocidad: incluye
reducción progresiva de la amplitud o de la velocidad del movimiento y
puede expresarse como vacilaciones o interrupciones durante tareas
repetitivas. En la movilidad funcional, estas alteraciones se asocian
con menor automaticidad de la marcha, pasos más cortos, reducción de la
velocidad, mayor tiempo de doble apoyo, variabilidad entre pasos, menor
balanceo de brazos y dificultades en transiciones y giros (Russo et al.,
2025).

La marcha parkinsoniana es heterogénea. En estadios tempranos, algunas
alteraciones pueden ser discretas y confundirse con cambios asociados a
envejecimiento o con otras condiciones. En fases más avanzadas pueden
aparecer festinación, inestabilidad postural ley congelamiento de la
marcha, especialmente durante inicio de marcha, giros, pasos estrechos o
tareas que incrementan la demanda atencional. Por ello, medir múltiples
dimensiones del desempeño motor resulta más informativo que utilizar una
única variable temporal.

La escala de Hoehn y Yahr y la MDS-UPDRS son referentes clínicos
frecuentes para describir severidad y compromiso motor. Sin embargo, las
escalas no proporcionan una descripción detallada de cada componente
biomecánico. La medición instrumentada puede complementar estas
evaluaciones al generar indicadores cuantitativos, reproducibles y
potencialmente sensibles a cambios en movilidad.

## Análisis biomecánico motor

El análisis biomecánico motor estudia el movimiento humano a partir de
variables temporales, espaciales, cinemáticas y cinéticas. En análisis
de marcha, las variables espaciotemporales incluyen velocidad, cadencia,
longitud de paso, longitud de zancada, tiempo de paso y duración del
doble apoyo. Las variables cinemáticas describen posiciones,
trayectorias, ángulos, rangos de movimiento, aceleraciones y velocidades
angulares. Las

variables cinéticas se relacionan con fuerzas, momentos y potencias
articulares, y suelen requerir plataformas de fuerza o sistemas de
laboratorio especializados.

La marcha es un patrón cíclico compuesto por fase de apoyo y fase de
balanceo. La fase de apoyo corresponde al intervalo en que el pie
mantiene contacto con el suelo; la fase de balanceo ocurre cuando el
miembro avanza para preparar el siguiente contacto. Los periodos de
doble apoyo corresponden a los instantes en que ambos pies están en
contacto con el suelo y reflejan la transferencia del peso corporal.
Cambios en estas fases pueden indicar estrategias compensatorias,
inestabilidad o alteraciones del control motor.

En EP, la literatura describe disminución de velocidad, menor longitud
de paso y zancada, incremento del doble apoyo y modificaciones de la
coordinación Inter segmentaria. Además, se han reportado cambios en el
rango de movimiento de tobillo, rodilla, cadera, pelvis y tronco, así
como alteraciones de momentos y potencias articulares (Russo et al.,
2025). La identificación de tales características permite representar de
forma más completa la movilidad del participante.

Dentro del TUG, el análisis debe diferenciar al menos cuatro dominios
biomecánicos: transiciones posturales, marcha recta, giros y control de
la sentada. Las transiciones informan sobre producción de impulso y
control del tronco; la marcha permite estimar periodicidad, velocidad y
regularidad; los giros reflejan reorientación corporal y estabilidad
dinámica; y la sentada permite observar desaceleración y control
postural. Esta diferenciación es especialmente pertinente en EP, donde
los giros y las transiciones pueden deteriorarse de manera
desproporcionada frente al tiempo global.

## Prueba Timed Up and Go (TUG)

El TUG es una prueba de movilidad funcional en la que el resultado
tradicional es el tiempo requerido para completar una secuencia de
levantarse, caminar, girar y sentarse. Su utilidad práctica reside en
que reúne tareas funcionales cotidianas y puede implementarse con
recursos mínimos en un entorno clínico.

En EP, el TUG es pertinente porque demanda planificación motora,
equilibrio dinámico, coordinación, cambio de dirección y control de
transiciones. La revisión sistemática de Mollinedo y Cancela (2020)
encontró evidencia de confiabilidad de moderada a buena y validez
adecuada del TUG en personas con EP. No obstante, los autores
advirtieron heterogeneidad en protocolos y evidencia limitada sobre
sensibilidad al cambio. Estas observaciones no invalidan el TUG;
muestran que la interpretación del tiempo total debe complementarse con
medidas más granulares.

La introducción del TUG instrumentado se justifica porque transforma una
medida global en una evaluación por componentes. En vez de registrar
únicamente cuánto tarda una persona en realizar el ensayo, permite
examinar dónde se origina la dificultad funcional. Este enfoque

facilita la extracción de variables específicas por fase y ofrece una
base para analizar patrones de movilidad mediante métodos estadísticos y
de aprendizaje automático.

En este contexto, la instrumentación de la prueba (iTUG) incorpora sensores y algoritmos para
identificar automáticamente los eventos que componen la prueba. Una
segmentación útil comprende: levantarse de la silla, marcha de ida, giro
de 180°, marcha de regreso, giro o aproximación final y sentarse. El
número exacto de subfases puede variar según el protocolo, pero debe
mantenerse consistente dentro del conjunto de datos y documentarse de
manera explícita.

Cada subfase posee una firma cinemática distinta. El levantamiento se
asocia con cambios marcados de aceleración y rotación del tronco; la
marcha presenta patrones repetitivos relacionados con el ciclo de paso;
los giros generan picos o cambios de velocidad angular de guiñada; y la
sentada se caracteriza por desaceleración y control de flexión del
tronco. Estas firmas permiten detectar eventos, estimar duración de
fases y calcular variables específicas.

Vervoort et al. (2016) analizaron datos de una IMU lumbar durante TUG y
mostraron que un conjunto de características de marcha, giro y
transición postural permitió diferenciar grupos de edad con una AUC de
0.947. Aunque su población no fue exclusivamente parkinsoniana, el
estudio es relevante porque demuestra que las subfases del TUG contienen
información discriminativa y que el análisis multivariado de señales
inerciales puede superar la interpretación basada únicamente en segundos
totales.

En pacientes con EP, Zampieri et al. (2010) mostraron que el iTUG puede
aportar medidas de resultado útiles en enfermedad temprana,
especialmente al considerar componentes como giros y transiciones
posturales. Asimismo, la revisión de Ortega-Bastidas et al. (2023)
identificó que los sensores inerciales predominan en las aplicaciones de
iTUG y que la segmentación automática constituye un paso central para
estimar variables relevantes para movilidad y riesgo de caídas.

## Unidades de Medición Inercial (IMU)

Las unidades de medición inercial integran, como mínimo, acelerómetros y
giroscopios triaxiales. Los acelerómetros miden aceleración lineal,
mientras que los giroscopios registran velocidad angular. En el TUG, una
IMU ubicada en región lumbar puede capturar de manera eficiente
movimientos globales del tronco y cambios asociados con levantarse,
caminar, girar y sentarse. Sensores adicionales en tobillos o pies
permiten caracterizar de forma más detallada eventos del paso y
simetrías entre miembros.

Entre las ventajas de las IMU se encuentran su portabilidad, frecuencia
de muestreo, costo relativamente bajo y aplicabilidad en entornos
clínicos o domiciliarios. Sus limitaciones incluyen sensibilidad a la
posición y orientación del sensor, ruido, errores de fijación y deriva
cuando se integran señales. Por esta razón, los algoritmos deben incluir
procedimientos de preprocesamiento, control de calidad y segmentación
robusta.

## Cámaras de Profundidad RGB-D

Las cámaras RGB-D combinan imagen de color con información de
profundidad, lo que permite estimar la posición tridimensional
aproximada de segmentos y articulaciones corporales sin adherir sensores
al paciente. A partir de la estimación de pose pueden derivarse
trayectorias, desplazamiento corporal, duración de fases, velocidad de
marcha, oscilación del tronco, balanceo de brazos y variables espaciales
relacionadas con paso y giro.

La principal ventaja de RGB-D es su naturaleza no invasiva y su
capacidad de observar el cuerpo completo. Sin embargo, la precisión
puede verse afectada por oclusiones, distancia, posición relativa del
participante, iluminación, ropa, campo de visión y errores del algoritmo
de estimación esquelética. Por tanto, una alta repetibilidad de una
modalidad no implica que sus métricas sean intercambiables con las de
una IMU; cada sensor observa dimensiones diferentes del movimiento y
debe validarse según su propósito.

Estudios con Kinect han demostrado la viabilidad de automatizar el TUG y
caracterizar variables de marcha en población con EP. Tan et al. (2019)
analizaron marcha y TUG modificado con Kinect en personas con EP,
mientras que van Kersbergen et al. (2021) reportaron diferencias entre
pacientes y controles en variables como longitud de paso y velocidad de
marcha. Choi et al. (2022) mostró que las subtareas del TUG pueden
segmentarse mediante aprendizaje profundo a partir de cámaras RGB-D.
Estos trabajos sustentan el uso de cámaras de profundidad como
alternativa o complemento a la instrumentación inercial.

El estudio de Molero-Mateo et al. (2026) es especialmente relevante para
este proyecto porque examinó el TUG instrumentado en 79 participantes 38
con EP y 41 controles mediante IMU sincronizadas con fotogrametría
optoelectrónica. El trabajo identificó marcadores biomecánicos en
estadios tempranos de Hoehn y Yahr y muestra que el análisis por fases
puede contribuir a la discriminación de alteraciones motoras tempranas.
En consecuencia, TUG 2 debe priorizar la extracción de características
interpretables por fase, el contraste con etiquetas clínicas disponibles
y la evaluación cuidadosa de generalización.

# Estado del arte

El estado del arte se organiza por aporte metodológico y no como una
enumeración de artículos. Se seleccionaron trabajos que sustentan una
decisión concreta del proyecto: la pertinencia del TUG en EP, la
segmentación por fases, la selección de variables biomecánicas, el uso
de IMU, la captura RGB-D y la evaluación de clasificación. Se excluyen
referencias que no aportan directamente al problema de análisis
instrumentado del TUG.

## Del TUG convencional al TUG instrumentado

Mollinedo y Cancela (2020) revisaron las propiedades psicométricas y
aplicaciones clínicas del TUG en EP. Su principal aporte consiste en
confirmar su utilidad clínica, pero también señalar que la
heterogeneidad de protocolos y la limitada evidencia de respuesta al
cambio

restringen la interpretación de un único tiempo total. Esta conclusión
sustenta el uso de instrumentación y de variables por fase en lugar de
reemplazar la prueba convencional.

Ortega-Bastidas et al. (2023) realizaron una revisión sistemática sobre
iTUG y destacaron el predominio de sensores inerciales y de estrategias
de segmentación automática. Este trabajo es relevante como mapa
metodológico: ayuda a definir qué fases, sensores, variables y métodos
de detección son recurrentes, y advierte que la diversidad de
configuraciones dificulta comparaciones directas entre estudios.

## IMU: segmentación y características

Vervoort et al. (2016) analizaron datos inerciales durante TUG mediante
un enfoque multivariado. El estudio reportó que características de
giros, marcha y transiciones posturales permitieron discriminar efectos
relacionados con la edad con AUC de 0.947. Para TUG 2, este artículo
aporta un referente concreto de ingeniería de características y de
evaluación de modelos a partir de fases, no solo de tiempo total.

Zampieri et al. (2010) evaluaron el iTUG como posible medida de
resultado en EP y mostraron que las variables por componente pueden
identificar deterioro motor sutil. Su aporte justifica el análisis de
giros y transiciones posturales como dominios prioritarios de extracción
de características.

Caramia et al. (2018) estudiaron cómo la ubicación de IMU y la selección
de características influyen en la clasificación de EP a partir de
marcha. El valor de este trabajo radica en advertir que el rendimiento
de un clasificador depende de decisiones de adquisición y
preprocesamiento; por ello, TUG 2 debe documentar ubicación de sensores,
frecuencia de muestreo, selección de variables y partición de datos.

## RGB-D y análisis no invasivo

Dubois et al. (2018) demostraron la automatización del TUG mediante
cámara de profundidad. Su aporte es validar la posibilidad de medir de
manera objetiva la prueba sin sensores adheridos. Tan et al. (2019)
extendieron esta línea a personas con EP y relacionaron medidas
derivadas de Kinect con desenlaces físicos clínicos, reforzando el valor
de las medidas ópticas para caracterización funcional.

Van Kersbergen et al. (2021) evaluaron medidas objetivas de marcha
basadas en cámara en personas con EP y controles. El estudio aporta
evidencia de que variables ópticas como velocidad y longitud de paso
pueden reflejar diferencias relacionadas con la enfermedad. Choi et al.
(2022), por su parte, aplicó aprendizaje profundo para segmentar
subtareas del TUG con RGB-D, aportando una referencia directa para
futuros enfoques automáticos de segmentación visual.

## Severidad y biomarcadores

Welzel et al. (2021) reportaron que la longitud de paso es un posible
marcador de progresión en EP. Su aporte para el proyecto es clínico:
muestra que una característica espaciotemporal puede tener mayor valor
que medidas temporales aisladas para estudiar severidad. Esta variable
debe considerarse entre las características candidatas cuando la calidad
de datos RGB-D o IMU permita estimarla de manera confiable.

Molero-Mateo et al. (2026) analizaron marcadores biomecánicos del TUG en
estadios tempranos de Hoehn y Yahr mediante IMU y fotogrametría
optoelectrónica. Este artículo representa el antecedente más cercano a
TUG 2 por tres razones: estudia EP, segmenta tareas funcionales del TUG
y se interesa por la diferenciación de estadios tempranos. Su evidencia
respalda explorar, solo si la base de datos lo permite, modelos que
vayan más allá de paciente frente a control.

# Referencias

Caramia, C., Torricelli, D., Schmid, M., Muñoz-González, A.,
González-Vargas, J., Grandas, F., & Pons, J. L. (2018). IMU-based
classification of Parkinson's disease from gait: A sensitivity
analysis on sensor location and feature selection. IEEE Journal of
Biomedical and Health Informatics, 22(6), 1765--1774.
[[https://doi.org/10.1109/JBHI.2018.2865218]{.underline}](https://doi.org/10.1109/JBHI.2018.2865218)
C
hoi, Y., Bae, Y., Cha, B., & Ryu, J. (2022). Deep learning-based
subtask segmentation of Timed Up-and-Go test using RGB-D cameras.
Sensors, 22(17), Article 6323.
[[https://doi.org/10.3390/s22176323]{.underline}](https://doi.org/10.3390/s22176323)

Dubois, A., Bihl, T., & Bresciani, J.-P. (2018). Automating the Timed
Up and Go test using a depth camera. Sensors, 18(1), Article 14.
[[https://doi.org/10.3390/s18010014]{.underline}](https://doi.org/10.3390/s18010014)

Molero-Mateo, P., Trigo, C., Torres-Pardo, A., Fernández-Vázquez, D.,
Torricelli, D., Akgün, İ., Gómez-García, J. A., Algaba-Vidoy, M.,
Carratalá-Tejada, M., García-Diego-Martínez, S., Navarro-López, V.,
González-Zamorano, Y., Alguacil-Diego, I. M., & Molina-Rueda, F.
(2026). Instrumented Timed Up and Go analysis identifies biomechanical
markers across early Hoehn and Yahr stages of Parkinson's disease.
Sensors, 26(16), Article 5177.
[[https://doi.org/10.3390/s26165177]{.underline}](https://doi.org/10.3390/s26165177)

Mollinedo, I., & Cancela, J. M. (2020). Evaluation of the psychometric
properties and clinical applications of the Timed Up and Go test in
Parkinson disease: A systematic review. Journal of Exercise
Rehabilitation, 16(4), 302--312.
[[https://doi.org/10.12965/jer.2040532.266]{.underline}](https://doi.org/10.12965/jer.2040532.266)

Ortega-Bastidas, P., Gómez, B., Aqueveque, P., & Leiva, S. (2023).
Instrumented Timed Up and Go test (iTUG)---More than assessing time to
predict falls: A systematic review. Sensors, 23(7), Article 3426.
[[https://doi.org/10.3390/s23073426]{.underline}](https://doi.org/10.3390/s23073426)

Patiño Zambrano, J., Mueses Zúñiga, D., & Montezuma Sevillano, J. (s.
f.). Timed Up and Go con unidades inerciales \[Proyecto de grado\].
Universidad Icesi. Documento interno del macroproyecto.

Postuma, R. B., Berg, D., Stern, M., Poewe, W., Olanow, C. W., Oertel,
W., Obeso, J., Marek, K.,
Litvan, I., Lang, A. E., Halliday, G., Goetz, C. G., Gasser, T.,
Dubois, B., Chan, P., Bloem, B. R., Adler, C. H., & Deuschl, G.
(2015). MDS clinical diagnostic criteria for Parkinson's disease.
Movement Disorders, 30(12), 1591--1601.
[[https://doi.org/10.1002/mds.26424]{.underline}](https://doi.org/10.1002/mds.26424)

Russo, M., Amboni, M., Pisani, N., Volzone, A., et al. (2025).
Biomechanics parameters of gait analysis to characterize Parkinson's
disease: A scoping review. Sensors, 25(2), Article 338.
[[https://doi.org/10.3390/s25020338]{.underline}](https://doi.org/10.3390/s25020338)

Tan, D., Pua, Y.-H., Balakrishnan, S., Scully, A., Bower, K. J.,
Prakash, K. M., Tan, E.-K., Chew, J.-S., Poh, E., Tan, S.-B., & Clark,
R. A. (2019). Automated analysis of gait and modified Timed Up and Go
using the Microsoft Kinect in people with Parkinson's disease:
Associations with physical outcome measures. Medical & Biological
Engineering & Computing, 57(2), 369--377.
[[https://doi.org/10.1007/s11517-018-1868-2]{.underline}](https://doi.org/10.1007/s11517-018-1868-2)

van Kersbergen, J., Otte, K., de Vries, N. M., Bloem, B. R., Röhling,
H. M., Mansow-Model, S., van der Kolk, N. M., Overeem, S., Zinger, S.,
& van Gilst, M. M. (2021). Camera-based objective measures of
Parkinson's disease gait features. BMC Research Notes, 14, Article
329.
[[https://doi.org/10.1186/s13104-021-05744-z]{.underline}](https://doi.org/10.1186/s13104-021-05744-z)

Vervoort, D., Vuillerme, N., Kosse, N., Hortobágyi, T., & Lamoth, C.
J. C. (2016). Multivariate analyses and classification of inertial
sensor data to identify aging effects on the Timed-Up-and-Go test.
PLOS ONE, 11(6), Article e0155984.
[[https://doi.org/10.1371/journal.pone.0155984]{.underline}](https://doi.org/10.1371/journal.pone.0155984)

Welzel, J., Wendtland, D., Warmerdam, E., Romijnders, R., Elshehabi,
M., Geritz, J., Berg, D., Hansen, C., & Maetzler, W. (2021). Step
length is a promising progression marker in Parkinson's disease.
Sensors, 21(7), Article 2292.
[[https://doi.org/10.3390/s21072292]{.underline}](https://doi.org/10.3390/s21072292)

Zampieri, C., Salarian, A., Carlson-Kuhta, P., Aminian, K., Nutt, J.
G., & Horak, F. B. (2010). The instrumented Timed Up and Go test:
Potential outcome measure for disease modifying therapies in
Parkinson's disease. Journal of Neurology, Neurosurgery & Psychiatry,
81(2), 171--176.
s[[https://doi.org/10.1136/jnnp.2009.173740]{.underline}](https://doi.org/10.1136/jnnp.2009.173740)
