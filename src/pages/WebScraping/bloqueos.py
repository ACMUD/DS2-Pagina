import streamlit as st

def WebScraping_bloqueos():

    st.markdown("## Evadir Bloqueos y Optimizar Scraping:")

    st.markdown("### Técnicas para evitar ser bloqueado")
    st.write("Respeto a robots.txt y limitación de la frecuencia de requests.")
    st.write("Uso de headers y user-agents personalizados.")
    st.write("Rotación de IPs y uso de proxies.")
    st.write("Selenium headless para reducir detección.")

    st.markdown("### Optimización del scraping")
    st.write("Uso de asynchronous requests (asyncio + aiohttp).")
    st.write("Reducción del tiempo de espera (time.sleep vs WebDriverWait).")