import streamlit as st
import numpy as np
import pandas as pd

def Clustering():
    st.title("Clustering")
    st.write("""
             La agrupación o clustering es un proceso de aprendizaje automático no supervisado para identificar grupos que contengan información similar.
             
             Los grupos pueden dar información como por ejemplo el tipo de cliente, que caracteristicas diferencian a un grupo de otros, o que productos son más vendidos por un grupo de otro.
             """)

    tmp1 = np.random.randint(1,50,50)
    tmp2 = np.random.randint(50,100,50)
    df = pd.DataFrame({
            "x": np.block([tmp1, tmp2]),
            "y": np.block([np.random.rand(50)*300+500, np.random.rand(50)*300]),
            "type": ["A"]*50+["B"]*50
        })
    st.scatter_chart(
        df,
        x="x",
        y="y"
    )
    
    st.write("""
             Para separar estos grupos se pueden colorear
             """)
    st.scatter_chart(
        df,
        x="x",
        y="y",
        color="type"
    )
    
    st.write("""
             Pero no siempre son tan faciles de identificar, por lo cual existen algoritmos que permiten identificar estos grupos.
             """)