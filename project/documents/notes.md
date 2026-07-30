El I de moran positivo indica que valores similares están cerca entre sí. 

p = 0,0001, estadisticamente significativos

No demuestra causalidad

# R2 score

El R² o coeficiente de determinación indica qué proporción de la variación observada en la variable objetivo es explicada por el modelo.


SEM y SAR-Lag modelan principalmente dependencia. GWR (Geographically Weighted Regression) y MGWR (Multiscale Geographically Weighted Regression), propuestas para una etapa futura, modelan heterogeneidad mediante coeficientes locales.

Los precios presentan asimetría: existen muchas viviendas de precio medio y pocas extremadamente costosas. Se creó la variable transformada:

log_price = log(price)

Se utilizó principalmente en los modelos estadísticos espaciales.

Existe autocorrelación cuando la similitud de los valores se relaciona con la cercanía:

Positiva: valores altos cerca de altos y bajos cerca de bajos.
Negativa: valores altos cerca de bajos.
Cercana a cero: no hay un patrón espacial global claro.

Random Forest captura casi todo el patrón espacial mediante latitud, longitud, barrio y relaciones no lineales.

Ejemplos de factores omitidos que pueden estar espacialmente agrupados:

Seguridad.
Estrato socioeconómico.
Accesibilidad.
Ruido.
Cercanía a equipamientos.
Calidad urbana.

# SEM

λ mide la intensidad de esa dependencia. Un valor positivo alto significa que los factores omitidos de viviendas cercanas se parecen.

# SAR-Lag

ρ indica cuánto se relaciona el precio local con el promedio espacial de precios cercanos. En vivienda puede representar comparación de mercado, referencias de avalúo o características compartidas que se transmiten a través del vecindario.

# Presentación final


## Interpretación de la centrografía

Esto ocurre porque el centro depende principalmente de dónde se concentran todos los anuncios, no solo de los más costosos. El Poblado reúne muchos anuncios caros, pero está al suroriente y su efecto se compensa con la oferta del centro, occidente y norte.

## Superficie kernel normalizada

Se puede confundir abundancia de anuncios con precios altos. Por eso se divide la suma suavizada de `log_price` entre la densidad suavizada de puntos. El resultado aproxima el precio logarítmico medio local. Se usa un ancho de banda de 1 km, una escala espacial cercana al entorno barrial, y se ocultan celdas con soporte kernel insuficiente.

Los máximos se observan principalmente hacia el sur y suroriente, alrededor de sectores de El Poblado, donde son frecuentes viviendas de mayor valor. Los niveles más bajos aparecen hacia sectores centrales y del norte.

## K means sobre la geometría

No se hizo basandose en el precio sino en la distancia y el precio los caracteriza. El mejor resultado dió con 3 clusteres para este caso.

El cluster 0 agrupa sobre todo sectores centrales y del norte, como La Candelaria y Boston, con mediana de $250 millones.

El cluster 1 cubre buena parte del occidente, con Laureles, Los Conquistadores y Belén, y mediana de $340 millones.

El cluster 2 reúne principalmente El Poblado y alcanza $690 millones.

# LISA (Local Indicators of Spatial Association) - Asociación espacial

LISA identifica 29 barrios Alto-Alto: barrios de precio alto junto a otros de precio alto. También encuentra 37 Bajo-Bajo: barrios de precio bajo rodeados por precios bajos. Los cinco Alto-Bajo y el único Bajo-Alto son contrastes locales; 154 barrios no son significativos.

El 23.8 % de las viviendas forma clusters Alto-Alto y el 24.4 % Bajo-Bajo. Esto muestra zonas amplias donde los precios similares se agrupan. Los casos Alto-Bajo (2.1 %) y Bajo-Alto (3.2 %) son viviendas que contrastan con sus vecinos. El 46.4 % no presenta asociación local significativa.

# Analisis espacial por barrios

El Moran es positivo y significativo (`I = 0.4752`, `p = 0.001`). 

# Dependencia espacial

**Sí existe dependencia espacial en el precio de las viviendas.** Los valores positivos y significativos del Moran global indican que los precios no se distribuyen al azar: las viviendas de precio alto tienden a estar cerca de otras viviendas costosas, mientras las de precio bajo suelen estar rodeadas por viviendas de precio bajo.

