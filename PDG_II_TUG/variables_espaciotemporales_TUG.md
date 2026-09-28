# Banco de Variables Espaciotemporales, Cinemáticas y Biomecánicas del TUG

## 1. Resumen de Fuentes Analizadas

Los siguientes artículos, presentes en el directorio local, fundamentan la extracción clínica y computacional.

**Fuentes Base Originales:**

* **Zampieri et al., 2010:** *The instrumented Timed Up and Go test: Potential outcome measure for disease modifying therapies in Parkinson's disease.*
* **Vervoort et al., 2016:** *Multivariate Analyses and Classification of Inertial Sensor Data to Identify Aging Effects on the Timed-Up-and-Go Test.*
* **Caramia et al., 2018:** *IMU-based classification of Parkinson's disease from gait: A sensitivity analysis on sensor location and feature selection.*
* **Molero-Mateo et al., 2026:** *Instrumented Timed Up and Go analysis identifies biomechanical markers across early Hoehn and Yahr stages of Parkinson's disease.*
* **Welzel et al., 2021:** *Step length is a promising progression marker in Parkinson's disease.*
* **Ortega-Bastidas et al., 2023:** *Instrumented Timed Up and Go test (iTUG)—More than assessing time to predict falls: A systematic review.*
* **Choi et al., 2022:** *Deep learning-based subtask segmentation of Timed Up-and-Go test using RGB-D cameras.*
* **van Kersbergen et al., 2021:** *Camera-based objective measures of Parkinson's disease gait features.*
* **Mollinedo & Cancela, 2020:** *Evaluation of the psychometric properties and clinical applications of the Timed Up and Go test in Parkinson disease.*
* **Dubois et al., 2018:** *Automating the Timed Up and Go test using a depth camera.*
* **Postuma et al., 2015:** *MDS clinical diagnostic criteria for Parkinson's disease.*
* **Russo et al., 2025:** *Biomechanics parameters of gait analysis to characterize Parkinson's disease.*
* **Patiño Zambrano et al., s.f.:** *Timed Up and Go con unidades inerciales.*
* **Smartphone Segmentation:** *AI-Driven Adaptive Segmentation of Timed Up and Go Test Phases Using a Smartphone.*
* **Wearable State of the Art:** *Application of Wearable Sensors in Parkinson's Disease State of the Art.*
* **Dual-Task TUG:** *Better than counting seconds Identifying fallers among healthy elderly using fusion of accelerometer features and dual-task Timed Up and Go.*
* **ML Protocols:** *Comparison of Walking Protocols and Gait Assessment Systems for Machine Learning-Based Classification of Parkinson's Disease.*
* **Depth Cameras Validation:** *Experimental Validation of Depth Cameras for the Parameterization of Functional Balance of Patients in Clinical Tests.*
* **Gait Patterns & Balance:** *Gait Patterns and Balance Impairment in Parkinson's Disease With Correlation to Disease Severity.*
* **iTUG Systematic Review:** *Instrumented Timed Up and Go (iTUG) A Systematic Review of Parameters Across Healthy, Older, and Neurological Populations.*
* **NPH vs PD Differentiation:** *Machine learning differentiation of Parkinson's disease and normal pressure hydrocephalus using wearable sensors capturing gait impairments.*
* **Disease Severity:** *Quantifying Parkinson's disease severity.*

---

## 2. Fichas Técnicas Detalladas

### Grupo A: Las 15 Variables de Oro (Prioridad de Extracción)
Estas son las métricas más importantes y deben priorizarse en el desarrollo por su alta interpretabilidad clínica.

### Variable #1: Duración del Giro 180° (Turn Duration)

* **Fase del TUG:** Fase 3.
* **Definición técnica y conceptual:** Tiempo desde que el paciente inicia la rotación axial hasta que recupera marcha recta en sentido contrario. Unidad: $s$.
* **Enfoque como descriptor discriminatorio:** Clínicamente el biomarcador más sensible en el TUG. Profundamente alterado en EP (bradicinesia y giros "en bloque").
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - FUSIÓN IMU + RGB-D]
  * **Explicación técnica:** Segmentable por umbralización de la velocidad angular de Yaw de la IMU o por cambio de ángulo pélvico en cámara.
* **Paper / Fuente de respaldo:** Zampieri et al. (2010); Molero-Mateo et al. (2026).

### Variable #2: Velocidad Angular Pico de Guiñada (Turn Peak Yaw Velocity)

