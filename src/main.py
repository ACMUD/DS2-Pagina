import streamlit as st

from pages import Introduction, Modelos, MongoDB


pages = {
    "Introduccion": [
        st.Page(Introduction, title="Introducción")
    ],
    "MongoDB": [
        st.Page(MongoDB, title="MongoDB"),
    ],
    "Modelos Matemáticos": [
        st.Page(Modelos, title="Modelos matemáticos"),
    ]
}
pg = st.navigation(pages)

pg.run()