Esta dependencia aparece tanto entre puntos individuales como al agrupar los anuncios por barrio. Además, parte del patrón permanece después de controlar las características de las viviendas, lo que señala la influencia de los precios vecinos y de factores territoriales no incluidos en los datos.

# Heterogeneidad espacial

**GWR (*Geographically Weighted Regression*)**, o Regresión Geográficamente Ponderada, estima una regresión alrededor de cada ubicación. Permite analizar cómo cambia dentro de Medellín la relación entre el precio y las características de la vivienda. Utiliza el mismo ancho de banda para todas las variables.

**MGWR (*Multiscale Geographically Weighted Regression*)**, o Regresión Geográficamente Ponderada Multiescala, permite que cada variable tenga su propio ancho de banda. Así, algunas relaciones pueden cambiar entre zonas cercanas, mientras otras se mantienen estables en áreas más amplias.

OLS global explica el 37.7 % de la variación del precio en esta muestra (`R² = 0.3768`). GWR aumenta el R² a `0.6277` y MGWR a `0.6370`. Esto indica que permitir relaciones diferentes según la ubicación mejora claramente el ajuste.

El R² ajustado también favorece a MGWR (`0.6102`) frente a GWR (`0.5985`), incluso después de considerar la mayor complejidad de los modelos locales. MGWR presenta además el menor AICc (`2773.17` frente a `2837.88`); como un AICc menor representa un mejor equilibrio entre ajuste y complejidad, este resultado favorece a MGWR.

MGWR utiliza menos parametros que GWR.

Esto ocurre porque cada variable se suaviza con su propia escala espacial. En conjunto, MGWR logra el mejor ajuste de los tres sin necesitar una complejidad efectiva mayor que GWR. El AICc de OLS aparece vacío porque no se calculó con el mismo procedimiento local usado por GWR y MGWR.

## Efecto de las variables

**Habitaciones** tiene un coeficiente positivo en toda la ciudad, entre 0.027 y 0.135. La relación es más fuerte en el centro y centro-oriente y más débil hacia el suroccidente. Es significativa en 54.1 % de los puntos. Su ancho de banda de 1.015 vecinos indica que cambia lentamente y funciona como una relación más amplia que local.

## Colinealidad

MGWR logra el mejor ajuste local. Baños es significativo en 83.5 % de los puntos, habitaciones en 54.1 % y dormitorios en 5.0 %. Ninguna ubicación supera un número de condición de 30, por lo que no se detecta multicolinealidad local fuerte.

La multicolinealidad ocurre cuando varios predictores aportan información muy parecida y sus coeficientes se vuelven difíciles de separar. Ningún punto supera el número de condición de 30, así que no se observa multicolinealidad local fuerte.

**Sí existe heterogeneidad espacial.** La relación entre baños y precio es positiva, pero su intensidad cambia según la ubicación: el coeficiente varía aproximadamente entre 0.154 y 0.747. Además, MGWR mejora el ajuste frente a GWR y encuentra anchos de banda diferentes para cada variable. Como no se observa multicolinealidad local fuerte, estas diferencias espaciales no parecen ser producto de predictores difíciles de separar, sino de relaciones que realmente varían dentro de Medellín.

## Modelos jerárquicos

Se comparan tres modelos con `log_price` y los mismos atributos numéricos. El **OLS global** supone un único nivel de precio para toda Medellín. El modelo de **intercepto aleatorio** permite que cada barrio tenga un nivel base diferente. El modelo de **intercepto y pendiente aleatoria** también permite que la relación entre baños y precio cambie entre barrios.

El modelo de intercepto y pendiente aleatoria de baños obtiene el menor AIC (`27755.80`) y RMSE en muestra (`0.4303`). Mejora al modelo de solo intercepto (`RMSE = 0.4410`) y a OLS (`0.5773`). Esto indica que los barrios difieren tanto en su nivel base de precios como en la relación entre baños y precio.

El **AIC** corresponde a *Akaike Information Criterion*, o **Criterio de Información de Akaike**. Es una medida estadística utilizada para comparar modelos ajustados sobre los mismos datos y busca un equilibrio entre buen ajuste y complejidad. Penaliza los modelos que añaden parámetros sin mejorar suficientemente el ajuste. Un valor menor indica un modelo preferible; el resultado se interpreta de forma relativa frente a los demás modelos, no de manera aislada.

