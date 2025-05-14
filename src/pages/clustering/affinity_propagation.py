import streamlit as st
from components.link import CLink_icon, CLink
from sklearn.datasets import make_blobs
from sklearn.cluster import AffinityPropagation as AP
import altair as alt
import pandas as pd
import time

def AffinityPropagation():
    st.title("Affinity Propagation")
    st.write("""
             Affinity propagation (AP) es un algoritmo que gestiona automaticamente los centros o clusters generados, en el cual cada punto interactua enviando mensajes para formar grupos, en el cual se elige en cada iteración un punto representativo.
             
             La idea central es que en cada paso se comunicaran puntos para decidir cual va a ser el centro o representante del grupo esto se hace mediante matrices de similitud y de responsabilidad, luego se verifica la disponibilidad y se actualizan las matrices, finalmente se verifica si se logró la convergencia.
             
             1. Calcular matriz de similitud
             2. Calcular matriz de responsabilidad
             3. Calcular matriz de disponibilidad
             4. Actualizar matrices
             5. Verificar convergencia
             6. Repetir paso 1-5
             """)
    
    st.header("Ejemplo con sklearn")
    st.write("""
             """)
    CLink("sklearn","https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg")
    
    
    st.code("""
            import matplotlib.pyplot as plt
            from sklearn.datasets import make_blobs
            X, y = make_blobs(n_samples=1000, centers=4, random_state=42)
            plt.scatter(X[:, 0], X[:, 1], alpha=0.5)
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
    clin = st.number_input(
        "Numero de grupos",
        min_value=1,
        max_value=5,
        value=4,
        on_change=lambda: dataset_reload(dataset, clin))
    
    dataset = st.empty()
    dataset_reload(dataset, clin)
    
    st.code("""
            from sklearn.cluster import AffinityPropagation
            AP = AffinityPropagation(random_state=1).fit(X)
            """)
    
    col1, col2 = st.columns(2)
    exe = col1.button("Ejecutar")
    cont_km = st.container(height=380)
    if exe:
        ap = AP(random_state=1).fit(X)
        Y=ap.predict(X)
        df["type"]=Y
        
        cont_km.altair_chart(
            alt.Chart(df).mark_circle().encode(
                x=alt.X('x', axis=alt.Axis(title='x_1')),
                y=alt.Y('y', axis=alt.Axis(title='x_2')),
                color="type",
            )
        )