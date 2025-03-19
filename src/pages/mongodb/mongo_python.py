import streamlit as st

def MongoPython():
    st.title("Mongo con Python")
    st.write("""
             Para manejar cualquier base de datos se suele usar herramientas como ORM, en el caso de mongo ODM. sin embargo,
             primero se puede ver como se hace directamente utilizando la liberia correspondiente.
             """)
    st.header("Pymongo")
    st.link_button("Pymongo", "https://www.mongodb.com/docs/languages/python/pymongo-driver/current/",icon=":material/open_in_new:")
    st.code("pip install pymongo")
    
    st.write("Con pymongo todas las consultas son prácticamente, iguales, cambiando en que las funciones usan notación cammel case,\
        a continuación un ejemplo")
    
    st.code("""
            from pymongo import MongoClient
            
            uri = "mongodb://localhost:27017/"
            client = MongoClient(uri)
            db = client['example']
            
            db.users.insert_one({
                "name": "John",
                "age": 30,
                "email": "john@gmail.com"
            })
            
            collection.find({})
            """, language='python')
    st.write("Hay que tener en cuenta que como es sincrono, es decir bloqueante, debe terminar antes de poder continuar con el código.")
    
    st.header("Motor (asincrono)")
    st.link_button("Motor", "https://www.mongodb.com/docs/drivers/motor/",icon=":material/open_in_new:")
    