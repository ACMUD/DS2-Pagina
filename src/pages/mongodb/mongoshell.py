import streamlit as st

def MongoShell():
    st.header("Mongosh")
    st.write("Se puede utilizar mongo mediante la shell, con mongosh la cual es una herramienta de linea de comandos para conectarse a bases de datos mongo.")
    st.header("Instalación")
    st.link_button("Mongosh", "https://www.mongodb.com/try/download/shell", icon=":material/open_in_new:")
    st.write("En windows se instala como cualquier programa, se ejecuta el .exe y se instala.")
    st.write("En un linux como debian o ubuntu se descargará un deb, se puede instalar con dpkg.")
    st.code("""
            wget <link>
            sudo dpkg -i <paquete>.deb
            """)
    st.header("Uso")
    st.write("mongosh recibe un parametro que es la URL de conexión, si no se coloca se toma por defecto es `mongodb://localhost:27017`")
    st.code("mongosh <URL>")
    st.subheader("Comandos básicos")
    st.write("Listar bases de datos")
    st.code("""
            show dbs
            > admin     40.00 KiB
            > config    40.00 KiB
            > local     72.00 KiB
            use test
            """)
    
    st.code("""
            show collections
            > col1
            > col2
            """)
    
    st.write("Mongo admite el uso de **javascript**")
    st.code("""
            let a = 1+[1,2,3,4].length
            console.log(a)
            > 5
            """)

    st.write("")
    st.code("""
            db.col1.insertOne({'juego':'Skyrim'})
            > {
                acknowledged: true,
                insertedId: ObjectId('67da0526ef681528996b140b')
                }
            """)