import streamlit as st

from pages import Introduction, Modelos

pg = st.navigation([Introduction, Modelos])

pg.run()