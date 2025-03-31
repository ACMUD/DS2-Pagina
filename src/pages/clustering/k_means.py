import streamlit as st
from components.link import CLink_icon, CLink
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans as KM
import altair as alt
import pandas as pd

def KMeans():
    st.title("K-Means")
    st.write("""
             K-means es un algoritmo de aprendizaje automatico no supervisado que puede agrupar datos utilizando un proceso de optimizacion iterativa.
             
             Cada grupo se llama cluster, y cada cluster tiene un centroide que representa su posicion media.
             
             El procedimiento es el siguiente:
             1. Se selecciona un centroide inicial de forma aleatorio para cada cluster.
             2. Se asigna cada punto a su cluster mas cercano.
             3. Se calcula el centroide de cada cluster.
             4. Se repiten los pasos del 2 al 3 hasta que no cambien los centroides.
             """)
    CLink_icon("PyGroupIA - kmeans","https://github.com/ACMUD/PyGroupIA/blob/main/Clases/Ciencia%20de%20datos/Clustering.ipynb", "devicon-github-original")
    
    st.header("Ejemplo con sklearn")
    st.write("""
             Sklearn es una libreria de python que contiene varios algoritmos de aprendizaje automatico, con utilidades de procesamiento y selección.
             """)
    CLink("sklearn","https://scikit-learn.org/stable/modules/clustering.html#k-means", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg")
    
    st.code("""
            pip install -U scikit-learn
            """)
    
    st.write("""Con sklearn se puede crear un dataset de prueba con la funcion make_blobs.""")
    
    st.code("""
            import matplotlib.pyplot as plt
            from sklearn.datasets import make_blobs
            X, y = make_blobs(n_samples=1000, centers=4, random_state=42)
            plt.plot(X[:, 0], X[:, 1], alpha=0.5)
            """)

    global X, df
    X = None
    df = None
    
    def dataset_reload(dataset, cl):
        global X, df
        X, y = make_blobs(n_samples=500, centers=cl, random_state=42)
    
        df = pd.DataFrame({
            "x": X[:, 0],
            "y": X[:, 1],
            "type": y
        })
        dataset.altair_chart(
        alt.Chart(df).mark_circle().encode(
            x=alt.X('x', axis=alt.Axis(title='x_1')),
            y=alt.Y('y', axis=alt.Axis(title='x_2')),
            color="type",
        )
    )
    clin = 0
    clin = st.number_input(
        "Numero de clusters",
        min_value=1,
        max_value=5,
        value=4,
        on_change=lambda: dataset_reload(dataset, clin))
    
    dataset = st.empty()
    dataset_reload(dataset, clin)
    
    st.code("""
            from sklearn.cluster import KMeans
            import numpy as np
            
            kmeans = KMeans(n_clusters=4, random_state=1, n_init="auto").fit(X)
            """)
    
    col1, col2 = st.columns(2)
    exe = col1.button("Ejecutar")
    cl = col2.number_input("Numero de clusters", min_value=1, max_value=5, value=4, key="kmeans_clusters")
    cont_km = st.container(height=380)
    if exe:
        kmeans = KM(n_clusters=cl, random_state=1, n_init="auto").fit(X)
        Y=kmeans.predict(X)
        df["type"]=Y
        
        cont_km.altair_chart(
            alt.Chart(df).mark_circle().encode(
                x=alt.X('x', axis=alt.Axis(title='x_1')),
                y=alt.Y('y', axis=alt.Axis(title='x_2')),
                color="type",
            )
        )
    st.write("""
             La unica dificultad que tiene el algoritmo es encontrar el numero de clusters para usar en cada caso, ya que no siempre es trivial.
             """)