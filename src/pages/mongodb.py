import streamlit as st

def MongoDB():
    st.title("MongoDB")
    col1, col2 = st.columns([.7,.3])
    col1.write("Mongo db es una base de datos no relacional muy util para multiples\
            propósitos, entre ellos el almacenamiento de grandes volumenes de datos no estructurados\
             para su posterior limpieza y analisis, es una gran opción para usar como datalake.")
    col2.write("""
             <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mongodb/mongodb-original-wordmark.svg" height="120px"/>
             """, unsafe_allow_html=True)
    
    st.header("Instalación y uso")
    
    st.link_button("Atlas", "https://cloud.mongodb.com/", icon=":material/open_in_new:")
    st.write("Se recomienda trabajarlo mediante Atlas, aunque tambien se puede ejecutar mongo en local con ayuda de Docker o Podman")
    st.code("docker run -p 27017:27017 -n database mongo")
    st.write("El puerto por defecto es 27017, si se quiere usar en otro puerto se puede usar la bandera ``-p`` y luego ``<puerto del equipo local>:<puerto del contenedor>``\
        luego bastará con utilizar la url ``mongodb://<ip del contenedor>:<puerto del contenedor>`` para conectarse a la base de datos.")
    st.code("""
            mongodb+srv://<db_user>:<db_password>@<cluster>/?retryWrites=true&w=majority&appName=<database>
            mongodb://<ip del contenedor>:<puerto del contenedor>""",
            language="none")