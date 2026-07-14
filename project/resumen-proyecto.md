# Resumen del proyecto: predicción espacial del precio de vivienda en Medellín

Este documento resume el trabajo desarrollado en [`house-price-medellin.ipynb`](house-price-medellin.ipynb) y explica los conceptos necesarios para entenderlo sin conocimientos previos de análisis geoespacial. La metodología espacial sigue principalmente los capítulos del `Libro_AnalisisGeoespacial` sobre datos espaciales, matrices de pesos, autocorrelación y regresión espacial.

## 1. La idea central en un minuto

El proyecto busca explicar y predecir el precio de venta de un inmueble en Medellín usando sus características y ubicación.

Un modelo convencional trata cada vivienda como una observación independiente. El análisis espacial añade una pregunta fundamental:

> ¿El precio de una vivienda está relacionado con los precios o con las condiciones no observadas de las viviendas cercanas?

El flujo aplicado fue:

1. Descargar, filtrar y limpiar los datos.
2. Preparar variables numéricas y categóricas.
3. Entrenar Random Forest y XGBoost como modelos predictivos.
4. Convertir las viviendas en puntos geográficos.
5. Definir cuáles viviendas son vecinas mediante KNN.
6. comprobar si los precios cercanos tienden a parecerse usando el I de Moran.
7. Comprobar si los modelos dejan errores agrupados espacialmente.
8. Ajustar OLS, SEM y SAR-Lag para representar explícitamente la dependencia espacial.
9. Comparar capacidad de ajuste, predicción y autocorrelación residual.

El resultado principal es que los precios presentan una estructura espacial fuerte. SEM logra representar completamente la dependencia residual, SAR-Lag obtiene el mejor ajuste entre los modelos estadísticos y Random Forest mantiene el mejor desempeño predictivo en el conjunto de prueba.

---

## 2. Problema de investigación

La variable objetivo es el precio de venta de los inmuebles en Medellín. Las variables disponibles son:

- Latitud y longitud.
- Comuna o zona, almacenada como `neighborhood`.
- Número de habitaciones, dormitorios y baños.
- Área total y área cubierta.
- Tipo de propiedad.
- Precio.

Las preguntas del proyecto son:

1. ¿Qué tan bien puede predecirse el precio con modelos de Machine Learning?
2. ¿Los precios presentan un patrón espacial?
3. ¿Los modelos convencionales dejan errores espacialmente relacionados?
4. ¿La dependencia se representa mejor como relación entre precios vecinos o como factores espaciales omitidos?

---

## 3. Datos y procesamiento

### 3.1 Fuente

Los datos provienen del conjunto **Colombia Housing Properties Price**, publicado en Kaggle. El archivo original contiene un millón de publicaciones inmobiliarias.

### 3.2 Filtros principales

El procesamiento siguió esta secuencia:

1. Selección de las columnas relevantes.
2. Filtro de registros cuya ciudad es Medellín: 262.856 observaciones.
3. Selección exclusiva de operaciones de venta: 119.394 observaciones.
4. Eliminación de registros sin latitud o sin precio: 36.524 observaciones.
5. Eliminación del 1 % inferior y superior del precio para reducir valores extremos.
6. Dataset analítico final: **35.814 viviendas**.

El precio final se encuentra entre 82 millones y 4.200 millones de pesos, con mediana de 420 millones.

### 3.3 Datos faltantes

Las variables de área tienen cerca del 96 % de valores faltantes. En los modelos de Machine Learning se conservaron mediante imputación, pero fueron excluidas de las regresiones espaciales porque contienen muy poca información observada.

Para el resto de variables se aplicó:

- Imputación con la mediana para variables numéricas.
- Estandarización de variables numéricas.
- Imputación y codificación *One-Hot* para barrio y tipo de propiedad.

La imputación se ajustó con los datos de entrenamiento para evitar fuga de información.

### 3.4 Partición de datos

