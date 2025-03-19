import streamlit as st

def MongoShell():
    st.title("Mongosh")
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
    st.code("show dbs")
    st.code("""
            > admin     40.00 KiB
            > config    40.00 KiB
            > local     72.00 KiB
            """)
    st.code("use test")
    
    st.code("show collections")
    st.code("""
            > col1
            > col2
            """)
    
    st.write("Mongo admite el uso de **javascript**")
    st.code("""
            let a = 1+[1,2,3,4].length
            console.log(a)
            """)
    st.code("> 5")

    st.subheader("Crear")
    st.write("Para insertar documentos se puede hacer mediante la instrucción `insertOne` o `insertMany`")
    st.code("db.col1.insertOne({'juego':'Skyrim'})")
    st.json({
                "acknowledged": True,
                "insertedId": "ObjectId('67da0526ef681528996b140b')"
                })
    st.code("db.col1.insertMany([{'nombre':'juan'}, {'dia': 'Martes'}])")
    st.json({
                "acknowledged": True,
                "insertedIds": {
                    '0': "ObjectId('67da0589ef681528996b140c')",
                    '1': "ObjectId('67da0589ef681528996b140d')"
                    }
                })
    st.subheader("Leer")
    st.write("Para leer se puede hacer mediante la instrucción `find`")
    st.code("db.col1.find()")
    st.json([
                { "_id": "ObjectId('67da0526ef681528996b140b')", "juego": 'Skyrim' },
                { "_id": "ObjectId('67da0589ef681528996b140c')", "nombre": 'juan' },
                { "_id": "ObjectId('67da0589ef681528996b140d')", "dia": 'Martes' }
             ])
    st.write("Las consultas son diccionarios que pueden ayudar a filtrar los documentos, por ejemplo por un nombre o por un valor.")
    st.code("""
            db.col1.find(<consulta>)
            db.col1.find({juego:'Skyrim'})
            """)
    st.json([ { "_id": "ObjectId('67da0526ef681528996b140b')", "juego": 'Skyrim' } ])
    st.code("db.col1.findOne({nombre:'juan'})")
    st.json({ "_id": "ObjectId('67da0526ef681528996b140b')", "nombre": 'juan' })
    
    st.subheader("Actualizar")
    st.write("""Para actualizar se puede hacer mediante la instrucción `updateOne` o `updateMany`
             Para actualizar uno o varios se debe hacer una consulta que filtre los documentos a actualizar y un diccionario con operaciones atómicas a realizar.
             """)
    st.code("""
            db.col1.updateMany({},{$set:{nombre:'juan'}})
            """)
    st.json({
                "acknowledged": True,
                "insertedId": None,
                "matchedCount": 3,
                "modifiedCount": 2,
                "upsertedCount": 0
                })
    
    st.code("db.col1.updateOne({_id:ObjectId('67da0526ef681528996b140b')}, {'nombre':'carlos'})")
    
    st.subheader('Borrar')
    st.write("Para borrar se puede hacer mediante la instrucción `deleteOne` o `deleteMany`")
    st.code("db.col1.deleteOne({_id:ObjectId('67da0526ef681528996b140b')})")
    st.json({ "acknowledged": True, "deletedCount": 1 })
    
    st.code("db.col1.deleteMany({})")