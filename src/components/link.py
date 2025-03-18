import streamlit as st
def CLink_icon(text:str, href:str, icon:str):
    st.write(f"""
             <div class="st-emotion-cache-ogrf2x e11mkfd22">
                <a href="{href}" style="text-decoration:none; color:white;">
                <i class="{icon}" style="margin-right: 10px"></i>
                <span>
                {text}
                <span/>
                </a>
             <div/>
             """, unsafe_allow_html=True)

import streamlit as st
def CLink(text:str, href:str, icon:str):
    st.write(f"""
             <div class="st-emotion-cache-ogrf2x e11mkfd22" style="padding:1em;">
                <a href="{href}" style="text-decoration:none; color:white;" ><img src="{icon}" width="20px" style="margin-right: 10px" />{text}</a>
             <div/>
             """, unsafe_allow_html=True)