import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado
st.header('Análisis de Datos de Vehículos')

# Crear un botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión')
    
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)