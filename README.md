# Análisis Geoespacial

# TRABAJO FINAL

# Presentación:

La presentación en este enlace:

https://gamma.app/docs/analisis-geoespacial-presentacion-final-6gmerex0vtd7msk

También se encuentra en el repositorio en formato PDF.

# Trabajo escrito:

El trabajo escrito (artículo) se encuentra en la carpeta [article](https://github.com/evinracher/3008338-geospatial-analysis/tree/main/article)

# Dataset

El dataset está disponible en este enlace:

https://www.kaggle.com/datasets/julianusugaortiz/colombia-housing-properties-price

Se le realizará las transformaciones pertinentes para el problemas. No se sube en el github por restricción de tamaño del archivo.


## Course Information

| Field | Detail |
|---|---|
| **Program** | Specialization in Artificial Intelligence |
| **SNIES Code** | 108149 |
| **University** | Universidad Nacional de Colombia |
| **Faculty** | Facultad de Minas |
| **Course Name** | Análisis Geoespacial |
| **Course Code (SIA)** | 3008338 |

---

## Repository Purpose

This repository contains the exercises, course materials, and final project developed for the Geospatial Analysis course. The main project investigates the question: **How is the geographic location of a home in Medellín related to its price?** It combines property characteristics with point locations, neighborhood boundaries, spatial dependence, spatial heterogeneity, hierarchical effects, and continuous spatial prediction.

### Learning Objectives

- Understand the characteristics, models, and structures of spatial data.
- Distinguish and analyze spatial dependence and spatial heterogeneity.
- Set up computational workflows for geospatial analysis using Python, Jupyter, Google Earth Engine, and GitHub.
- Create and interpret web maps and geospatial visualizations.
- Apply point-pattern analysis methods, including centrography, convex hulls, density estimation, and nearest-neighbor analysis.
- Conduct exploratory spatial data analysis using spatial weights, spatial autocorrelation, and thematic maps.
- Apply regression models for spatial dependence and spatial heterogeneity.
- Analyze continuous spatial data through raster methods, geostatistics, and Gaussian processes.

### Academic Scope

The repository is practical and research-oriented. Its central workflow is implemented in Python and follows the spatial methods presented in the course book and lectures. The final deliverables include the analysis notebook, presentation materials, a written article, generated figures, supporting notes, and reproducible exercises.

---

## Content Overview

### Main Topics

- Housing-data cleaning, preprocessing, and exploratory analysis
- Point geometries, neighborhood polygons, spatial joins, and CRS transformations
- Marked point patterns, centrography, normalized kernel surfaces, and spatial K-means
- Queen and K-nearest-neighbor spatial weights
- Global Moran's I and Local Indicators of Spatial Association (LISA)
- Hedonic OLS, Spatial Error Models (SEM), and Spatial Lag Models (SAR-Lag)
- Geographically Weighted Regression (GWR) and Multiscale GWR (MGWR)
- Hierarchical models with neighborhood-level random effects
- Ordinary Kriging, Regression-Kriging, and Gaussian process regression
- Random Forest and XGBoost price prediction

### Types of Artifacts

- Jupyter notebooks for the final project, examples, and exercises
- A processed Medellín housing dataset and course geospatial data
- Course notes, guides, and the course book
- A final article in LaTeX and PDF formats
- Presentation files and project documentation
- Maps, diagnostic plots, model comparisons, and prediction surfaces

### Repository Structure

```
ANALISIS_GEOESPACIAL/
├── README.md
├── project/
│   ├── house-price-medellin.ipynb
│   ├── dataset/final_dataset.csv
│   ├── documents/
│   └── examples/
├── article/
│   ├── house_price_medellin.tex
│   ├── house_price_medellin.pdf
│   └── figures/
├── exercises/
└── presentacion-3.pdf
```

---

## Key Concepts Implemented

- **Spatial representation:** property coordinates are converted from longitude and latitude in WGS 84 (`EPSG:4326`) to MAGNA-SIRGAS / Origen-Nacional (`EPSG:9377`) for metric distance calculations.
- **Spatial context:** property points are joined to Medellín neighborhood polygons and summarized through choropleth maps.
- **Point-pattern exploration:** marked point maps, mean center, standard deviational ellipse, convex hull, and a normalized kernel price surface describe the geographic distribution of listings.
- **Spatial clustering:** K-means is fitted to projected coordinates, while price is used to characterize the resulting geographic clusters.
- **Spatial weights:** Queen contiguity represents neighborhood adjacency, and row-standardized KNN matrices represent proximity among property listings.
- **Spatial autocorrelation:** global Moran's I measures overall price clustering; LISA identifies High-High, Low-Low, High-Low, and Low-High local patterns.
- **Spatial dependence:** OLS diagnostics and LM tests motivate SEM and SAR-Lag models for omitted spatial factors and neighboring-price effects.
- **Spatial heterogeneity:** GWR and MGWR estimate relationships that vary across Medellín and at different spatial scales.
- **Spatial regimes:** mixed-effects models allow neighborhood-specific intercepts and a varying bathroom-price relationship.
- **Spatial interpolation:** Ordinary Kriging, Regression-Kriging, and Gaussian process regression generate continuous prediction and uncertainty surfaces.

---

## Repository Analysis

The principal implementation is [`project/house-price-medellin.ipynb`](project/house-price-medellin.ipynb). It acquires and prepares Colombian housing listings, focuses the analysis on properties in Medellín, and develops complementary predictive and spatial workflows. The notebook covers data preprocessing, exploratory analysis, spatial representation, model estimation, validation, visualization, and interpretation.

### Packages and Libraries

- **Data processing:** pandas, NumPy, SciPy, and KaggleHub
- **Geospatial analysis:** GeoPandas, Shapely, libpysal, esda, splot, and spreg
- **Spatially varying models:** mgwr and statsmodels
- **Interpolation:** PyKrige and scikit-learn Gaussian processes
- **Machine learning:** scikit-learn and XGBoost
- **Visualization:** Matplotlib and GeoPandas plotting tools

### Techniques and Approaches

- Median imputation, standardization, one-hot encoding, pipelines, cross-validation, and grid search
- Random Forest and XGBoost regression on property attributes and location
- Spatial joins, neighborhood aggregation, marked point analysis, kernel smoothing, and geographic clustering
- Sensitivity analysis for alternative KNN spatial-weight configurations
- Moran's I and LISA for prices and model residuals
- OLS, SEM, SAR-Lag, GWR, MGWR, and mixed-effects regression
- Variogram-based Ordinary Kriging, Regression-Kriging, and Matérn Gaussian processes
- Random train-test evaluation for global models and group-based spatial validation for interpolation

### Methodologies

The project separates prediction, spatial explanation, and interpolation because each addresses a different aspect of the research question. Machine-learning models provide flexible predictive baselines, while OLS supports the diagnosis of spatial effects. SEM represents spatial dependence associated with omitted factors, and SAR-Lag models relationships between values observed at neighboring locations. GWR and MGWR examine whether associations vary across the city and operate at different spatial scales, while hierarchical models represent neighborhood-level variation. Kriging-based methods and Gaussian processes are used for continuous spatial prediction and uncertainty estimation. Model assessment combines conventional validation with spatially structured validation where appropriate.

---

## Technologies and Tools

- **Language:** Python
- **Environment:** Jupyter Notebook or JupyterLab
- **Geospatial stack:** GeoPandas, Shapely, PySAL (`libpysal`, `esda`, `splot`, `spreg`), MGWR, and PyKrige
- **Data science and modeling:** NumPy, pandas, SciPy, statsmodels, scikit-learn, and XGBoost
- **Visualization:** Matplotlib
- **Data access:** KaggleHub
- **Document preparation:** LaTeX

---

## How to Run / Reproduce

### 1. Environment Setup

```bash
# Clone the repository
git clone https://github.com/evinracher/3008338-geospatial-analysis.git
cd 3008338-geospatial-analysis

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
```

### 2. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install jupyter kagglehub pandas numpy scipy matplotlib \
  scikit-learn xgboost geopandas shapely libpysal esda splot spreg \
  mgwr statsmodels pykrige
```

The repository does not currently provide a project-level `requirements.txt`; the command above reflects the imports used by the main notebook. Some geospatial packages may require system-level geospatial dependencies depending on the operating system.

### 3. Run Notebooks

```bash
cd project
jupyter notebook house-price-medellin.ipynb
```

Run the cells sequentially from the `project` directory. The notebook uses the included `project/dataset/final_dataset.csv` for the processed analysis and can also download the original Kaggle dataset through KaggleHub. Medellín's neighborhood boundaries are provided with the course materials.

---

## Skills Demonstrated

- Acquisition, cleaning, and reproducible preprocessing of real-estate listings
- CRS selection, reprojection, spatial joins, and neighborhood aggregation
- Cartographic design and interpretation of point, choropleth, cluster, and uncertainty maps
- Construction and justification of spatial weight matrices
- Global and local spatial autocorrelation analysis
- Diagnosis and modeling of spatial dependence and heterogeneity
- Comparison of machine-learning, spatial regression, hierarchical, and geostatistical models
- Validation using both random holdout samples and spatially separated blocks
- Communication of results through a documented notebook, presentation, and academic article

---

## Academic Disclaimer

> **Disclaimer:**  
> This repository was created for academic purposes. The analysis uses advertised housing prices rather than completed transaction prices and is not designed to estimate causal effects. Some labels, outputs, and documentation are in Spanish because the course was taught in Spanish; this README is provided in English for broader accessibility.

---

## Academic Context

This repository is part of the **Specialization in Artificial Intelligence (SNIES 108149)** at **Universidad Nacional de Colombia – Facultad de Minas**. The project applies the methods taught in the course to a single research problem and prioritizes methodological interpretation, reproducibility, and academic learning over production-level optimization.
