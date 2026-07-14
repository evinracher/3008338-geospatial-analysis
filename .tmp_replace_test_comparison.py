import json
from pathlib import Path


notebook_path = Path("project/house-price-medellin.ipynb")
notebook = json.loads(notebook_path.read_text())
cells = notebook["cells"]


def markdown_cell(source):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source.splitlines(keepends=True),
    }


def code_cell(source):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source.splitlines(keepends=True),
    }


replacement_cells = [
    markdown_cell(
        """## Comparación de todos los modelos en el conjunto de prueba

La comparación anterior mezclaba el ajuste de OLS, SEM y SAR-Lag sobre toda la muestra con la predicción de Random Forest y XGBoost sobre datos de prueba. Para obtener métricas comparables, los tres modelos estadísticos se entrenan nuevamente utilizando solo el conjunto de entrenamiento. Los cinco modelos se evalúan después sobre las mismas 10.745 viviendas de prueba y con `log_price` como variable objetivo.

El preprocesamiento también se ajusta exclusivamente con entrenamiento. De esta forma, la imputación, estandarización y codificación categórica no utilizan información del conjunto de prueba."""
    ),
    markdown_cell(
        """### Preparación espacial de entrenamiento y prueba

Se construye una matriz KNN con 20 vecinos para cada conjunto. Ambas matrices representan el mismo criterio de vecindad, pero utilizan solamente las ubicaciones disponibles en su partición."""
    ),
    code_cell(
        """from sklearn.base import clone

comparison_preprocessor = clone(ols_preprocessor)
comparison_train_x = comparison_preprocessor.fit_transform(
    train_set[ols_features]
).astype(float)
comparison_test_x = comparison_preprocessor.transform(
    test_set[ols_features]
).astype(float)

comparison_train_y = np.log(train_set["price"].to_numpy()).reshape(-1, 1)
comparison_test_y = np.log(test_set["price"].to_numpy())
comparison_feature_names = comparison_preprocessor.get_feature_names_out().tolist()

comparison_train_gdf = gpd.GeoDataFrame(
    train_set.copy(),
    geometry=gpd.points_from_xy(train_set["lon"], train_set["lat"]),
    crs="EPSG:4326",
).to_crs(epsg=9377).reset_index(drop=True)

comparison_test_gdf = gpd.GeoDataFrame(
    test_set.copy(),
    geometry=gpd.points_from_xy(test_set["lon"], test_set["lat"]),
    crs="EPSG:4326",
).to_crs(epsg=9377).reset_index(drop=True)

comparison_train_weights = KNN.from_dataframe(
    comparison_train_gdf,
    k=20,
    use_index=True,
)
comparison_test_weights = KNN.from_dataframe(
    comparison_test_gdf,
    k=20,
    use_index=True,
)
comparison_train_weights.transform = "R"
comparison_test_weights.transform = "R"

print(f"Observaciones de entrenamiento: {len(comparison_train_gdf)}")
print(f"Observaciones de prueba: {len(comparison_test_gdf)}")
print(
    "Componentes KNN de entrenamiento y prueba:",
    comparison_train_weights.n_components,
    comparison_test_weights.n_components,
)"""
    ),
    markdown_cell(
        """### Entrenamiento de OLS, SEM y SAR-Lag

Los modelos se ajustan con la misma matriz de variables y las mismas observaciones de entrenamiento. Los parámetros espaciales se estiman a partir de la red KNN de entrenamiento."""
    ),
    code_cell(
        """comparison_ols_model = spreg.OLS(
    comparison_train_y,
    comparison_train_x,
    name_y="Precio logarítmico",
    name_x=comparison_feature_names,
)
comparison_sem_model = spreg.GM_Error_Het(
    comparison_train_y,
    comparison_train_x,
    w=comparison_train_weights,
    name_y="Precio logarítmico",
    name_x=comparison_feature_names,
    name_w="KNN de entrenamiento con 20 vecinos",
)
comparison_sar_lag_model = spreg.GM_Lag(
    comparison_train_y,
    comparison_train_x,
    w=comparison_train_weights,
    name_y="Precio logarítmico",
    name_x=comparison_feature_names,
    name_w="KNN de entrenamiento con 20 vecinos",
)

comparison_spatial_parameters = pd.DataFrame(
    {
        "Modelo": ["SEM", "SAR-Lag"],
        "Parámetro": ["λ", "ρ"],
        "Estimación": [
            comparison_sem_model.betas[-1, 0],
            comparison_sar_lag_model.betas[-1, 0],
        ],
        "Valor p": [
            format_analytical_p_value(comparison_sem_model.z_stat[-1][1]),
            format_analytical_p_value(comparison_sar_lag_model.z_stat[-1][1]),
        ],
    }
)
comparison_spatial_parameters.round(4)"""
    ),
    markdown_cell(
        """### Predicción sobre el conjunto de prueba

OLS y SEM predicen la parte sistemática $X\beta$. En SEM, el componente espacial pertenece al error y no puede predecirse en una ubicación nueva sin observar errores cercanos.

SAR-Lag se predice mediante su forma reducida:

$$
\hat y=(I-\hat\rho W_{test})^{-1}X_{test}\hat\beta
$$

Esta expresión incorpora la retroalimentación espacial entre las ubicaciones de prueba, pero no utiliza sus precios reales."""
    ),
    code_cell(
        """from scipy.sparse import identity
from scipy.sparse.linalg import spsolve

comparison_test_x_constant = np.column_stack(
    [np.ones(comparison_test_x.shape[0]), comparison_test_x]
)

ols_test_log_prediction = (
    comparison_test_x_constant @ comparison_ols_model.betas.flatten()
)
sem_test_log_prediction = (
    comparison_test_x_constant @ comparison_sem_model.betas[:-1].flatten()
)

sar_lag_rho = comparison_sar_lag_model.betas[-1, 0]
sar_lag_linear_prediction = (
    comparison_test_x_constant @ comparison_sar_lag_model.betas[:-1].flatten()
)
sar_lag_test_log_prediction = spsolve(
    identity(len(comparison_test_y), format="csr")
    - sar_lag_rho * comparison_test_weights.sparse,
    sar_lag_linear_prediction,
)

random_forest_test_log_prediction = np.log(
    np.clip(y_pred_test_best_random_forest, a_min=1, a_max=None)
)
xgboost_test_log_prediction = np.log(
    np.clip(y_pred_test_best_xgboost, a_min=1, a_max=None)
)

test_log_predictions = {
    "OLS": ols_test_log_prediction,
    "SEM": sem_test_log_prediction,
    "SAR-Lag": sar_lag_test_log_prediction,
    "Random Forest": random_forest_test_log_prediction,
    "XGBoost": xgboost_test_log_prediction,
}"""
    ),
    markdown_cell(
        """### Métricas comparables en prueba

Todos los modelos se evalúan con R², MAE y RMSE sobre `log_price`. También se calcula el I de Moran de sus residuos usando la misma matriz KNN de prueba. En esta tabla, una diferencia de desempeño corresponde al modelo y no a una muestra de evaluación diferente."""
    ),
    code_cell(
        """np.random.seed(42)
test_comparison_rows = []
test_residual_moran = {}

for model_name, prediction in test_log_predictions.items():
    residual = comparison_test_y - prediction
    moran = Moran(
        residual,
        comparison_test_weights,
        permutations=999,
    )
    test_residual_moran[model_name] = moran
    test_comparison_rows.append(
        {
            "Modelo": model_name,
            "R² log_price": r2_score(comparison_test_y, prediction),
            "MAE log_price": mean_absolute_error(comparison_test_y, prediction),
            "RMSE log_price": np.sqrt(
                mean_squared_error(comparison_test_y, prediction)
            ),
            "I de Moran residual": moran.I,
            "Valor p de Moran": moran.p_sim,
        }
    )

test_model_comparison = pd.DataFrame(test_comparison_rows)
test_model_comparison_display = test_model_comparison.copy()
test_model_comparison_display["Valor p de Moran"] = (
    test_model_comparison_display["Valor p de Moran"].map(
        lambda value: f"{value:.3f}"
    )
)
test_model_comparison_display.round(4)"""
    ),
    markdown_cell(
        """## Visualización de la comparación en prueba"""
    ),
    code_cell(
        """figure, axes = plt.subplots(1, 2, figsize=(14, 5))

test_model_comparison.plot.bar(
    x="Modelo",
    y="R² log_price",
    color=["#9E9E9E", "#1976D2", "#EF6C00", "#388E3C", "#7B1FA2"],
    legend=False,
    ax=axes[0],
)
axes[0].set_title("R² sobre el conjunto de prueba")
axes[0].set_xlabel("Modelo")
axes[0].set_ylabel("R² de log_price")
axes[0].tick_params(axis="x", rotation=30)

test_model_comparison.plot.bar(
    x="Modelo",
    y="RMSE log_price",
    color=["#9E9E9E", "#1976D2", "#EF6C00", "#388E3C", "#7B1FA2"],
    legend=False,
    ax=axes[1],
)
axes[1].set_title("RMSE sobre el conjunto de prueba")
axes[1].set_xlabel("Modelo")
axes[1].set_ylabel("RMSE de log_price")
axes[1].tick_params(axis="x", rotation=30)

plt.tight_layout()
plt.show()"""
    ),
    code_cell(
        """figure, axis = plt.subplots(figsize=(9, 5))
test_model_comparison.plot.bar(
    x="Modelo",
    y="I de Moran residual",
    color=["#9E9E9E", "#1976D2", "#EF6C00", "#388E3C", "#7B1FA2"],
    legend=False,
    ax=axis,
)
axis.axhline(0, color="black", linewidth=0.8)
axis.set_title("Autocorrelación residual en el conjunto de prueba")
axis.set_xlabel("Modelo")
axis.set_ylabel("I de Moran")
axis.tick_params(axis="x", rotation=30)
plt.tight_layout()
plt.show()"""
    ),
    code_cell(
        """figure, axes = plt.subplots(2, 3, figsize=(18, 11))
axes = axes.flatten()
plot_minimum = min(
    comparison_test_y.min(),
    *(prediction.min() for prediction in test_log_predictions.values()),
)
plot_maximum = max(
    comparison_test_y.max(),
    *(prediction.max() for prediction in test_log_predictions.values()),
)

for axis, (model_name, prediction) in zip(axes, test_log_predictions.items()):
    axis.scatter(comparison_test_y, prediction, alpha=0.10, s=8)
    axis.plot(
        [plot_minimum, plot_maximum],
        [plot_minimum, plot_maximum],
        color="red",
        linestyle="--",
    )
    axis.set_title(f"Observado frente a {model_name}")
    axis.set_xlabel("log_price observado")
    axis.set_ylabel("log_price predicho")

axes[-1].axis("off")
plt.tight_layout()
plt.show()"""
    ),
    markdown_cell(
        """## Interpretación de la comparación en prueba

La evaluación homogénea confirma que Random Forest es el mejor predictor: obtiene R² = 0.7767 y RMSE = 0.3477. Además, presenta la menor autocorrelación residual, con I de Moran = 0.0296. Aunque este valor es significativo (`p = 0.001`), su magnitud es muy baja.

Entre los modelos estadísticos, SAR-Lag obtiene el mejor resultado de prueba, con R² = 0.5997 y RMSE = 0.4655. Supera a OLS, que obtiene R² = 0.5828 y RMSE = 0.4752, y a SEM, con R² = 0.5649 y RMSE = 0.4853. Esto indica que el rezago del precio aporta información predictiva adicional.

SEM presenta el menor desempeño predictivo entre los tres modelos estadísticos y deja I de Moran = 0.2437 en prueba. Esto no contradice el diagnóstico anterior: SEM logra filtrar la dependencia de los errores observados durante el ajuste, pero ese error espacial no puede anticiparse para viviendas nuevas usando solamente sus atributos. Por eso SEM es útil para explicar y corregir inferencia espacial, pero no necesariamente para predicción fuera de muestra.

SAR-Lag reduce la autocorrelación residual de prueba a 0.1753, frente a 0.1926 de OLS, aunque todavía queda estructura espacial significativa. XGBoost obtiene R² = 0.5373 y RMSE = 0.5004, por debajo de Random Forest y SAR-Lag.

En conclusión, la comparación sobre una muestra común permite separar claramente los objetivos: Random Forest es el mejor modelo predictivo, SAR-Lag es el mejor modelo estadístico para predicción y SEM sigue siendo el modelo que mejor representa la dependencia espacial de los errores durante el ajuste."""
    ),
]


start_index = next(
    index
    for index, cell in enumerate(cells)
    if "".join(cell.get("source", [])).strip().startswith(
        "## Comparación de los modelos estadísticos"
    )
)
end_index = next(
    index
    for index, cell in enumerate(cells)
    if "".join(cell.get("source", [])).strip().startswith("# Conclusiones")
)

notebook["cells"] = cells[:start_index] + replacement_cells + cells[end_index:]
notebook_path.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n")
