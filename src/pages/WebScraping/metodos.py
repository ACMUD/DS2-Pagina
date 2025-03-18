import streamlit as st

def WebScraping_metodos():

    st.markdown("## Métodos de Web Scraping:")

    st.markdown("### Scraping con requests y BeautifulSoup")
    st.write("Envío de solicitudes HTTP (GET, POST).")
    st.write("Análisis del HTML con BeautifulSoup.")
    st.write("Extracción de datos estructurados.")

    st.markdown("### Scraping con Scrapy")
    st.write("Creación de un spider para automatizar la extracción.")
    st.write("Manejo de múltiples páginas y navegación recursiva.")
    st.write("Exportación de datos en CSV, JSON, y bases de datos.")
    
    st.markdown("### Scraping con Selenium (JavaScript Rendering)")
    st.write("Interacción con páginas dinámicas.")
    st.write("Simulación de clics, scroll y llenado de formularios.")
    st.write("Uso de WebDriver (Chrome, Firefox, Edge).")