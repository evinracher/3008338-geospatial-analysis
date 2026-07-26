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