* **Fase del TUG:** Fase 3.
* **Definición técnica y conceptual:** Máxima velocidad angular axial durante el giro intermedio. Unidad: $°/s$.
* **Enfoque como descriptor discriminatorio:** Acentuadamente menor en Parkinson. Giros lentos y fragmentados.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Directamente del pico máximo de la señal del giroscopio (Yaw) durante la Fase 3.
* **Paper / Fuente de respaldo:** Vervoort et al. (2016).

### Variable #3: Número de Pasos durante el Giro (Turn Step Count)

* **Fase del TUG:** Fase 3.
* **Definición técnica y conceptual:** Cantidad de pisadas requeridas para completar el giro de 180°. Unidad: $unidades$.
* **Enfoque como descriptor discriminatorio:** Aumenta dramáticamente en EP (giros multicomponente o "en bloque") frente a sanos (generalmente de 1 a 3 pasos). Marcador predictor de caídas.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - FUSIÓN IMU + RGB-D]
  * **Explicación técnica:** Picos AP o verticales filtrados dentro de la ventana del giro.
* **Paper / Fuente de respaldo:** Molero-Mateo et al. (2026).

### Variable #4: Velocidad de Marcha (Gait Speed)

* **Fase del TUG:** Fase 2 y Fase 4 (Marcha).
* **Definición técnica y conceptual:** Distancia recorrida dividida por el tiempo de la fase de marcha. Unidad: $m/s$.
* **Enfoque como descriptor discriminatorio:** Altamente reducida en EP. Es el biomarcador global más robusto de deterioro motor progresivo (bradicinesia).
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - FUSIÓN IMU + RGB-D]
  * **Explicación técnica:** La cámara RGB-D lo extrae muy fácilmente (distancia de la pelvis en el eje $Z$ de la cámara / tiempo). Con IMU en L5 requiere integrar aceleración o modelar marcha paramétricamente (menor precisión).
* **Paper / Fuente de respaldo:** Caramia et al. (2018); van Kersbergen et al. (2021).

### Variable #5: Longitud de Paso (Step Length)

* **Fase del TUG:** Fase 2 y Fase 4 (Marcha).
* **Definición técnica y conceptual:** Distancia espacial anteroposterior entre los apoyos sucesivos del pie derecho y el izquierdo. Unidad: $m$.
* **Enfoque como descriptor discriminatorio:** Muy reducida en EP (pasos cortos, marcha arrastrada). Welzel et al. indican que es un marcador primario de progresión.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - RGB-D] (Viable con IMU solo si hay IMU en pies/tobillos).
  * **Explicación técnica:** Cámara: distancia euclidiana 3D entre los joints de los tobillos en los instantes de Heel Strike. Si el hardware IMU solo está en L5, estimar longitud de paso espacial es geométricamente indirecto y propenso a error (requeriría [NO VIABLE - IMU L5 SOLA]).
* **Paper / Fuente de respaldo:** Welzel et al. (2021); Caramia et al. (2018).

### Variable #6: Variabilidad del Tiempo de Paso (Step Time Variability)

* **Fase del TUG:** Fase 2 y 4.
* **Definición técnica y conceptual:** Desviación estándar o coeficiente de variación (CV) de los tiempos de paso. Unidad: $\%$.
* **Enfoque como descriptor discriminatorio:** Altamente aumentada en EP, indicativo claro de inestabilidad dinámica y pérdida de automaticidad.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Extracción de todos los intervalos pico a pico y cálculo estadístico.
* **Paper / Fuente de respaldo:** Molero-Mateo et al. (2026).

### Variable #7: Armónico de Marcha / Regularidad (Harmonic Ratio / Stride Regularity)

* **Fase del TUG:** Fase 2 y 4.
* **Definición técnica y conceptual:** Medida de la suavidad del paso evaluada mediante análisis espectral o autocorrelación (ACF) en el eje Vertical y AP de la IMU.
* **Enfoque como descriptor discriminatorio:** Mucho menor en EP por marcha arrastrada, asimetría y episodios de FoG.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Aplicación de ACF sobre las ventanas temporales segmentadas en Fase 2 y 4 del acelerómetro L5.
* **Paper / Fuente de respaldo:** Ortega-Bastidas et al. (2023).

### Variable #8: Duración de la Transición a Bípedo (Sit-to-Stand Duration)

