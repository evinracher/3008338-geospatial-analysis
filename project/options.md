# Proyectos de Análisis Geoespacial + Machine Learning

## 1. Clasificación de cultivos

**Tipo de dato:**  
Áreas (polígonos de parcelas agrícolas)

**Problema:**  
Identificar automáticamente el tipo de cultivo presente en cada parcela (café, maíz, arroz, etc.) usando imágenes satelitales y datos geoespaciales. El reto principal es que los cultivos pueden verse similares visualmente, pero presentan diferencias en patrones espectrales, ciclos temporales y contexto geográfico.

**ML aplicado:**  
- Segmentación semántica (U-Net, DeepLab)  
- Clasificación multiclase (Random Forest, XGBoost, CNN)

**Input:**  
- Imágenes satelitales (Sentinel-2)  
- Polígonos de parcelas  
- Datos espectrales multibanda  

**Output:**  
- Mapa clasificado por tipo de cultivo  

**Valor:**  
- Optimización agrícola  
- Monitoreo de producción  
- Planeación territorial  

**Cómo se aplica a Colombia y Medellín:**  
- Colombia es altamente agrícola (café, caña, banano)  
- En Antioquia se puede aplicar para análisis de cultivos cafeteros  
- Útil para agrotech y políticas públicas rurales  

---

## 2. Detección de expansión urbana

**Tipo de dato:**  
Superficies (imágenes raster temporales)

**Problema:**  
Detectar cómo crecen las ciudades en el tiempo, identificando cambios en el uso del suelo (de rural a urbano). El reto es analizar series temporales y distinguir entre crecimiento real y ruido en las imágenes.

**ML aplicado:**  
- Change Detection  
- Segmentación  
- Modelos temporales (CNN + series de tiempo)

**Input:**  
- Imágenes satelitales históricas (Landsat, Sentinel)  

**Output:**  
- Mapas de expansión urbana  
- Comparaciones entre años  

**Valor:**  
- Planeación urbana  
- Análisis inmobiliario  
- Identificación de zonas de crecimiento  

**Cómo se aplica a Colombia y Medellín:**  
- Medellín y el Valle de Aburrá tienen expansión acelerada  
- Útil para detectar urbanización informal  
- Aplica directamente a inversión inmobiliaria  

---

## 3. Detección de deforestación

**Tipo de dato:**  
Áreas (superficies forestales)

**Problema:**  
Identificar pérdida de cobertura forestal en el tiempo, diferenciando entre bosque y no bosque. El reto es detectar cambios sutiles y evitar falsos positivos por variaciones estacionales.

**ML aplicado:**  
- Segmentación binaria  
- Change detection  

**Input:**  
- Imágenes satelitales (Landsat, Sentinel)  

**Output:**  
- Mapas de pérdida de bosque  

**Valor:**  
- Impacto ambiental  
- Monitoreo de deforestación  
- Soporte a políticas públicas  

**Cómo se aplica a Colombia y Medellín:**  
- Colombia tiene alta deforestación en Amazonía  
- En Antioquia hay presión sobre zonas rurales  
- Útil para proyectos ambientales y ONG  

---

## 4. Identificación de techos para energía solar

**Tipo de dato:**  
Áreas (techos) y puntos (centroides)

**Problema:**  
Detectar automáticamente techos aptos para instalación de paneles solares, considerando área, orientación y ubicación. El reto es segmentar correctamente edificaciones en entornos urbanos complejos.

**ML aplicado:**  
- Segmentación (U-Net)  
- Object detection (YOLO)

**Input:**  
- Imágenes satelitales o aéreas  
- Footprints de edificios  

**Output:**  
- Mapa de techos disponibles  
- Estimación de área útil  

**Valor:**  
- Energía renovable  
- Oportunidad de negocio (SaaS)  

**Cómo se aplica a Colombia y Medellín:**  
- Medellín tiene alta radiación solar  
- Mercado creciente de paneles solares  
- Aplicable a empresas y hogares  

---

## 5. Clasificación de cuerpos de agua

**Tipo de dato:**  
Superficies (raster)

