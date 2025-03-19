import streamlit as st
from PIL import Image
from pages import (
    Introduction, 
    MongoDB,
    MongoShell,
    MongoAggregations,
    MongoPython,
    ODM,

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
    
    Pipeline
    
)

pages = {
    "Introduccion": [
        st.Page(Introduction, title="Introducción")
    ],
    "MongoDB": [
        st.Page(MongoDB, title="Mongodb instalación", icon=":material/database:"),
        st.Page(MongoShell, title="Mongo shell", icon=":material/terminal:"),
        st.Page(MongoAggregations, title="Agregaciones", icon=":material/flowchart:"),
        st.Page(MongoPython, title="Mongo con python", icon=":material/code:"),
        st.Page(ODM, title="uso de ODM (Object Document Mapper)", icon=":material/code:")
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
        st.Page(Pipeline, title="Pipelines")
    ]
}


st.write("""
        <style>
        .stLogo {
            height:6em !important;
            margin-left: 1em;
        }
        </style>
         """, unsafe_allow_html=True)


st.logo(
    image = Image.open("./src/static/logo.png"),
    icon_image = Image.open("./src/static/logo.png"),
    size = "large",
)

pg = st.navigation(pages)

pg.run()