* **Fase del TUG:** Fase 1.
* **Definición técnica y conceptual:** Tiempo que transcurre desde el inicio del movimiento del tronco hacia adelante hasta alcanzar la bipedestación estable completa. Unidad: $s$.
* **Enfoque como descriptor discriminatorio (Parkinson vs. Control):** Aumenta en pacientes con EP. Se asocia con bradicinesia y debilidad en extensores de cadera, requiriendo más tiempo para vencer la inercia. (Altamente discriminatorio).
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - FUSIÓN IMU + RGB-D]
  * **Explicación técnica:** Extraíble con IMU lumbar (detección de pico en aceleración vertical y rotación pitch) y con cámara RGB-D midiendo desplazamiento vertical del centroide / hombros.
* **Paper / Fuente de respaldo:** Zampieri et al. (2010); Molero-Mateo et al. (2026).

### Variable #9: Velocidad Angular Pico de Flexión (Peak Trunk Flexion Velocity)

* **Fase del TUG:** Fase 1 (Sit-to-Stand).
* **Definición técnica y conceptual:** Máxima velocidad angular del tronco en el plano sagital (pitch) al inclinarse hacia adelante para ganar momento. Unidad: $rad/s$ o $°/s$.
* **Enfoque como descriptor discriminatorio:** Disminuye significativamente en EP (rigidez axial y bradicinesia). El paciente falla en generar suficiente inercia, compensando con múltiples intentos.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Integración directa y extracción de picos en el eje medio-lateral del giroscopio (eje de pitch) lumbar. Con RGB-D es más ruidoso calcular derivadas segundas/primeras precisas de ángulos.
* **Paper / Fuente de respaldo:** Zampieri et al. (2010).

### Variable #10: Impacto Vertical al Sentarse (Peak Vertical Deceleration)

* **Fase del TUG:** Fase 5.
* **Definición técnica y conceptual:** Aceleración máxima al chocar contra la silla. Unidad: $m/s^2$.
* **Enfoque como descriptor discriminatorio:** Mayor en pacientes con control motor deficiente ("plopping" o caída descontrolada).
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Detección de máximo en acelerómetro eje Z (Vertical) en fase final.
* **Paper / Fuente de respaldo:** Ortega-Bastidas et al. (2023).

### Variable #11: Amplitud de Balanceo de Brazos (Arm Swing Amplitude)

* **Fase del TUG:** Fase 2 y 4.
* **Definición técnica y conceptual:** Oscilación anteroposterior de las extremidades superiores.
* **Enfoque como descriptor discriminatorio:** La reducción asimétrica es uno de los síntomas más tempranos en EP.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - RGB-D] (Descartada para IMU L5, requeriría IMUs en muñecas).
  * **Explicación técnica:** Seguimiento esquelético de muñecas (distancia relativa a cadera).
* **Paper / Fuente de respaldo:** van Kersbergen et al. (2021).

### Variable #12: Índice de Congelamiento de la Marcha (FoG Index)

* **Fase del TUG:** Fase 2, 3 y 4.
* **Definición técnica y conceptual:** Ratio de la potencia espectral en la banda de alta frecuencia (3-8 Hz, temblor/congelamiento) sobre la banda de baja frecuencia (0.5-3 Hz, marcha normal). Unidad: Adimensional.
* **Enfoque como descriptor discriminatorio:** Aumenta drásticamente antes y durante un episodio de FoG. Marcador crítico.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Análisis FFT sobre ventanas deslizantes de la aceleración anteroposterior o vertical.
* **Paper / Fuente de respaldo:** *Application of Wearable Sensors in Parkinson's Disease State of the Art*.

### Variable #13: Ancho de Paso / Base de Sustentación (Step Width)

* **Fase del TUG:** Fase 2 y 4.
* **Definición técnica y conceptual:** Distancia transversal (medio-lateral) entre ambos pies durante la marcha. Unidad: $m$.
* **Enfoque como descriptor discriminatorio:** Frecuentemente aumentado en EP como compensación a la inestabilidad postural, o muy ancho en Hidrocefalia de Presión Normal.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - RGB-D]
  * **Explicación técnica:** Distancia euclidiana $X$ (lateral) entre las coordenadas 3D de los tobillos.
* **Paper / Fuente de respaldo:** *Gait Patterns and Balance Impairment in Parkinson's Disease*.

### Variable #14: Duración Total del TUG (Total TUG Time)