El dataset se dividió aleatoriamente en:

- 70 % para entrenamiento.
- 30 % para prueba.

El conjunto de prueba se usó al final para medir la capacidad predictiva de Random Forest y XGBoost.

---

## 4. Modelos de Machine Learning

### 4.1 Random Forest

Random Forest combina muchos árboles de decisión. Cada árbol aprende reglas diferentes y la predicción final es el promedio de todos. Es útil porque captura relaciones no lineales e interacciones entre ubicación, barrio y características del inmueble.

### 4.2 XGBoost

XGBoost construye árboles secuencialmente. Cada árbol nuevo intenta corregir los errores de los anteriores. Puede ser muy preciso, pero depende bastante de la selección de hiperparámetros y de la calidad de las variables.

### 4.3 Optimización

Ambos modelos se ajustaron inicialmente con parámetros base y luego se optimizaron mediante `GridSearchCV`. Esta técnica evalúa distintas combinaciones de hiperparámetros usando validación cruzada.

### 4.4 Resultados sobre el precio original

| Modelo | MAE | RMSE | R² |
|---|---:|---:|---:|
| Random Forest base | $144,4 millones | $299,0 millones | 0,705 |
| Random Forest optimizado | **$143,2 millones** | **$294,2 millones** | **0,714** |
| XGBoost base | $212,4 millones | $370,7 millones | 0,546 |
| XGBoost optimizado | $198,1 millones | $348,8 millones | 0,598 |

Random Forest optimizado fue el mejor modelo predictivo. La importancia de variables mostró un peso alto de baños, latitud, longitud y pertenencia a El Poblado.

---

## 5. Conceptos geoespaciales fundamentales

## 5.1 ¿Qué hace espacial a un dato?

Un dato espacial combina:

- **Geometría:** dónde está la observación.
- **Atributos:** qué características tiene.
- **Relaciones espaciales:** qué observaciones están cerca o conectadas.

En este proyecto, cada vivienda es un punto con atributos como precio, baños y tipo de propiedad.

La primera ley de Tobler resume la intuición del análisis:

> Todo está relacionado con todo, pero las cosas cercanas tienden a estar más relacionadas que las lejanas.

Esto no significa que toda cercanía produzca una relación causal. Significa que la ubicación puede contener información útil que un modelo convencional ignora.

## 5.2 Dependencia y heterogeneidad espacial

Son conceptos distintos:

- **Dependencia espacial:** el valor de una observación se relaciona con los valores o errores de sus vecinas.
- **Heterogeneidad espacial:** la relación entre variables cambia según el lugar. Por ejemplo, un baño adicional podría asociarse con aumentos diferentes de precio en distintas zonas.

SEM y SAR-Lag modelan principalmente dependencia. GWR y MGWR, propuestos para una etapa futura, modelan heterogeneidad mediante coeficientes locales.

## 5.3 GeoDataFrame

Un `DataFrame` contiene filas y columnas. Un `GeoDataFrame` añade una columna `geometry` y un sistema de referencia de coordenadas. Esto permite calcular distancias, vecindades y operaciones espaciales.

Las columnas `lon` y `lat` se transformaron en puntos usando GeoPandas.

## 5.4 CRS y reproyección

Un **CRS** indica cómo interpretar las coordenadas.

- `EPSG:4326`, WGS 84, representa longitud y latitud en grados. Es adecuado para almacenar y visualizar ubicaciones globales.
- `EPSG:9377`, MAGNA-SIRGAS / Origen-Nacional, representa coordenadas colombianas en metros.

La reproyección no mueve las viviendas. Solo cambia la forma matemática de expresar su ubicación. Se necesita un CRS métrico porque KNN calcula distancias y los grados no son una unidad constante de longitud.

## 5.5 Transformación logarítmica del precio

Los precios presentan asimetría: existen muchas viviendas de precio medio y pocas extremadamente costosas. Se creó:

