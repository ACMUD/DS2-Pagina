import streamlit as st
from components.link import CLink

def MongoDB():
    st.title("MongoDB")
    col1, col2 = st.columns([.7,.3])
    col1.write("Mongo db es una base de datos no relacional basada en documentos muy util para multiples\
            propósitos, entre ellos el almacenamiento de grandes volumenes de datos no estructurados\
             para su posterior limpieza y analisis, es una gran opción para usar como datalake.")
    col1.write("""En mongo lo equivalente a tablas en sql son colecciones, las cuales almacenan documentos
               Estas se crean de forma automatica al momento de agregar documentos.""")
    col2.write("""
             <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mongodb/mongodb-original-wordmark.svg" height="120px"/>
             """, unsafe_allow_html=True)
    
    CLink("MongoDB", "https://www.mongodb.com/", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mongodb/mongodb-original.svg")
    st.link_button("Atlas", "https://cloud.mongodb.com/", icon=":material/open_in_new:")
    
    st.subheader("bson")
    col1, col2 = st.columns(2)
    col2.write("Bson es el formato utilizado por mongodb, es muy parecido a json pero agrega algunos tipos de dato adicional, como `datetime` y `ObjectId`,\
        a parte de que es mucho más rápido que json.")
    col1.json({
        "id_": "67da0589ef681528996b140c",
        "pelicula": "Star wars",
        "etiquetas": ["ciencia ficción", "acción"]
    })
    
    st.header("Instalación y uso")
    
    
    st.write("Se recomienda trabajarlo mediante Atlas, aunque tambien se puede ejecutar mongo en local con ayuda de Docker o Podman")
    st.code("""
            docker pull mongo
            docker run -p 27017:27017 --name database mongo
            """)
    st.write("El puerto por defecto es 27017, si se quiere usar en otro puerto se puede usar la bandera ``-p`` y luego ``<puerto del equipo local>:<puerto del contenedor>``\
        luego bastará con utilizar la url ``mongodb://<host>:<puerto>`` para conectarse a la base de datos.")
    st.code("""
            mongodb+srv://<db_user>:<db_password>@<cluster>/?retryWrites=true&w=majority&appName=<database>
            mongodb://<host>:<puerto>""",
            language="none")
