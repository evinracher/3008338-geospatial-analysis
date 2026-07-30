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

# LISA

El 23.8 % de las viviendas forma clusters Alto-Alto y el 24.4 % Bajo-Bajo. Esto muestra zonas amplias donde los precios similares se agrupan. Los casos Alto-Bajo (2.1 %) y Bajo-Alto (3.2 %) son viviendas que contrastan con sus vecinos. El 46.4 % no presenta asociación local significativa.

# Analisis espacial por barrios

# Dependencia espacial

**Sí existe dependencia espacial en el precio de las viviendas.** Los valores positivos y significativos del Moran global indican que los precios no se distribuyen al azar: las viviendas de precio alto tienden a estar cerca de otras viviendas costosas, mientras las de precio bajo suelen estar rodeadas por viviendas de precio bajo. Esta dependencia aparece tanto entre puntos individuales como al agrupar los anuncios por barrio. Además, parte del patrón permanece después de controlar las características de las viviendas, lo que señala la influencia de los precios vecinos y de factores territoriales no incluidos en los datos.