$$
\text{log\_price}=\log(\text{price})
$$

El logaritmo:

- Reduce la influencia de valores extremos.
- Estabiliza la variabilidad de los errores.
- Facilita el ajuste lineal.
- Convierte diferencias absolutas grandes en diferencias relativas más manejables.

El precio original se conservó. `log_price` se utilizó principalmente en los modelos estadísticos espaciales.

---

## 6. Matriz de pesos espaciales

## 6.1 ¿Qué representa?

La matriz de pesos espaciales $W$ formaliza quién es vecino de quién. Tiene una fila y una columna por observación:

$$
w_{ij}>0 \quad \text{si }j\text{ es vecina de }i
$$

$$
w_{ij}=0 \quad \text{si no son vecinas}
$$

La diagonal es cero porque una vivienda no se considera vecina de sí misma.

La matriz $W$ es una decisión del analista, no algo que los datos determinen automáticamente. Por eso se debe justificar y evaluar su sensibilidad.

## 6.2 K vecinos más cercanos

Como las viviendas son puntos, se utilizó **KNN**: para cada inmueble se seleccionan los $k$ puntos más cercanos.

Se probaron:

- $k=5$: 434 componentes desconectados.
- $k=10$: 18 componentes desconectados.
- $k=20$: red conectada.

Se eligió $k=20$ para los modelos porque todas las observaciones quedan integradas en una sola red.

## 6.3 Estandarización por filas

Los pesos se estandarizaron para que cada fila sume uno:

$$
\sum_j w_{ij}=1
$$

Así, cada vivienda distribuye una influencia total igual entre sus vecinos. Esto permite interpretar $Wy$ como un promedio espacial.

## 6.4 Rezago espacial

El rezago espacial de una variable es:

$$
Wy
$$

Para una vivienda $i$:

$$
(Wy)_i=\sum_j w_{ij}y_j
$$

Con pesos estandarizados, este valor se interpreta como el precio promedio de sus vecinos. Es el equivalente espacial de mirar el contexto inmediato de cada observación.

---

## 7. Autocorrelación espacial e I de Moran

## 7.1 ¿Qué es autocorrelación espacial?

Existe autocorrelación cuando la similitud de los valores se relaciona con la cercanía:

- **Positiva:** valores altos cerca de altos y bajos cerca de bajos.
- **Negativa:** valores altos cerca de bajos.
- **Cercana a cero:** no hay un patrón espacial global claro.

## 7.2 I de Moran

El I de Moran resume la asociación entre una variable y su rezago espacial. Conceptualmente compara cada valor con los valores de sus vecinos.

- $I>0$: agrupación de valores similares.
- $I\approx0$: comportamiento compatible con aleatoriedad espacial.
- $I<0$: agrupación de valores diferentes.

Su significancia se calculó con 999 permutaciones. En cada permutación se redistribuyen los valores entre ubicaciones y se compara el patrón aleatorio con el observado. Con 999 permutaciones, `p = 0.001` es el menor valor empírico posible.

El valor p indica si hay evidencia estadística, pero la magnitud de $I$ indica qué tan fuerte es el patrón. Con muestras grandes, asociaciones pequeñas pueden ser significativas.

## 7.3 Gráfico de Moran

El eje horizontal contiene la variable estandarizada y el vertical su rezago espacial. La pendiente corresponde al I de Moran.

Los cuadrantes principales son:

- Alto-Alto: valores altos rodeados de altos.
- Bajo-Bajo: valores bajos rodeados de bajos.
- Alto-Bajo: valor alto rodeado de bajos.
- Bajo-Alto: valor bajo rodeado de altos.

El gráfico global identifica una tendencia general. Para localizar agrupaciones específicas se usaría LISA, que quedó como extensión opcional.

## 7.4 Resultados del precio