* **Fase del TUG:** Global.
* **Definición técnica y conceptual:** Tiempo desde indicación hasta retorno a estado estático basal. Unidad: $s$.
* **Enfoque como descriptor discriminatorio:** Biomarcador clínico clásico (>14s riesgo de caída). Aumenta severamente en EP.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - FUSIÓN]
  * **Explicación técnica:** Distancia temporal entre inicio Fase 1 y fin Fase 5.
* **Paper / Fuente de respaldo:** Podsiadlo & Richardson (TUG clásico) y Zampieri (2010).

### Variable #15: Rango de Movimiento del Tronco (Trunk Pitch ROM)

* **Fase del TUG:** Fase 1 y Fase 5.
* **Definición técnica y conceptual:** Diferencia entre el ángulo máximo y mínimo de flexión del tronco durante la transición. Unidad: $grados (°)$.
* **Enfoque como descriptor discriminatorio:** Disminuye en EP. Los pacientes presentan un patrón "en bloque" y menor capacidad de inclinar el tronco para transferir el centro de presión.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Integración de la velocidad angular (giroscopio) apoyada con filtro complementario de acelerómetro (para evitar deriva).
* **Paper / Fuente de respaldo:** Molero-Mateo et al. (2026).

---

### Grupo B: También identificamos estas otras variables
Las siguientes son métricas secundarias o complementarias.

### Variable #16: Aceleración Vertical Pico (STS Peak Vertical Acceleration)

* **Fase del TUG:** Fase 1 (Sit-to-Stand).
* **Definición técnica y conceptual:** Máxima aceleración en el eje vertical (Z) generada por las piernas para levantar el centro de masa. Unidad: $m/s^2$.
* **Enfoque como descriptor discriminatorio:** Atenuada en EP. Refleja pérdida de potencia muscular explosiva y bradicinesia axial.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Análisis del acelerómetro eje vertical post-rotación (corrigiendo la gravedad).
* **Paper / Fuente de respaldo:** Vervoort et al. (2016).

### Variable #17: Longitud de Zancada (Stride Length)

* **Fase del TUG:** Fase 2 y Fase 4 (Marcha).
* **Definición técnica y conceptual:** Distancia entre dos apoyos consecutivos del mismo pie. Unidad: $m$.
* **Enfoque como descriptor discriminatorio:** Análogo a la longitud de paso; decrece progresivamente con el Hoehn y Yahr.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - RGB-D]
  * **Explicación técnica:** Similar a la longitud de paso; se obtiene de las trazas del esqueleto 3D (tobillo).
* **Paper / Fuente de respaldo:** Molero-Mateo et al. (2026).

### Variable #18: Cadencia de Marcha (Cadence)

* **Fase del TUG:** Fase 2 y Fase 4 (Marcha).
* **Definición técnica y conceptual:** Tasa de paso. Número de pasos por unidad de tiempo. Unidad: $pasos/minuto$.
* **Enfoque como descriptor discriminatorio:** Incrementa en algunos casos de festinación (intentando compensar la baja longitud de zancada) o disminuye por bradicinesia. Dispersión muy alta en EP.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - FUSIÓN IMU + RGB-D]
  * **Explicación técnica:** IMU en L5 detecta fácilmente los Heel Strikes (picos de aceleración vertical o AP). RGB-D detecta cruces de velocidad de piernas.
* **Paper / Fuente de respaldo:** Caramia et al. (2018).

### Variable #19: Tiempo de Paso (Step Time)

* **Fase del TUG:** Fase 2 y 4.
* **Definición técnica y conceptual:** Duración temporal de un solo paso. Unidad: $s$.
* **Enfoque como descriptor discriminatorio:** Aumentado y muy variable en Parkinson.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Distancia temporal entre picos sucesivos de impacto en la aceleración IMU.
* **Paper / Fuente de respaldo:** Zampieri et al. (2010).

### Variable #20: Tiempo de Fase de Apoyo (Stance Phase Duration)

* **Fase del TUG:** Fase 2 y 4.
* **Definición técnica y conceptual:** Porcentaje del ciclo de marcha en el que el pie está en contacto con el suelo. Unidad: $\%$.
* **Enfoque como descriptor discriminatorio:** Aumenta en EP como mecanismo de adaptación para mantener estabilidad.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [DESCARTADA (Si solo hay IMU lumbar)] / [VIABLE - RGB-D o IMU TOBILLO].
  * **Explicación técnica:** Difícil de discernir precisamente Toe Off desde L5 IMU. Con RGB-D se puede estimar velocidad 0 del pie.