## Efectos por barrio

Los tonos rojos indican barrios cuyo precio base queda por encima del promedio después de controlar habitaciones, dormitorios y baños; los azules indican un nivel base menor. Los efectos positivos se concentran principalmente en el suroriente, especialmente en El Poblado, mientras varios sectores del norte presentan efectos negativos. Esto muestra que el barrio aporta información que las características de la vivienda no capturan.

## Kriging y procesos gaussianos

Regresión-Kriging obtiene el mejor resultado (`R² = 0.4373`, `RMSE = 0.4343`, `MAE = 0.3116`). Kriging ordinario alcanza `R² = 0.2256` y `RMSE = 0.5094`; el proceso gaussiano, `R² = 0.1610` y `RMSE = 0.5302`. La mejora ocurre porque Regresión-Kriging usa habitaciones, dormitorios y baños para estimar la tendencia y luego interpola lo que esa tendencia no explica.

Los residuos todavía presentan dependencia espacial. Es menor en Regresión-Kriging (`I = 0.0657`, `p = 0.017`) que en Kriging (`I = 0.1878`) y en el proceso gaussiano (`I = 0.2481`). Por tanto, Regresión-Kriging captura mejor la estructura espacial, aunque aún queda un patrón pequeño sin explicar.

## Superficies de predicción e incertidumbre

Las superficies muestran el precio esperado en `log_price` y cuánto puede variar esa predicción. Una incertidumbre alta significa menor confianza, no necesariamente un precio alto.

Kriging muestra los valores más altos en el sur y suroriente, especialmente alrededor de El Poblado: El Tesoro, San Lucas, Los Balsos, La Florida y Castropol. Allí se concentran anuncios de mayor precio y el método transmite esa información a lugares cercanos. Los valores bajan hacia el centro-norte y norte. La superficie es suave porque Kriging combina precios vecinos según el variograma, sin usar atributos de las viviendas.

La incertidumbre de Kriging es menor en el centro, centro-occidente y buena parte del sur, donde hay mejor soporte de anuncios. Aumenta en los bordes, especialmente al oriente, nororiente y algunos extremos occidentales, porque la predicción depende de puntos más lejanos. Su promedio es `0.5989` en `log_price`; por eso las estimaciones periféricas deben leerse con más cautela.

La media del proceso gaussiano repite el patrón principal: precios altos en El Poblado y el suroriente, valores intermedios en el occidente —por ejemplo Laureles y Belén— y menores hacia el norte. El kernel Matérn genera una transición continua entre los puntos. Su R² por bloques es `0.1610`, menor que Kriging ordinario y Regresión-Kriging, por lo que representa la tendencia general, pero explica poco de la variación en zonas completas no vistas.

La incertidumbre posterior es menor en las zonas centrales y aumenta hacia la periferia, sobre todo al oriente y nororiente. Allí hay menos evidencia cercana y el modelo debe extender el patrón aprendido. La incertidumbre media es `0.6624`, mayor que la de Kriging (`0.5989`) y Regresión-Kriging (`0.5628`). Junto con su RMSE de `0.5302`, esto muestra que el proceso gaussiano fue el método continuo menos preciso en esta validación.

Ambos métodos condicionan una estructura de dependencia espacial a valores observados y producen predicción e incertidumbre. En Kriging, la dependencia se expresa mediante el variograma —nugget, sill y range—; en el proceso gaussiano se expresa mediante el kernel —ruido, varianza y longitud de escala—. Kriging ordinario estima una media local desconocida, mientras el proceso gaussiano ofrece una formulación probabilística flexible y aprende sus hiperparámetros mediante verosimilitud marginal.

## Comparación final

Los modelos no se evaluaron todos de la misma forma. OLS, SEM y SAR usan la prueba aleatoria original; GWR, MGWR y el modelo jerárquico muestran ajuste sobre su propia muestra; los métodos de interpolación usan bloques espaciales completos. Por eso las cifras se comparan principalmente dentro de cada grupo.

Entre los modelos espaciales globales, SAR obtiene el mejor resultado de prueba (`R² = 0.5997`, `RMSE = 0.4655`). Su parámetro `rho = 0.5496` confirma que el precio de las viviendas vecinas aporta información. SEM es útil para otro propósito: su `lambda = 0.7351` muestra que existen factores territoriales omitidos y su error filtrado ya no presenta dependencia significativa. OLS es una base clara, pero deja más agrupación espacial en sus residuos.