| Vecinos | Moran de `price` | Moran de `log_price` | p simulado |
|---:|---:|---:|---:|
| 5 | 0,5165 | 0,6506 | 0,001 |
| 10 | 0,4542 | 0,6000 | 0,001 |
| 20 | 0,4151 | 0,5671 | 0,001 |

Conclusiones:

- Los precios cercanos tienden a parecerse.
- El resultado es robusto para tres valores de $k$.
- El patrón es más fuerte entre vecinos próximos.
- `log_price` hace más visible la estructura general al reducir la influencia de precios extremos.

---

## 8. ¿Por qué analizar residuos?

Un precio puede presentar autocorrelación porque barrios cercanos comparten características. Eso no prueba que un modelo sea incorrecto.

El diagnóstico importante es el residuo:

$$
e_i=y_i-\hat y_i
$$

Si los residuos siguen agrupados, el modelo se equivoca de manera sistemática según la ubicación. Esto viola la independencia de los errores y muestra que todavía queda información espacial sin representar.

### Residuos de Random Forest

Sobre 10.745 observaciones de prueba:

- Moran del residuo en precio original: $I=0,0222$, `p = 0.001`.
- Moran del residuo logarítmico: $I=0,0296$, `p = 0.001`.

La asociación es estadísticamente significativa, pero muy pequeña. Random Forest captura casi todo el patrón espacial mediante latitud, longitud, barrio y relaciones no lineales.

---

## 9. OLS hedónico como modelo de referencia

## 9.1 ¿Qué significa hedónico?

Un modelo hedónico explica el precio como combinación de atributos:

$$
\log(P_i)=\beta_0+\sum_k\beta_kX_{ik}+e_i
$$

El precio representa el valor conjunto de tamaño, baños, tipo, barrio y otras características. OLS estima un efecto global para cada variable y supone que las observaciones y errores son independientes.

## 9.2 Especificación

Se usaron:

- Habitaciones.
- Dormitorios.
- Baños.
- Barrio.
- Tipo de propiedad.

Las áreas se excluyeron por su alto porcentaje de datos faltantes.

## 9.3 Resultados

- R²: 0,5861.
- R² ajustado: 0,5857.
- RMSE de `log_price`: 0,4745.
- Moran residual: $I=0,2673$, `p = 0.001`.

OLS explica cerca del 59 % de la variación, pero deja una dependencia espacial importante. Baños es la variable numérica con mayor efecto. El Poblado, Laureles y Santa Elena presentan efectos positivos frente al barrio de referencia.

Estos coeficientes describen asociaciones, no efectos causales. Además, las variables numéricas fueron estandarizadas; por eso sus coeficientes representan cambios por desviación estándar y no directamente por una unidad física.

## 9.4 Diagnósticos LM

Las pruebas de Multiplicadores de Lagrange ayudan a seleccionar la forma de dependencia:

- **LM-Lag:** evalúa dependencia en la variable objetivo.
- **LM-Error:** evalúa dependencia en los errores.
- Las versiones robustas ayudan cuando ambas pruebas simples son significativas.

Resultados robustos:

- LM-Lag robusto: 1.598,84; `p < 0.001`.
- LM-Error robusto: 11.361,18; `p < 0.001`.

Ambas alternativas son relevantes, pero la evidencia inicial es más fuerte para SEM. Por eso se ajustaron los dos modelos.

---

## 10. SEM: modelo de error espacial

## 10.1 Idea

SEM supone que la dependencia está en factores no observados:

$$
y=X\beta+u
$$

$$
u=\lambda Wu+\varepsilon
$$

$u$ es el error con estructura espacial y $\varepsilon$ es la innovación final que debería comportarse aleatoriamente.

Ejemplos de factores omitidos que pueden estar espacialmente agrupados:

- Seguridad.
- Estrato socioeconómico.
- Accesibilidad.
- Ruido.
- Cercanía a equipamientos.
- Calidad urbana.

$\lambda$ mide la intensidad de esa dependencia. Un valor positivo alto significa que los factores omitidos de viviendas cercanas se parecen.

