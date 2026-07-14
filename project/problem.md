# Descripción del problema

En este proyecto se busca predecir el precio de un inmueble en Medellín, basado en el número de habitaciones, número de baños, el area total del inmueble, el barrio en que está ubicado y la ubicación (dadas por la latitud y la longitud). 

# Métodología

La implementación de este proyecto se realizón en Python, llevando a cabo el procesamiento de datos del dataset, limpiando y filtrando los datos que no servían para el proyecto. Se realizó la normalización de los datos, la imputación y se manejaron algunos outliers en el precio. Luego se dividió el dataset en datos de entrenamiento y prueba y se  probaron varios modelos bases sin optimizar. Esto permitió mirar el desempeño de los modelos y hacer algunos ajustes. Posteriormente se optimizaron los parametros de algunos modelos usando para esto Grid Search y finalmente se compararon los modelos en el dataset de prueba.

Se evaluaron Random Forest y XGBoost como modelos de aprendizaje automático, OLS como referencia estadística y dos modelos de regresión espacial: SEM y SAR-Lag. Todos se ajustaron con el conjunto de entrenamiento y se compararon sobre el mismo conjunto de prueba.

# Base de datos

Los datos fueron tomados de Kaggle

Referencia: https://www.kaggle.com/datasets/julianusugaortiz/colombia-housing-properties-price

Se hizo procesamiento de datos y descartaron columnas que no eran relevantes para el problema, además de eliminar registros nulos.

# Resultados

El precio logarítmico presenta autocorrelación espacial positiva y significativa. En entrenamiento, el I de Moran varía entre 0,6254 con 5 vecinos y 0,5553 con 20 vecinos (`p = 0.001`), lo que evidencia agrupaciones locales de precios semejantes.

OLS obtuvo R² = 0,5870, pero dejó autocorrelación residual importante (I = 0,2461). SEM estimó una dependencia fuerte en el error ($\lambda=0,7351$) y eliminó la autocorrelación del residuo filtrado (I = -0,0013; `p = 0.243`). SAR-Lag estimó una asociación positiva entre precios vecinos ($\rho=0,5496$), alcanzó pseudo-R² = 0,6749 y redujo el Moran residual a 0,0353 durante el ajuste.

En prueba, SAR-Lag fue el mejor modelo estadístico, con R² = 0,5997 y RMSE = 0,4655 en `log_price`. Random Forest obtuvo el mejor desempeño general, con R² = 0,7756 y RMSE = 0,3485.

# Conclusiones

El precio de la vivienda en Medellín no se distribuye aleatoriamente: existe una estructura espacial fuerte que permanece parcialmente sin explicar en una regresión convencional. SEM muestra que una parte sustancial de esa dependencia corresponde a factores espaciales omitidos, como accesibilidad, seguridad o calidad urbana. SAR-Lag muestra además una relación positiva entre precios vecinos y efectos indirectos transmitidos por la red espacial.

No existe un modelo único superior para todos los objetivos. SEM es el más adecuado para representar y corregir la dependencia espacial de los errores durante el ajuste. SAR-Lag es el mejor modelo estadístico para predicción fuera de muestra y permite interpretar efectos directos e indirectos. Random Forest continúa siendo la opción más precisa cuando el objetivo principal es la predicción.

La principal limitación de los datos es el alto porcentaje de valores faltantes en las variables de área y la ausencia de características urbanas externas. Una etapa posterior debería incorporar estas variables y aplicar validación espacial por bloques.

# Referencias

Relacione tantas referencias bibliográficas como los enlaces (si aplica, libro HANDS ON MACHINE Learning, 2nd edition) a las bases de datos empleadas

J. U. Ortiz, “Colombia Housing Properties Price,” Kaggle.com, 2022. https://www.kaggle.com/datasets/julianusugaortiz/colombia-housing-properties-price (accessed May 28, 2026).

A. Géron, Hands-on Machine Learning with Scikit-Learn, Keras, and Tensorflow, Second Edition. Sebastopol (CA): O’Reilly, 2019. ‌
