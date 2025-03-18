import streamlit as st
from components.link import CLink

tools = [
    ["Scikit-learn",
        "",
        "scikitlearn/scikitlearn-original.svg"],
    ["Pandas",
        "",
        "pandas/pandas-original.svg"],
    ["Matplotlib",
        "",
        "matplotlib/matplotlib-original.svg"],
]

def Modelos():
    st.markdown("# Modelos Matemáticos e Indicadores en Data Science")

    st.divider()
    st.markdown("## Introducción:")
    st.markdown("### Definición de modelos matemáticos en Data Science")
    st.write("Los modelos matemáticos son una representación simplificada de un sistema real, que se utiliza para estudiar el comportamiento del sistema o para hacer predicciones sobre su comportamiento futuro. En el contexto de la ciencia de datos, los modelos matemáticos se utilizan para analizar y predecir el comportamiento de los datos, y para tomar decisiones basadas en esos análisis.")
    st.markdown("### Importancia de los indicadores en la toma de decisiones basada en datos.")
    st.write("Los indicadores son medidas cuantitativas que se utilizan para evaluar el desempeño de un sistema o para medir el impacto de una intervención. En el contexto de la ciencia de datos, los indicadores se utilizan para evaluar la calidad de los datos, para medir el rendimiento de los modelos matemáticos y para evaluar el impacto de las decisiones basadas en datos.")
    st.markdown("### Aplicaciones en distintos dominios (negocios, salud, finanzas, seguridad, etc.).")
    st.write()

    st.divider()
    st.markdown("## Fundamentos de Modelos Matemáticos:")

    st.markdown("### Álgebra Lineal")
    st.write("Vectores y matrices en la manipulación de datos.")
    st.write("Operaciones con matrices: multiplicación, inversa y descomposiciones.")
    st.write("Aplicaciones en Machine Learning (ejemplo: regresión lineal).")

    st.markdown("### Cálculo y Optimización")
    st.write("Derivadas y gradientes en el ajuste de modelos.")
    st.write("Descenso del gradiente y optimización de funciones de costo.")
    st.write("Regularización (L1, L2) para evitar sobreajuste.")
    
    st.markdown("### Probabilidad y Estadística")
    st.write("Distribuciones de probabilidad y sus aplicaciones.")
    st.write("Inferencia estadística y prueba de hipótesis.")
    st.write("Intervalos de confianza y p-valor.")
    
    st.divider()
    st.markdown("## Indicadores Clave en Data Science:")

    st.markdown("### Métricas de Desempeño de Modelos")
    st.write("Regresión: MSE, RMSE, R², MAE.")
    st.write("Clasificación: Precisión, Recall, F1-score, Curva ROC-AUC.")
    st.write("Agrupación: Inercia, Silhouette Score, Coeficiente de Rand.")

    st.markdown("### Indicadores de Calidad de Datos")
    st.write("Valores faltantes y su impacto en los modelos.")
    st.write("Detección de valores atípicos.")
    st.write("Distribución y sesgo de los datos.")
    
    st.markdown("### Indicadores de Negocio y Análisis Exploratorio")
    st.write("KPI’s en diferentes industrias.")
    st.write("Visualización de tendencias y correlaciones.")
    st.write("Interpretación de resultados para la toma de decisiones.")

    st.divider()
    st.markdown("## Implementación en Python:")

    st.markdown("### Cálculo de métricas con scikit-learn y statsmodels")
    st.markdown("### Optimización de modelos con scipy.optimize")
    st.markdown("### Análisis estadístico con pandas, matplotlib y seaborn")

    layout = st.columns(4)
    for i in range(len(tools)):
        with layout[i%len(layout)]:
            tools[i][2] = 'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/'+ tools[i][2]
            CLink(*tools[i])

    st.divider()
    st.markdown("## Casos Prácticos:")

    st.markdown("### Predicción de ventas con regresión lineal")
    st.link_button("Kaggle: Predicción de ventas de tiendas", "https://www.kaggle.com/competitions/regresion-lineal")
    st.markdown("### Clasificación de clientes con métricas de desempeño.")
    st.markdown("### Análisis de series de tiempo y métricas de tendencia.")
    st.link_button("Kaggle: Formula 1 World Championship", "https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020")

    

    