## 10.2 Resultado

- $\lambda=0,7363$; `p < 0.001`.
- Pseudo-R²: 0,5783.
- RMSE de ajuste: 0,4832.
- Moran del residuo filtrado: $I=-0,0007$; `p = 0.288`.

El residuo correcto para diagnosticar SEM es `e_filtered`, porque ya se retiró el componente espacial $\lambda Wu$. El residuo `u` todavía contiene la dependencia que el modelo busca representar.

La conclusión es clara: SEM elimina la autocorrelación residual. Su objetivo principal no es mejorar automáticamente la predicción puntual, sino corregir la estructura espacial de los errores y producir una representación estadística coherente.

---

## 11. SAR-Lag: modelo de rezago espacial

## 11.1 Idea

SAR-Lag incluye el precio de las viviendas vecinas:

$$
y=\rho Wy+X\beta+\varepsilon
$$

$\rho$ indica cuánto se relaciona el precio local con el promedio espacial de precios cercanos. En vivienda puede representar comparación de mercado, referencias de avalúo o características compartidas que se transmiten a través del vecindario.

## 11.2 Efectos directos e indirectos

En SAR-Lag, cambiar una variable en una vivienda puede afectar:

- **Efecto directo:** la propia vivienda.
- **Efecto indirecto:** viviendas vecinas por retroalimentación espacial.
- **Efecto total:** suma de ambos.

Por eso los coeficientes de SAR-Lag no deben interpretarse solos como en OLS.

Para baños, el modelo obtuvo aproximadamente:

- Efecto directo: 0,2514.
- Efecto indirecto: 0,2502.
- Efecto total: 0,5016.

Como baños está estandarizado y el precio está en logaritmo, esto describe una asociación relativa por una desviación estándar, no el aumento literal causado por agregar un baño.

## 11.3 Resultado

- $\rho=0,4989$; `p < 0.001`.
- Pseudo-R²: 0,6749.
- Pseudo-R² espacial: 0,6029.
- RMSE de ajuste: 0,4209.
- Moran residual: $I=0,0567$; `p = 0.001`.

SAR-Lag mejora claramente el ajuste frente a OLS y SEM. Sin embargo, deja una autocorrelación residual pequeña pero significativa, por lo que no representa toda la dependencia espacial.

---

## 12. Comparación final

### 12.1 Modelos estadísticos sobre la muestra completa

| Modelo | R² o pseudo-R² | RMSE log | Moran residual | p de Moran | Parámetro espacial |
|---|---:|---:|---:|---:|---:|
| OLS | 0,5861 | 0,4745 | 0,2673 | 0,001 | No aplica |
| SEM | 0,5783 | 0,4832 | **-0,0007** | **0,288** | $\lambda=0,7363$ |
| SAR-Lag | **0,6749** | **0,4209** | 0,0567 | 0,001 | $\rho=0,4989$ |

Interpretación:

- **SEM es preferible para explicar la dependencia residual**, porque deja errores compatibles con aleatoriedad espacial.
- **SAR-Lag es preferible por ajuste**, porque obtiene mayor pseudo-R² y menor RMSE entre los modelos estadísticos.

### 12.2 Comparación general

| Modelo | Tipo de evaluación | R² log | RMSE log | Moran residual |
|---|---|---:|---:|---:|
| OLS | Ajuste completo | 0,5861 | 0,4745 | 0,2673 |
| SEM | Ajuste completo | 0,5783 | 0,4832 | -0,0007 |
| SAR-Lag | Ajuste completo | 0,6749 | 0,4209 | 0,0567 |
| Random Forest | Prueba | **0,7767** | **0,3477** | 0,0296 |
| XGBoost | Prueba | 0,5373 | 0,5004 | 0,0698 |

Esta tabla usa una escala común, pero no constituye una competencia completamente justa: los modelos estadísticos muestran ajuste sobre toda la muestra y Machine Learning muestra predicción en datos de prueba.

