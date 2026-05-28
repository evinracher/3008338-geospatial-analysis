Seciones que deben ir en el poster para la presentación

# Descripción del problema

En este proyecto se busca predecir el precio de un inmueble en Medellín, basado en el número de habitaciones, número de baños, el area total del inmueble, el barrio en que está ubicado y la ubicación (dadas por la latitud y la longitud). Es un problema de regresión supervisada, y se evaluaran los métodos: Regresión lineal, Árbol de decisión, Random Forest, XGBoost y redes neuronales.

# Métodología

Describir mediante un diagrama de flujo las tres métodologías

CRÍTICO

Se realizó el procesamiento de datos del dataset, limpiando y filtrando los datos que no servían para el proyecto. Se realizó la normalización de los datos, la imputación y se manejaron algunos outliers en el precio. Luego se dividió el dataset en datos de entrenamiento y prueba y se  probaron varios modelos bases sin optimizar. Esto permitió mirar el desempeño de los modelos y hacer algunos ajustes. Posteriormente se optimizaron los parametros de algunos modelos usando para esto Grid Search y finalmente se compararon los modelos en el dataset de prueba.

# Base de datos

Los datos fueron tomados de Kaggle

TODO: describir los tipos de datos

Referencia: https://www.kaggle.com/datasets/julianusugaortiz/colombia-housing-properties-price

Se hizo procesamiento de datos y descartaron columnas que no eran relevantes para el problema, además de eliminar registros nulos.

TODO: INSERTAR TABLAS Y DISTRIBUCIONES DE FRECUENCIA DE PROPERTY TYPE Y NEIGHBORHOOD

# Resultados

Resuma mediante tablas y figuras los principales resultados, evidenciando la
comparación de las técnicas aplicadas.

# Conclusiones

Brevemente presente las conclusiones de su proyecto

Se evidenció que los resultados en la fase de prueba con el dataset de prueba fueron ligeramente menores a los resultados del entrenamiento. Esto puede ser el resultado de la calidad de los datos disponibles en el dataset para entrenar el modelo, los cuales tenían algunas características faltantes para gran parte de los registros. Sin embargo, en general algunos modelos obtuvieron métricas aceptables, como el caso del Random Forest, con un R2 Score DEEEEEE:  y un ERROR TÍPICO MEDIO DEEEEE. Estos resultados son satisfactorios para un proyecto de este tipo, donde se buscó un dataset cercano a la realidad. En proyectos con datasets academicos suelen obtenerse mejores resultados pero esto se debe en parte porque los datos están curados y optimizados para demostrar los modelos que se usan.

De la naturaleza de los datos a usar, resulta interesante que el número de baños sea la característica con mayor correlación con el precio. Se esperaba que fuera el area total o la ubicación. Esto se puede deber a que el area total faltaba en gran parte de los registros y que los modelos usados no eran modelos espaciales que le dieran un peso mayor a la ubicación o que tuvieran en cuenta la relación entre la ubicación de los registros y sus caracteristicas. Un trabajo a futuro interesante sería probar con modelos espaciales y ver que tanta importancia podría aportar la ubicación al precio del inmueble.

En este proyecto de aprendizaje de máquinas se pudo comprobar que gran parte del trabajo en la aplicación de modelos reside en la parte de procesamiento de datos. Analizar, limpiar, extraer, filtrar los datos representa gran parte del proceso y puede tener un gran efecto en los resultados si no se hace adecuadamente.

# Referencias

Relacione tantas referencias bibliográficas como los enlaces (si aplica, libro HANDS ON MACHINE Learning, 2nd edition) a las bases de datos empleadas

J. U. Ortiz, “Colombia Housing Properties Price,” Kaggle.com, 2022. https://www.kaggle.com/datasets/julianusugaortiz/colombia-housing-properties-price (accessed May 28, 2026).

A. Géron, Hands-on Machine Learning with Scikit-Learn, Keras, and Tensorflow, Second Edition. Sebastopol (CA): O’Reilly, 2019. ‌

PREGUNTAS:

- SE PUEDE HACER EN OTRO SOFTWARE O TINENE QUE SER EN POWER POINT Y CON BASE EN LA PLATILLA (ESCUDO Y DEMÁS): MEJOR ESE PARA MAS ESTANDAR

- Como sería el paddle? hay que registrarse o que se pondría en el asunto?: NOTA Y AUTORES

- La entrega está para el viernes 29 de Mayo en el moodle, pero en la guía dice que para el 30. Entonces cual sería la fecha final (29 de Mayo)

Practica 3 3 de junio