import streamlit as st


def Modelos_introduccion():

    st.markdown("## Introducción:")

    st.markdown("### Definición de modelos matemáticos en Data Science")
    st.write("Los modelos matemáticos son una representación simplificada de un sistema real, que se utiliza para estudiar el comportamiento del sistema o para hacer predicciones sobre su comportamiento futuro. En el contexto de la ciencia de datos, los modelos matemáticos se utilizan para analizar y predecir el comportamiento de los datos, y para tomar decisiones basadas en esos análisis.")

    st.markdown("#### Ejemplo de modelo matemático:")
    st.markdown("##### 📌 Predicción de temperatura:")
    st.write("La temperatura de un día puede modelarse mediante una regresión lineal simple:")
    st.latex(r"T = \alpha + \beta \cdot H + \varepsilon")


    st.markdown("""
                donde:
                *   𝑇 es la temperatura.
                *   𝐻 es la humedad.
                *   α,β son coeficientes del modelo.
                *   ε es el error.

                y se establece relación entre una variable dependiente (temperatura 𝑇) y una variable independiente (humedad 𝐻).
                """)
    
    st.write("Supongamos el siguiente dataset")
    st.code("""
            # Fijar semilla para reproducibilidad
            np.random.seed(42)

            # Generar datos de humedad (H) en porcentaje (entre 20% y 90%)
            humedad = np.random.uniform(20, 90, 20)
            """)
    

    st.markdown("### Importancia de los indicadores en la toma de decisiones basada en datos.")
    st.write("Los indicadores son medidas cuantitativas que se utilizan para evaluar el desempeño de un sistema o para medir el impacto de una intervención. En el contexto de la ciencia de datos, los indicadores se utilizan para evaluar la calidad de los datos, para medir el rendimiento de los modelos matemáticos y para evaluar el impacto de las decisiones basadas en datos.")
        
    st.markdown("### Aplicaciones en distintos dominios (negocios, salud, finanzas, seguridad, etc.).")
    st.write()