La lectura correcta es:

- Random Forest es el mejor predictor disponible.
- SEM explica mejor la dependencia de los errores.
- SAR-Lag ofrece el mejor ajuste estadístico global.
- No existe un único “mejor modelo” sin definir primero si el objetivo es predecir, explicar o corregir dependencia espacial.

---

## 13. Significancia, magnitud y causalidad

Tres advertencias son esenciales:

### 13.1 Significativo no significa importante

Random Forest tiene Moran residual cercano a cero, pero `p = 0.001`. Con más de diez mil observaciones, una asociación débil puede ser estadísticamente detectable. Se deben leer juntos el estadístico y el valor p.

### 13.2 `p = 0.000` no significa probabilidad cero

Cuando una tabla redondea un valor muy pequeño a `0.000`, debe reportarse como `p < 0.001`.

### 13.3 Asociación no significa causalidad

Que baños y precio estén asociados no prueba que agregar un baño cause exactamente ese aumento. Pueden existir variables relacionadas con ambos, como tamaño, calidad o tipo de inmueble.

---

## 14. Limitaciones

1. Las áreas total y cubierta tienen demasiados datos faltantes.
2. No se incorporaron variables externas de seguridad, accesibilidad, transporte o equipamientos.
3. Muchos anuncios comparten coordenadas, aunque los identificadores originales son únicos. Esto puede reflejar edificios, ubicaciones aproximadas o republicaciones.
4. La partición de Machine Learning es aleatoria y no una validación espacial por bloques.
5. SEM y SAR-Lag se evaluaron como ajuste sobre la muestra completa, no como predicción espacial fuera de muestra.
6. La matriz KNN es una aproximación del mercado inmobiliario; otras definiciones de vecindad podrían cambiar los resultados.
7. Los resultados son asociaciones estadísticas y no estimaciones causales.

Estas limitaciones no invalidan el análisis, pero delimitan el alcance de sus conclusiones.

---

## 15. Qué quedaría para la entrega final

### 15.1 Validación espacial por bloques

Separar entrenamiento y prueba por zonas geográficas permitiría evaluar si el modelo generaliza a sectores no observados y reduciría la similitud espacial entre ambos conjuntos.

### 15.2 SLX y SDM

- **SLX:** incorpora rezagos espaciales de las variables explicativas, $WX$.
- **SDM:** combina $Wy$ y $WX$.

Las pruebas Spatial Durbin del OLS fueron significativas, por lo que estas extensiones tienen fundamento estadístico.

### 15.3 GWR y MGWR

GWR permite que cada coeficiente cambie según la ubicación:

$$
y_i=\beta_0(u_i,v_i)+\sum_k\beta_k(u_i,v_i)x_{ik}+\varepsilon_i
$$

MGWR permite además que cada variable opere a una escala espacial distinta. Estos modelos servirían para estudiar heterogeneidad: por ejemplo, si baños o tipo de propiedad tienen efectos diferentes entre zonas.

### 15.4 LISA

El Moran global confirma que existe agrupación, pero no dice dónde. LISA permitiría mapear agrupaciones Alto-Alto, Bajo-Bajo y valores atípicos espaciales.

---

## 16. Guía de estudio para aprenderlo en un día

### Bloque 1 — Datos espaciales

Aprender:

- Punto, atributo y GeoDataFrame.
- Diferencia entre coordenadas geográficas y proyectadas.
- Por qué las distancias requieren unidades métricas.

Idea que debe quedar: una coordenada no basta; también se necesita conocer su CRS.

### Bloque 2 — Vecindad

Aprender:

- Qué representa $W$.
- Cómo funciona KNN.
- Qué significa estandarizar por filas.
- Cómo interpretar $Wy$.

Idea que debe quedar: antes de medir dependencia hay que definir formalmente quién es vecino.

### Bloque 3 — Autocorrelación

Aprender:

