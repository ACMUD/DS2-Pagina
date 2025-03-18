import streamlit as st

from pages import Introduction

pg = st.navigation([Introduction])

pg.run()