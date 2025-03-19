import streamlit as st
import pandas as pd
import numpy as np


df = pd.DataFrame(
            {
                "x": np.random.randint(1,25,15),
                "y": np.random.randint(1,25,15)
                }
            )

def Pipeline():
    st.title("Pipelines")
    st.write("""
             Un pipeline es una secuencia de pasos para procesar datos para cualquier proposito, por ejemplo preprocesado, modelado, evaluación y transformación.
             
             De modo que automatiza el proceso para nuevos datos.
             """)
    
    st.latex(r"X \rightarrow f(X)")
    
    st.write("Supongamos el siguiente dataset")
    st.code("""
            import pandas as pd
            df = pd.read_csv('data.csv')
            """)
    tmp = st.data_editor(
        df
        )
    
    st.write("se puede hacer la operación de media sobre las filas y agregarla al dataframe")
    
    st.code("""
    tmp = df.copy()
    tmp.loc[:,'Media'] = tmp.mean(axis=1) 
    """)
    
    tmp.loc[:,'Media'] = tmp.mean(axis=1)
    st.dataframe(tmp)
    with st.spinner("Espere un momento", show_time=True):
        st.scatter_chart(tmp, x = 'x', y = 'y', size = 'Media')
    
    st.write("""
             Sin embargo, ¿como se podria hacer para que todos los datos que vengan de una fuente se procesen?.
             
             Una forma puede ser utilizando funciones, por ejemplo:
             """)
    
    st.code("""
            def process(data: pd.dataframe) -> pd.dataframe:
                data.loc[:,'Media'] = data.mean(axis=1)
                return data
            """)
    st.write("Y por lo tanto conforme se van cargando los datos se procesan")
    st.code("""
            if data:
                df = process(data)
                save(df)
            """)