import streamlit as st

from pages import (
    Introduction, 
    MongoDB,
    MongoShell,

    Modelos_introduccion,
    Modelos_fundamentos,
    Modelos_indicadores,
    Modelos_implementacion,
    Modelos_casos,

    WebScraping_introduccion,
    WebScraping_fundamentos,
    WebScraping_metodos,
    WebScraping_bloqueos,
    WebScraping_almacenamiento,
    WebScraping_proyectos,
    WebScraping_alternativas,
    WebScraping_buenaspracticas,
    
    Pipeline,
    
    Clustering,
    KMeans,
    AffinityPropagation,
    
    Spark,
    Sparkml
)

pages = {
    "Introduccion": [
        st.Page(Introduction, title="Introducción")
    ],
    "MongoDB": [
        st.Page(MongoDB, title="Mongodb instalación"),
        st.Page(MongoShell, title="Mongo shell")
    ],
    "Modelos Matemáticos e Indicadores en Data Science": [
        st.Page(Modelos_introduccion, title="Introducción"),
        st.Page(Modelos_fundamentos, title="Fundamentos"),
        st.Page(Modelos_indicadores, title="Indicadores"),
        st.Page(Modelos_implementacion, title="Implementación"),
        st.Page(Modelos_casos, title="Casos"),
    ],
    "Web Scrapping": [
        st.Page(WebScraping_introduccion, title="Introducción"),
        st.Page(WebScraping_fundamentos, title="Fundamentos"),
        st.Page(WebScraping_metodos, title="Métodos"),
        st.Page(WebScraping_bloqueos, title="Bloqueos"),
        st.Page(WebScraping_almacenamiento, title="Almacenamiento"),
        st.Page(WebScraping_proyectos, title="Proyectos"),
        st.Page(WebScraping_alternativas, title="Alternativas"),
        st.Page(WebScraping_buenaspracticas, title="Buenas Prácticas"),
    ],
    "Pipeline": [
        st.Page(Pipeline, title="Pipelines", icon=":material/valve:")
    ],
    "Clustering o Agrupación": [
        st.Page(Clustering, title="Clustering", icon=":material/join:"),
        st.Page(KMeans, title="K-Means", icon=":material/workspaces:"),
        st.Page(AffinityPropagation, title="Affinity Propagation", icon = ":material/hub:"),
    ],
    "Frameworks": [
        st.Page(Spark, title="Spark"),
        st.Page(Sparkml, title="SparkML")
    ],
}


st.write("""
        <style>
        .stLogo {
            height:6em !important;
            margin-left: 1em;
        }
        </style>
        <link rel="stylesheet" type='text/css' href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css" />
         """, unsafe_allow_html=True)


st.logo(
    image = Image.open("./src/static/logo.png"),
    icon_image = Image.open("./src/static/logo.png"),
    size = "large",
)

pg = st.navigation(pages)

pg.run()