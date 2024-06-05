import streamlit as st
import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

elif menu_selection == "Noticias de Mercado":
    st.markdown("# Noticias de Mercado")
    # Mostrar DataFrame con los tickers por sector
    st.write("Selecciona un sector y luego un ticker de la tabla para ver las noticias relevantes:")
    sector_seleccionado = st.selectbox("Selecciona un Sector", pd.unique(df_tickers['Sector']))
    
    # Filtrar tickers para el sector seleccionado
    df_sector = df_tickers[df_tickers['Sector'] == sector_seleccionado]
    ticker_display = st.selectbox("Selecciona un Ticker", df_sector['Display'].tolist())
    
    # Extraer el ticker seleccionado del texto display
    ticker_seleccionado = ticker_display.split(' - ')[0]

    # API Key
    api_key = "728e8a5efd29431ea15f0874e93b8a98"

    # Llamada al API para obtener noticias
    def obtener_noticias(ticker):
        url = f"https://newsapi.org/v2/everything?q={ticker}&apiKey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("articles", [])
        else:
            st.error("No se pudieron obtener las noticias.")
            return []

    # Obtiene las noticias del mercado para el ticker seleccionado
    noticias = obtener_noticias(ticker_seleccionado)

    # Itera sobre cada elemento de noticias y extrae los detalles necesarios
    for item in noticias:
        # Extrae y muestra el título de la noticia
        st.write(f"### {item['title']}")
        # Extrae y muestra la fuente y la hora de publicación
        st.write(f"{item['source']['name']} - {item['publishedAt']}")
        # Muestra el link para leer más sobre la noticia
        st.write(f"[Leer más]({item['url']})")

        # Verifica si existe una imagen asociada y la muestra
        if item.get('urlToImage'):
            st.image(item['urlToImage'], caption="Imagen de la noticia", use_column_width=True)
        else:
            st.image("logoad.png", caption="Logo predeterminado", use_column_width=True)
        
        st.markdown("---")