* **Paper / Fuente de respaldo:** Caramia et al. (2018).

### Variable #21: Tiempo de Doble Apoyo (Double Support Time)

* **Fase del TUG:** Fase 2 y 4.
* **Definición técnica y conceptual:** Tiempo donde ambos pies tocan el suelo simultáneamente. Unidad: $s$ o $\%$.
* **Enfoque como descriptor discriminatorio:** Sensiblemente mayor en EP para compensar inestabilidad postural y miedo a caer.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - RGB-D]
  * **Explicación técnica:** Distancia temporal entre Heel Strike de un pie y Toe-Off del contralateral. Mejor con cámara por cinemática de pies.
* **Paper / Fuente de respaldo:** van Kersbergen et al. (2021).

### Variable #22: Simetría Espacial del Paso (Step Spatial Symmetry)

* **Fase del TUG:** Fase 2 y 4.
* **Definición técnica y conceptual:** Ratio entre longitud de paso derecho vs izquierdo.
* **Enfoque como descriptor discriminatorio:** Asimetría predominante en EP (por inicio unilateral patológico común en ganglios basales).
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - RGB-D]
  * **Explicación técnica:** Ratio de distancias extraídas por visión artificial de ambos hemicuerpos.
* **Paper / Fuente de respaldo:** Caramia et al. (2018).

### Variable #23: Desplazamiento Medio-Lateral del Tronco (Mediolateral Sway)

* **Fase del TUG:** Fase 2 y 4.
* **Definición técnica y conceptual:** Amplitud de oscilación del centro de masa en el plano frontal. Unidad: $m$ o $m/s^2$ (RMS).
* **Enfoque como descriptor discriminatorio:** Incrementado por inestabilidad de control de equilibrio lateral en EP.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** RMS de la aceleración filtrada en el eje medio-lateral.
* **Paper / Fuente de respaldo:** Vervoort et al. (2016).

### Variable #24: Velocidad Angular Media de Giro (Mean Turn Angular Velocity)

* **Fase del TUG:** Fase 3.
* **Definición técnica y conceptual:** Promedio de la tasa de giro (Total angle / Time). Unidad: $°/s$.
* **Enfoque como descriptor discriminatorio:** Disminuye progresivamente a mayor avance de la EP.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Integral de la señal de guiñada dividida sobre la duración.
* **Paper / Fuente de respaldo:** Zampieri et al. (2010).

### Variable #25: Turn Jerk (Suavidad del giro)

* **Fase del TUG:** Fase 3.
* **Definición técnica y conceptual:** Derivada de la aceleración angular, mide las detenciones o vacilaciones.
* **Enfoque como descriptor discriminatorio:** Mucho mayor en EP, indicativo de un giro fragmentado y poco fluido.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Derivada temporal de los datos crudos del giroscopio (Pitch/Yaw/Roll).
* **Paper / Fuente de respaldo:** Ortega-Bastidas et al. (2023).

### Variable #26: Duración de Transición a Sentado (Stand-to-Sit Duration)

* **Fase del TUG:** Fase 5.
* **Definición técnica y conceptual:** Tiempo para sentarse, controlando excéntricamente el descenso. Unidad: $s$.
* **Enfoque como descriptor discriminatorio:** Mayor en EP debido a debilidad e inestabilidad; los pacientes se dejan caer (menor control).
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - FUSIÓN IMU + RGB-D]
  * **Explicación técnica:** Similar a Fase 1 pero con polaridades invertidas en rotación.
* **Paper / Fuente de respaldo:** Zampieri et al. (2010).

### Variable #27: Flexión Pico del Tronco al Sentarse (Peak Trunk Flexion Stand-to-Sit)

* **Fase del TUG:** Fase 5.
* **Definición técnica y conceptual:** Extensión y velocidad máxima hacia adelante previo al descenso.
* **Enfoque como descriptor discriminatorio:** Reducida, limitando la estrategia de control excéntrico de cuádriceps.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Integración sobre giroscopio Pitch en ventana 5.
* **Paper / Fuente de respaldo:** Molero-Mateo et al. (2026).

### Variable #28: Duración del Giro Final (Pre-Sit Turn Duration)

