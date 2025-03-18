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

def Modelos_implementacion():

    st.markdown("## Implementación en Python:")

    st.markdown("### Cálculo de métricas con scikit-learn y statsmodels")
    st.markdown("### Optimización de modelos con scipy.optimize")
    st.markdown("### Análisis estadístico con pandas, matplotlib y seaborn")

    layout = st.columns(4)
    for i in range(len(tools)):
        with layout[i%len(layout)]:
            tools[i][2] = 'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/'+ tools[i][2]
            CLink(*tools[i])