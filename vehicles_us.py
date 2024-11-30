import pandas as pd
import plotly.express as px
import streamlit as st

df_vehicles = pd.read_csv("notebooks/vehicles_us.csv")

st.header(
    "Análisis de los Anúncios de Venta para Vehículos Usados en los Estados Unidos")
st.image("image_vehicles_us.png", use_container_width=True)
st.write("")
st.write("A continuación, encontrará una lista con diversas secciones que al seleccionar una o varias, le mostrará el análisis con gráficos y observaciones relevantes.")
st.divider()

vehicles_price_checkbox = st.checkbox('Precios de Vehículos')
odometer_price_checkbok = st.checkbox('Correlación entre Kilometraje y Precio')
vehicle_type_checkbox = st.checkbox('Popularidad del Tipo de Vehículo')
days_condition_checkbox = st.checkbox(
    'Duración Promedio en el Mercado por Condición del Vehículo')
paint_color_checkbox = st.checkbox('Popularidad de Colores en los Vehículos')
st.divider()

if vehicles_price_checkbox:
    st.markdown("### Distribución de los Precios de Vehículos")

    fig_price_distribution = px.histogram(df_vehicles,
                                          x="price",
                                          nbins=50,
                                          marginal="box")
    fig_price_distribution.update_layout(
        xaxis_title="Precio en USD",
        yaxis_title="Unidades")
    st.plotly_chart(fig_price_distribution, use_container_width=True)

    st.write("Observaciones:")
    st.markdown("""
    - La mayoría de los vehículos anunciados tienen precios que oscilan entre los $5,000 y $15,000 dólares, mostrándose como opciones accesibles para un mercado amplio.
    - Se observaron vehículos de alta gama con precios superiores a $50,000 dólares, aunque representan una minoría en el mercado.
    - La distribución de precios presenta un sesgo hacia valores más bajos, muestra de que los vehículos económicos dominan el mercado.
    """)
    st.divider()

if odometer_price_checkbok:
    st.markdown("### Correlación entre el Kilometraje y los Precios Anunciados")

    fig_odometer_price = px.scatter(df_vehicles,
                                    x="odometer",
                                    y="price",
                                    color="condition",
                                    labels={"odometer": "Kilometraje (Odómetro)", "price": "Precio"})
    st.plotly_chart(fig_odometer_price, use_container_width=True)

    st.write("Observaciones:")
    st.markdown("""
    - Existe una corelación inversa entre el kilometraje y el precio: vehículos con menos de 50,000 km tienden a alcanzar precios más altos.
    - La condición del vehículo resulta muy importante: vehículos en condiciones "como nuevos" y "excelentes" tienen precios elevados, incluso si tienen una gran cantidad de kilometraje.
    - Los compradores en busca de vehículos económicos, podrán encontrar en aquellos con un kilometraje alto, una gran oportunidad de ahorro.
    """)
    st.divider()

if vehicle_type_checkbox:
    st.markdown("### Popularidad en el Mercado por Tipo de Vehículo")

    df_vehicles_type = df_vehicles["type"].value_counts().reset_index()

    fig_vehicle_types = px.bar(df_vehicles_type,
                               x="type",
                               y="count",
                               labels={"type": "Tipo de Vehículo", "count": "Número de anuncios"})
    st.plotly_chart(fig_vehicle_types, use_container_width=True)

    st.write("Observaciones:")
    st.markdown("""
    - Los SUVs, sedanes y camiones son los tipos de vehículos más populares, representando juntos más del 60% de los anuncios.
    - Los vans, convertibles y buses tienen una participación menor, mostràndose como opciones más específicas o nichos de mercado.
    - Esto indica que los sedanes y SUVs son opciones seguras tanto para compradores como para vendedores, debido a su alta demanda.
    """)
    st.divider()

if days_condition_checkbox:
    st.markdown(
        "### Días Promedio en el Mercado Dependiendo la Condición del Vehículo")

    fig_days_condition = px.box(df_vehicles,
                                x="condition",
                                y="days_listed",
                                labels={"condition": "Condición del vehículo", "days_listed": "Días en el mercado"})
    st.plotly_chart(fig_days_condition, use_container_width=True)

    st.write("Observaciones:")
    st.markdown("""
    - Los vehículos en mejores condiciones, como "excelentes" o "como nuevos", se venden rápidamente, con una duración promedio en el mercado de menos de 10 días.
    - Los vehículos en condiciones "buenas" tienen un tiempo de venta intermedio, mientras que los "reparables" suelen permanecer listados durante más de 30 días.
    - Lo anterior muestra la importancia de contar con buena presentación y mantenimiento para acelerar la venta.
    """)
    st.divider()

if paint_color_checkbox:
    st.markdown("### Distribución de Color en los Vehículos Anunciados")

    df_paint_color = df_vehicles["paint_color"].value_counts().reset_index()

    fig_paint_color = px.pie(df_paint_color,
                             names="paint_color",
                             values="count",
                             labels={"paint_color": "Color de Pintura", "count": "Frecuencia"})
    st.plotly_chart(fig_paint_color, use_container_width=True)

    st.write("Observaciones:")
    st.markdown("""
    - Los colores más populares en los anuncios son el blanco y el negro, representando más del 40% del total de vehículos.
    - Colores como gris y plata también son comunes, lo que sugiere una preferencia general por tonos neutros y versátiles.
    - Los colores menos comunes pueden apuntar a preferencias más particulares o atrevidas, enfocadas a nichos de mercado.
    """)
    st.divider()
