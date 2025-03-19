import streamlit as st

def MongoPython():
    st.title("Mongo con Python")
    st.write("""
             Para manejar cualquier base de datos se suele usar herramientas como un ORM que es una forma de representar la base de datos mediante objetos, en el caso de mongo ODM. sin embargo,
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
    st.code("pip install motor")
    st.write("motor es una libreria muy util para trabajar con mongo cuando se requiere un procesamiento asincrona y masiva de datos. A continuación un ejemplo de como se uso")
    st.code("""
            import asyncio
            from motor.motor_asyncio import AsyncIOMotorClient

            async def main():
                uri = "mongodb://localhost:27017/"
                client = AsyncIOMotorClient(uri)
                db = client['test']
                await db.users.insert_one({
                    "nombre":"carlos",
                    "email":"carlos@gmail.com"
                    })

            asyncio.run(main())
            """)
    
    st.markdown("""
                Motor es util cuando:
                *   Se tienen muchos clientes en una base de datos.
                *   Se requiere un acceso masivo a los datos, por ejemplo una API.
                *   Se requiere mayor fluidez en el procesamiento de los datos.
                """)