* **Fase del TUG:** Fase 5.
* **Definición técnica y conceptual:** Tiempo empleado en rotar para alinear la espalda a la silla. Unidad: $s$.
* **Enfoque como descriptor discriminatorio:** Zona de alta probabilidad de Congelamiento de Marcha (FoG).
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Detección de Yaw justo antes del impacto de sentada.
* **Paper / Fuente de respaldo:** Vervoort et al. (2016).

### Variable #29: Número Total de Pasos (Total Step Count)

* **Fase del TUG:** Global.
* **Definición técnica y conceptual:** Conteo acumulado en Fases 2, 3, 4 y 5.
* **Enfoque como descriptor discriminatorio:** Mayor en EP (pasos cortos, marcha festinante).
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Detección adaptativa de picos globales.
* **Paper / Fuente de respaldo:** Molero-Mateo et al. (2026).

### Variable #30: Aceleración Cuadrática Media (RMS Acceleration Global)

* **Fase del TUG:** Global.
* **Definición técnica y conceptual:** Energía general del movimiento.
* **Enfoque como descriptor discriminatorio:** Disminuida por bradicinesia.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** RMS de la norma euclidiana del acelerómetro 3D.
* **Paper / Fuente de respaldo:** Ortega-Bastidas et al. (2023).

### Variable #31: Variabilidad de la Velocidad de Giro (Turn Velocity Variability)

* **Fase del TUG:** Fase 3.
* **Definición técnica y conceptual:** Desviación estándar de la velocidad angular de guiñada durante el giro.
* **Enfoque como descriptor discriminatorio:** Mayor en EP debido a giros "a trompicones" y falta de fluidez.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Varianza estadística sobre la señal Yaw segmentada.
* **Paper / Fuente de respaldo:** *Instrumented Timed Up and Go (iTUG) A Systematic Review of Parameters*.

### Variable #32: Costo de Tarea Dual (Dual-Task Cost - DTC)

* **Fase del TUG:** Global / Fase 2.
* **Definición técnica y conceptual:** Diferencia porcentual del rendimiento (ej. Velocidad) entre el TUG simple y un TUG cognitivo (Dual-task). Unidad: $\%$.
* **Enfoque como descriptor discriminatorio:** Decremento desproporcionado en EP.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - FUSIÓN]
  * **Explicación técnica:** Algoritmo delta entre dos pruebas del mismo paciente.
* **Paper / Fuente de respaldo:** *Better than counting seconds Identifying fallers...*

### Variable #33: Área de Balanceo del Centro de Masa (CoM Sway Area)

* **Fase del TUG:** Fase 1 y 5 (Transiciones).
* **Definición técnica y conceptual:** Área abarcada por las oscilaciones transversales y AP del centro de masa al incorporarse. Unidad: $cm^2$.
* **Enfoque como descriptor discriminatorio:** Aumenta severamente en riesgo de caída (inestabilidad).
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - RGB-D]
  * **Explicación técnica:** Convex Hull o elipse de confianza de la trayectoria 2D del CoM (Pelvis).
* **Paper / Fuente de respaldo:** *Experimental Validation of Depth Cameras...*

### Variable #34: Índice de Suavidad de la Transición (Transition SPARC)

* **Fase del TUG:** Fase 1 y 5.
* **Definición técnica y conceptual:** Medida Spectral Arc Length (SPARC) de la curva de velocidad angular.
* **Enfoque como descriptor discriminatorio:** Decremento en EP por movimiento espasmódico.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Transformación espectral de la señal de giroscopio en el instante de levantamiento.
* **Paper / Fuente de respaldo:** *Instrumented Timed Up and Go analysis identifies biomechanical markers...*

### Variable #35: Simetría Espacial de Giro (Turn Spatial Symmetry)

* **Fase del TUG:** Fase 3.
* **Definición técnica y conceptual:** Diferencia de amplitud de paso entre el pie pivotante y el pie externo durante la rotación.
* **Enfoque como descriptor discriminatorio:** Altamente asimétrico en síndromes parkinsonianos tempranos unilaterales.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - RGB-D]
  * **Explicación técnica:** Rastreo de coordenadas 3D de tobillos durante la ventana del giro.
* **Paper / Fuente de respaldo:** *Gait Patterns and Balance Impairment...*

### Variable #36: Aceleración Máxima de Impacto del Talón (Heel Strike Peak Accel)

