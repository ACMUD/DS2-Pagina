import streamlit as st

def MongoAggregations():
    st.title("Agregación")
    st.write("Las agregaciones son operaciones que procesan los datos de una colección, para realizar una agregación se utiliza la función `aggregate`")
    
    st.write("suponiendo los siguientes datos")
    st.json([
        { '_id': 3, 'producto': 'A', 'cantidad': 7, 'precio': 20 },
        { '_id': 2, 'producto': 'A', 'cantidad': 103, 'precio': 20 },
        { '_id': 5, 'producto': 'A', 'cantidad': 7, 'precio': 20 },
        { '_id': 7, 'producto': 'B', 'cantidad': 103, 'precio': 20 }
        ])
    
    st.code("""
            db.ventas.aggregate([
            {
                $group: {
                _id: "$producto",
                totalVentas: { $sum: { $multiply: ["$cantidad", "$precio"] } }
                }
            }
            ])
            """)
    st.json([ { '_id': 'A', 'totalVentas': 2340 }, { '_id': 'B', 'totalVentas': 2060 } ])