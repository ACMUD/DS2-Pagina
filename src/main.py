import streamlit as st

from pages import Introduction, Modelos


pages = {
    "Introduccion": [
        st.Page(Introduction, title="Introducción")
    ],
    "Modelos Matemáticos": [
        st.Page(Modelos, title="Modelos matemáticos"),
    ]
}
pg = st.navigation(pages)

pg.run()