**Problema:**  
Identificar y segmentar cuerpos de agua (ríos, lagos, inundaciones) en imágenes satelitales. El reto es diferenciar agua de sombras o superficies oscuras.

**ML aplicado:**  
- Segmentación semántica  

**Input:**  
- Imágenes satelitales multiespectrales  

**Output:**  
- Mapas de cuerpos de agua  

**Valor:**  
- Gestión de recursos hídricos  
- Prevención de desastres  

**Cómo se aplica a Colombia y Medellín:**  
- Medellín tiene riesgo de inundaciones  
- Importante para gestión del río Medellín  
- Útil para planeación urbana  

---

## 6. Detección de carreteras

**Tipo de dato:**  
Líneas (derivadas de imágenes raster)

**Problema:**  
Extraer automáticamente la red vial a partir de imágenes satelitales. El reto es detectar carreteras en diferentes condiciones (urbanas, rurales, cubiertas).

**ML aplicado:**  
- Segmentación  
- Post-procesamiento (vectorización)

**Input:**  
- Imágenes satelitales  
- Datos de referencia (OpenStreetMap)

**Output:**  
- Red de carreteras (grafo)

**Valor:**  
- Logística  
- Mapas  
- Transporte  

**Cómo se aplica a Colombia y Medellín:**  
- Infraestructura vial en constante cambio  
- Útil para apps de movilidad  
- Aplicable a zonas rurales poco mapeadas  

---

## 7. Identificación de zonas de riesgo (deslizamientos)

**Tipo de dato:**  
Áreas (superficies)

**Problema:**  
Detectar zonas propensas a deslizamientos usando variables geográficas como pendiente, lluvia y cobertura vegetal. El reto es integrar múltiples fuentes de datos.

**ML aplicado:**  
- Clasificación supervisada  
- Modelos geoespaciales  

**Input:**  
- DEM (elevación)  
- Imágenes satelitales  
- Datos climáticos  

**Output:**  
- Mapa de riesgo  

**Valor:**  
- Prevención de desastres  
- Planeación urbana  

**Cómo se aplica a Colombia y Medellín:**  
- Medellín tiene alto riesgo de deslizamientos  
- Aplicable a zonas de ladera  
- Muy relevante para políticas públicas  

---

## 8. Conteo de objetos (vehículos, casas)

**Tipo de dato:**  
Puntos

**Problema:**  
Detectar y contar objetos en imágenes satelitales (vehículos, edificaciones). El reto es la resolución y la variabilidad visual.

**ML aplicado:**  
- Object detection (YOLO, Faster R-CNN)

**Input:**  
- Imágenes satelitales  

**Output:**  
- Coordenadas de objetos  
- Conteo total  

**Valor:**  
- Análisis urbano  
- Tráfico  
- Densidad poblacional  

**Cómo se aplica a Colombia y Medellín:**  
- Tráfico en Medellín  
- Análisis de parqueaderos  
- Planeación urbana  

---

## 9. Clasificación de tipo de vivienda (casas vs apartamentos)

**Tipo de dato:**  
Áreas (polígonos), puntos (centroides), superficies (zonas)

**Problema:**  
Clasificar edificaciones en casas o apartamentos usando su geometría, altura y contexto espacial. El reto es que visualmente pueden ser similares, por lo que se requiere incorporar información espacial (densidad, vecindad, patrones urbanos).

**ML aplicado:**  
- Random Forest / XGBoost (features geoespaciales)  
- CNN (imágenes satelitales)  
- Posible extensión: Graph Neural Networks  

**Input:**  
- Footprints de edificios  
- Imágenes satelitales  
- Datos de altura (cuando existan)  
- Features espaciales (densidad, distancia, vecindad)

**Output:**  
- Clasificación por edificio  
- Mapas por zonas (% casas vs apartamentos)

**Valor:**  
- Análisis inmobiliario  
- Planeación urbana  
- Alto potencial comercial (proptech)

**Cómo se aplica a Colombia y Medellín:**  
- Medellín tiene mezcla de casas y edificios  
- Útil para identificar zonas de valorización  
- Aplicable a inversión inmobiliaria  
- Posible extensión a detección de conjuntos residenciales  

---