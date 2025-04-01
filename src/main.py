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
    ]
}
pg = st.navigation(pages)

pg.run()