Para estudiar heterogeneidad, GWR y MGWR mejoran ampliamente al OLS ajustado sobre los mismos 1.890 puntos. MGWR logra el mejor resultado (`R² ajustado = 0.6102`, `RMSE = 0.4678`, `AICc = 2773.17`) porque permite una escala distinta para cada atributo. GWR deja un Moran residual de `0.0132` no significativo; MGWR deja un valor pequeño y negativo de `-0.0347`.

El modelo jerárquico muestra que el barrio importa: el ICC de `0.4809` atribuye cerca del 48 % de la variación residual a diferencias entre barrios. El modelo con intercepto y pendiente aleatoria de baños tiene el menor AIC y RMSE en muestra, por lo que describe mejor estos regímenes barriales que el modelo de solo intercepto.

En la validación espacial por bloques, Regresión-Kriging es el mejor método continuo (`R² = 0.4373`, `RMSE = 0.4343`). Supera a Kriging ordinario y al proceso gaussiano porque combina atributos de la vivienda con una corrección espacial. Aun así, conserva una dependencia residual pequeña (`I = 0.0657`), de modo que ninguna superficie explica por completo el patrón territorial.


## Conclusiones

La ubicación geográfica sí está relacionada con el precio de las viviendas en Medellín. Los valores más altos se concentran principalmente en el sur y suroriente, especialmente en El Poblado, mientras en varios sectores del centro-norte y norte predominan precios menores. K-means confirma esta diferencia: el grupo localizado principalmente en El Poblado tiene una mediana de $690 millones, frente a $340 millones en buena parte del occidente y $250 millones en sectores centrales y del norte. La ubicación resume condiciones del entorno como accesibilidad, servicios, seguridad, oferta urbana y valoración del barrio.

También existe dependencia espacial: el precio de una vivienda se relaciona con los precios observados a su alrededor. Los precios de vivienda en Medellín presentan una dependencia espacial clara. Los precios cercanos suelen parecerse más de lo esperado por azar. LISA ubica grupos Alto-Alto en zonas donde viviendas costosas están rodeadas por otras costosas, y grupos Bajo-Bajo donde los precios bajos también se agrupan.

La cercanía de los inmuebles vecinos mejora la explicación y la predicción. OLS considera las características de la vivienda, pero deja dependencia en sus residuos (`I = 0.2461`). SEM muestra que existen factores territoriales no incluidos, mientras SAR confirma una relación positiva entre el precio y los precios vecinos. SAR es el mejor modelo espacial global evaluado en prueba (`R² = 0.5997`, `RMSE = 0.4655`), aunque su Moran residual de `0.1753` indica que la cercanía no explica por sí sola todo el patrón.

Además de dependencia, existe heterogeneidad espacial porque la relación entre los atributos y el precio no es igual en toda Medellín. MGWR mejora a GWR y alcanza un R² ajustado de `0.6102`. El efecto de baños es positivo y significativo en 83.5 % de los puntos, pero su intensidad cambia según la zona. Los distintos anchos de banda muestran que cada atributo actúa a una escala espacial diferente.

Los barrios también funcionan como contextos diferentes. El ICC de `0.48` indica que cerca del 48 % de la variación restante está asociada con diferencias entre barrios, después de considerar las variables incluidas. El modelo con intercepto y pendiente aleatoria obtiene el menor AIC (`27755.80`) y RMSE en muestra (`0.4303`). Esto confirma que una vivienda con características similares puede tener un precio distinto según el barrio y que incluso el aporte de un baño adicional cambia entre barrios.

Predecir el precio sigue siendo difícil porque depende de muchos factores que no están en los datos: área construida, estado del inmueble, antigüedad, piso, parqueaderos, seguridad, ruido, accesibilidad y cercanía a servicios. También hay pocos anuncios en algunas zonas y diferencias entre el precio publicado y el precio real de venta. Regresión-Kriging fue la mejor interpolación por bloques (`R² = 0.4373`, `RMSE = 0.4343`), pero todavía dejó dependencia residual. En conjunto, SAR explica mejor la relación global con los vecinos, MGWR muestra cómo cambian las relaciones dentro de la ciudad y Regresión-Kriging ofrece la mejor superficie de predicción evaluada.