* **Fase del TUG:** Fase 2 y 4.
* **Definición técnica y conceptual:** Pico de fuerza vertical/AP estimado en la L5 durante cada contacto inicial del pie. Unidad: $m/s^2$.
* **Enfoque como descriptor discriminatorio:** Reducido en EP por marcha arrastrada y falta de impacto (marcha festinante).
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - IMU]
  * **Explicación técnica:** Filtrado pasabajas adaptativo y detección de picos en Z.
* **Paper / Fuente de respaldo:** *Machine learning differentiation of Parkinson's disease...*

### Variable #37: Variabilidad del Tiempo de Balanceo (Swing Time Variability)

* **Fase del TUG:** Fase 2 y 4.
* **Definición técnica y conceptual:** Fluctuación porcentual (CV) del tiempo que el pie pasa en el aire.
* **Enfoque como descriptor discriminatorio:** Marcador crítico de déficit atencional en la marcha en EP.
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - RGB-D]
  * **Explicación técnica:** Cálculo estadístico derivado de los tiempos medidos visualmente entre *Toe Off* y *Heel Strike*.
* **Paper / Fuente de respaldo:** *Comparison of Walking Protocols...*

### Variable #38: Duración Pospuesta del Paso (Delayed Step Initiation)

* **Fase del TUG:** Transición 1 a 2.
* **Definición técnica y conceptual:** Tiempo de inmovilidad desde la bipedestación completa hasta que el primer pie despega del suelo. Unidad: $s$.
* **Enfoque como descriptor discriminatorio:** Elevado por Acinesia de Inicio (*Start Hesitation*).
* **Fuente sensorial y viabilidad técnica (Peluqueo):**
  * **Estado:** [VIABLE - FUSIÓN]
  * **Explicación técnica:** Cruce temporal entre el fin de la Fase 1 (estable) y el primer pico de aceleración de marcha.
* **Paper / Fuente de respaldo:** *Application of Wearable Sensors in Parkinson's Disease*.


---

## 3. Matriz de Priorización y Depuración (Peluqueo) Actualizada

### Grupo A: Top 15 Variables de Oro
| # | Nombre de la Variable | Fase TUG | Fuente Sensorial | Comportamiento EP | Viabilidad |
|---|---|---|---|---|---|
| 1 | Duración del Giro 180° (Turn Duration) | Fase 3 | FUSIÓN | ↑ (Aumenta) | VIABLE |
| 2 | Velocidad Angular Pico de Guiñada (Turn Peak Yaw Velocity) | Fase 3 | IMU | ↓ (Disminuye) | VIABLE |
| 3 | Número de Pasos durante el Giro (Turn Step Count) | Fase 3 | FUSIÓN | ↑ (Aumenta) | VIABLE |
| 4 | Velocidad de Marcha (Gait Speed) | Fase 2/4 | FUSIÓN | ↓ (Disminuye) | VIABLE |
| 5 | Longitud de Paso (Step Length) | Fase 2/4 | RGB-D | ↓ (Disminuye) | VIABLE |
| 6 | Variabilidad del Tiempo de Paso (Step Time Variability) | Fase 2/4 | IMU | ↑ (Aumenta) | VIABLE |
| 7 | Armónico de Marcha / Regularidad (Harmonic Ratio) | Fase 2/4 | IMU | ↓ (Disminuye) | VIABLE |
| 8 | Duración de la Transición a Bípedo (Sit-to-Stand Duration) | Fase 1 | FUSIÓN | ↑ (Aumenta) | VIABLE |
| 9 | Velocidad Angular Pico de Flexión (Peak Trunk Flexion Velocity) | Fase 1 | IMU | ↓ (Disminuye) | VIABLE |
| 10 | Impacto Vertical al Sentarse (Peak Vertical Deceleration) | Fase 5 | IMU | ↑ (Aumenta) | VIABLE |
| 11 | Amplitud de Balanceo de Brazos (Arm Swing Amplitude) | Fase 2/4 | RGB-D | ↓ (Disminuye) | VIABLE |
| 12 | Índice de Congelamiento de la Marcha (FoG Index) | Fase 2/3/4 | IMU | ↑ (Aumenta) | VIABLE |
| 13 | Ancho de Paso / Base de Sustentación (Step Width) | Fase 2/4 | RGB-D | ↑ (Aumenta) | VIABLE |
| 14 | Duración Total del TUG (Total TUG Time) | Global | FUSIÓN | ↑ (Aumenta) | VIABLE |
| 15 | Rango de Movimiento del Tronco (Trunk Pitch ROM) | Fase 1/5 | IMU | ↓ (Disminuye) | VIABLE |

