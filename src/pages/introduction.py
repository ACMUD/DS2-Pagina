import streamlit as st
from components.link import CLink
import requests

tools = [
    ["Python",
    "https://www.python.org/",
    "python/python-original.svg"],
    ["Jupyter",
    "https://jupyter.org/",
    "jupyter/jupyter-original-wordmark.svg"],
    ["Podman",
        "https://podman.io/",
        "podman/podman-original.svg"],
    ["Docker",
        "https://www.docker.com/",
        "docker/docker-original-wordmark.svg"],
    ["MongoDB",
        "https://www.mongodb.com/",
        "mongodb/mongodb-original.svg"]
]

frameworks = [
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

def Introduction():
    st.title("Introduction a la ciencia de datos")
    st.write("""
             El curso de ciencia de datos está centrado en como gestionar los datos,\
             las estructuras para almacenarlos y como utilizarlos para construir \
             modelos que permitan predecir y clasificar nuevos conjuntos de datos utilizando python.
             """)
    
    st.header("Tecnologías y herramientas")
    st.write("Las herramientas utilizadas para este curso son:")
    layout = st.columns(4)
    for i in range(len(tools)):
        with layout[i%len(layout)]:
            tools[i][2] = 'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/'+ tools[i][2]
            CLink(*tools[i])

    st.divider()
    st.write("Los Frameworks y librerias utilizadas son:")
    layout = st.columns(4)
    for i in range(len(frameworks)):
        with layout[i%len(layout)]:
            frameworks[i][2] = 'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/'+ frameworks[i][2]
            CLink(*frameworks[i])
    
    