import streamlit as st

from pages import (
    Introduction, 
    MongoDB, 

    Modelos_introduccion,
    Modelos_fundamentos,
    Modelos_indicadores,
    Modelos_implementacion,
    Modelos_casos
    
)


pages = {
    "Introduccion": [
        st.Page(Introduction, title="Introducción")
    ],
    "MongoDB": [
        st.Page(MongoDB, title="MongoDB"),
    ],
    "Modelos Matemáticos e Indicadores en Data Science": [
        st.Page(Modelos_introduccion, title="Introducción"),
        st.Page(Modelos_fundamentos, title="Fundamentos"),
        st.Page(Modelos_indicadores, title="Indicadores"),
        st.Page(Modelos_implementacion, title="Implementacion"),
        st.Page(Modelos_casos, title="Casos"),
    ]
}
pg = st.navigation(pages)

pg.run()