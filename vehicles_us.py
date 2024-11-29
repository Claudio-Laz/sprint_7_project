import pandas as pd
import plotly.express as px
import streamlit as st

df_vehicles = pd.read_csv("notebooks/vehicles_us.csv")

st.header("Análisis de los Anúncios de Venta para Vehículos Usados en los Estados Unidos")
st.write("")
st.write("A continuación, encontrará una lista con diversas secciones que al seleccionar una o varias, le mostrará el análisis con gráficos y observaciones relevantes.")
st.divider()

vehicles_price_checkbox = st.checkbox('Precios de Vehículos')
odometer_price_checkbok = st.checkbox('Relación entre Kilometraje y Precio')
vehicle_type_checkbox = st.checkbox('Popularidad del Tipo de Vehículo')
days_condition_checkbox = st.checkbox('Duración Promedio en el Mercado por Condición del Vehículo')
paint_color_checkbox = st.checkbox('Popularidad de Colores en los Vehículos')
st.divider()

if vehicles_price_checkbox:
    st.write(
        "Hola")
    fig_price_distribution = px.histogram(df_vehicles,
                                          x="price",
                                          nbins=50,
                                          title="Distribución de Precios de Vehículos",
                                          marginal="box")

    fig_price_distribution.update_layout(
        xaxis_title="Precio en USD",
        yaxis_title="Millones de unidades")
    st.plotly_chart(fig_price_distribution, use_container_width=True)