### Grupo B: Variables Complementarias
| # | Nombre de la Variable | Fase TUG | Fuente Sensorial | Comportamiento EP | Viabilidad |
|---|---|---|---|---|---|
| 16 | Aceleración Vertical Pico (STS Peak Vertical Acceleration) | Fase 1 | IMU | ↓ (Disminuye) | VIABLE |
| 17 | Longitud de Zancada (Stride Length) | Fase 2/4 | RGB-D | ↓ (Disminuye) | VIABLE |
| 18 | Cadencia de Marcha (Cadence) | Fase 2/4 | FUSIÓN | Mixto / Disperso | VIABLE |
| 19 | Tiempo de Paso (Step Time) | Fase 2/4 | IMU | ↑ (Aumenta) | VIABLE |
| 20 | Tiempo de Fase de Apoyo (Stance Phase Duration) | Fase 2/4 | IMU | ↑ (Aumenta) | DESCARTADA (IMU) |
| 21 | Tiempo de Doble Apoyo (Double Support Time) | Fase 2/4 | RGB-D | ↑ (Aumenta) | VIABLE |
| 22 | Simetría Espacial del Paso (Step Spatial Symmetry) | Fase 2/4 | RGB-D | ↓ (Menos simetría)| VIABLE |
| 23 | Desplazamiento Medio-Lateral del Tronco (Mediolateral Sway) | Fase 2/4 | IMU | ↑ (Aumenta) | VIABLE |
| 24 | Velocidad Angular Media de Giro (Mean Turn Angular Velocity) | Fase 3 | IMU | ↓ (Disminuye) | VIABLE |
| 25 | Turn Jerk (Suavidad del giro) | Fase 3 | IMU | ↑ (Aumenta) | VIABLE |
| 26 | Duración de Transición a Sentado (Stand-to-Sit Duration) | Fase 5 | FUSIÓN | ↑ (Aumenta) | VIABLE |
| 27 | Flexión Pico del Tronco al Sentarse (Peak Trunk Flexion) | Fase 5 | IMU | ↓ (Disminuye) | VIABLE |
| 28 | Duración del Giro Final (Pre-Sit Turn Duration) | Fase 5 | IMU | ↑ (Aumenta) | VIABLE |
| 29 | Número Total de Pasos (Total Step Count) | Global | IMU | ↑ (Aumenta) | VIABLE |
| 30 | Aceleración Cuadrática Media (RMS Acceleration Global) | Global | IMU | ↓ (Disminuye) | VIABLE |
| 31 | Variabilidad de la Velocidad de Giro (Turn Velocity Variability) | Fase 3 | IMU | ↑ (Aumenta) | VIABLE |
| 32 | Costo de Tarea Dual (Dual-Task Cost - DTC) | Global | FUSIÓN | ↑ (Aumenta) | VIABLE |
| 33 | Área de Balanceo del Centro de Masa (CoM Sway Area) | Fase 1/5 | RGB-D | ↑ (Aumenta) | VIABLE |
| 34 | Índice de Suavidad de la Transición (Transition SPARC) | Fase 1/5 | IMU | ↓ (Disminuye) | VIABLE |
| 35 | Simetría Espacial de Giro (Turn Spatial Symmetry) | Fase 3 | RGB-D | ↓ (Menos simetría)| VIABLE |
| 36 | Aceleración Máxima de Impacto del Talón (Heel Strike Peak Accel)| Fase 2/4 | IMU | ↓ (Disminuye) | VIABLE |
| 37 | Variabilidad del Tiempo de Balanceo (Swing Time Variability) | Fase 2/4 | RGB-D | ↑ (Aumenta) | VIABLE |
| 38 | Duración Pospuesta del Paso (Delayed Step Initiation) | Transición | FUSIÓN | ↑ (Aumenta) | VIABLE |


---

## 4. Recomendación para el Sprint de Extracción Computacional

Como investigador principal de biomecánica, se recomienda priorizar computacionalmente las **Top 15 Variables de Oro** descritas en el **Grupo A**.

Esta priorización asegura que el algoritmo entregará métricas con directa interpretabilidad clínica para la escala UPDRS-III de la FVL, evitando el cálculo de variables de segundo nivel altamente ruidosas que puedan perjudicar el rendimiento del modelo clasificador.
