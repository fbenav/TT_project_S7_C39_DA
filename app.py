import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Analisis de venta de vehiculos')

hist_button = st.button('Construir histograma de kilometraje') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
build_lineplot = st.checkbox('Construir evolución precio promedio por día')

if build_lineplot:
    
    # escribir un mensaje
    st.write('Evolución precio promedio según condición del vehiculo')
    df = car_data.groupby(['date_posted','condition'])['price'].mean().reset_index()

    # crear un histograma
    fig = px.line(df, x="date_posted", y="price", color = 'condition',
                  title='precio promedio vehiculos según dia de publicación')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)