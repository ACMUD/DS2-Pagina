import streamlit as st

from pages import Introduction, Modelos, MongoDB, MongoShell


pages = {
    "Introduccion": [
        st.Page(Introduction, title="Introducción")
    ],
    "MongoDB": [
        st.Page(MongoDB, title="Mongodb instalación"),
        st.Page(MongoShell, title="Mongo shell")
    ],
    "Modelos Matemáticos": [
        st.Page(Modelos, title="Modelos matemáticos"),
    ]
}
pg = st.navigation(pages)

pg.run()