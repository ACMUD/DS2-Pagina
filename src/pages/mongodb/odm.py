import streamlit as st
def ODM():
    st.title("ODM (Object Document Mapper)")
    st.link_button("odmantic", "https://art049.github.io/odmantic/",icon=":material/open_in_new:")
    st.markdown("""
                ODMantic es un ORM (Object Document Mapper), que facilita la interacción y las consultas con la base de datos, permitiendo gestionar en código no solo los modelos y los tipos de datos sino tambien indices y propiedades de cada colección.
                Los modelos de odmantic se basan en pydantic por lo cual facilitan mucho la validación de los datos y el procesmiento.
                """)
    st.header("Modelado de la base de datos")
    st.code("""
            from odmantic import Model
            
            class User(Model):
                name: str
                email: str
            """)
    st.write("Luego se puede agregar una validación al modelo o incluso modelos anidados")
    st.code("""
            from odmantic import Field, Index, EmbeddedModel
            
            class Favoritos(EmbeddedModel):
                musica: list[str] = []
                peliculas: list[str] = []
            
            class User(Model):
                name: str = Field(index=True)
                email: str = Field(unique=True)
                favoritos: Favoritos = Field(default_factory=Favoritos)
                
                model_config = {
                    "Indexes": lambda: [
                        Index(User.name),
                        Index(User.email, unique=True)
                    ]
                }
            """)
    
    st.write("Todos los modelos tienen representaciones en json, y normalmente reciben otro objeto o un json")
    
    col1, col2 = st.columns(2)
    col1.code("""
            class SimpleUser(Model):
                name: str = Field(index=True)
                email: str = Field(unique=True)
            
            SimpleUser(user) # user -> User
               """)
    col2.json("""
              {
                  "name":"Juan",
                  "email":"juan@gmail.com"
              }
              """)
    
    st.header("configuración de la base de datos")
    st.write("Se puede construir una base de datos a partir de un modelo")
    st.code("""
            from odmantic import AIOEngine
            from .models import User
            
            client = <cliente>
            engine = AIOEngine(client, database = 'test')
            
            engine.configure_database([User])
            """)
    st.header("Consultas con odmantic")
    
    st.write("Finalmente para buscar con ODMantic se puede usar el engine seguir del uso de las clases.")
    st.write("Hay que tener en cuenta que ``ObjectId`` no puede ser serializado como json, por lo cual debe convertirse a ``str`` antes de serializarlo")
    st.code("""
             # Si es asincrono debe usarse con await dentro de una función asincrona
             user = engine.find_one(User, User.email == 'juan@gmail.com')
             
             user.name = user.name.upper()
             
             engine.save(user)
             """)