- I de Moran.
- Gráfico de Moran.
- Permutaciones y valor p.
- Diferencia entre magnitud y significancia.

Idea que debe quedar: Moran responde si valores similares tienden a agruparse.

### Bloque 4 — Regresión espacial

Aprender:

- OLS como referencia.
- Moran de residuos.
- LM-Lag y LM-Error.
- Diferencia entre SEM y SAR-Lag.

Idea que debe quedar: SEM modela factores omitidos espacialmente relacionados; SAR-Lag modela relación directa con la variable objetivo de los vecinos.

### Bloque 5 — Selección

Aprender:

- R² y RMSE miden ajuste o predicción.
- Moran residual mide estructura espacial no explicada.
- El mejor modelo depende del objetivo.

Idea que debe quedar: un modelo puede predecir bien y ser poco interpretable, o explicar bien la dependencia sin ser el mejor predictor.

---

## 17. Glosario mínimo

| Concepto | Definición breve |
|---|---|
| CRS | Regla para interpretar coordenadas. |
| Reproyección | Conversión entre sistemas de coordenadas sin mover el objeto real. |
| GeoDataFrame | Tabla con geometría y CRS. |
| Matriz $W$ | Representación matemática de la vecindad. |
| KNN | Selección de los $k$ puntos más cercanos. |
| Rezago espacial | Promedio o combinación ponderada de valores vecinos. |
| Autocorrelación | Relación entre similitud de valores y cercanía. |
| I de Moran | Medida global de autocorrelación espacial. |
| Residuo | Diferencia entre valor observado y ajustado. |
| OLS | Regresión lineal global sin dependencia espacial explícita. |
| SEM | Modelo con dependencia espacial en los errores. |
| SAR-Lag | Modelo con rezago espacial de la variable dependiente. |
| $\lambda$ | Intensidad de la dependencia espacial del error. |
| $\rho$ | Intensidad de la dependencia espacial de la variable objetivo. |
| LISA | Indicador local que identifica agrupaciones específicas. |
| GWR | Regresión cuyos coeficientes cambian geográficamente. |

---

## 18. Material del curso utilizado

- [`01_DatosEspaciales.ipynb`](../Libro_AnalisisGeoespacial/01_DatosEspaciales.ipynb): datos espaciales, GeoDataFrame y CRS.
- [`07_MatrizCorrelacion.ipynb`](../Libro_AnalisisGeoespacial/07_MatrizCorrelacion.ipynb): matrices de pesos, KNN, rezago espacial, Moran global y LISA.
- [`09_SpatialRegression.ipynb`](../Libro_AnalisisGeoespacial/09_SpatialRegression.ipynb): OLS espacial, residuos, dependencia y heterogeneidad.
- [`10_SAR.ipynb`](../Libro_AnalisisGeoespacial/10_SAR.ipynb): SEM, SAR-Lag, SLX, SDM e impactos espaciales.
- [`13_MGWR.ipynb`](../Libro_AnalisisGeoespacial/13_MGWR.ipynb): heterogeneidad espacial, GWR y MGWR.

## 19. Síntesis final

El proyecto demuestra que el precio de vivienda en Medellín no se distribuye aleatoriamente en el espacio. La cercanía aporta información y debe formar parte del análisis.

- Moran confirmó una agrupación fuerte de precios similares.
- OLS dejó dependencia espacial importante.
- SEM identificó una dependencia fuerte en factores espaciales omitidos y produjo residuos espacialmente aleatorios.
- SAR-Lag confirmó una asociación entre precios vecinos y mejoró el ajuste estadístico.
- Random Forest aprovechó eficazmente la ubicación y obtuvo la mejor predicción en prueba.

La lección general es que el análisis espacial no consiste solamente en agregar latitud y longitud a un modelo. Requiere definir vecindad, medir dependencia, diagnosticar residuos y escoger una estructura espacial coherente con el proceso que se quiere estudiar.
