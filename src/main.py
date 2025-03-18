import streamlit as st

from pages import Introduction, MongoDB

pg = st.navigation([Introduction, MongoDB])

pg.run()