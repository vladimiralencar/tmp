# =====================================================
# DASHBOARD ESTRATÉGICO - CENTRO DE COMANDO
# =====================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# --------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------

st.set_page_config(
    page_title="Centro de Comando - Análise de Ataques",
    layout="wide"
)

st.title("🛰️ Painel Estratégico de Ataques")

# --------------------------------------------
# CARREGAR DATASET
# --------------------------------------------

df = pd.read_csv("dataset_ataques_estrategico.csv")

# df["data"] = pd.to_datetime(df[["ano","mes","dia"]])

df["data"] = pd.to_datetime({
    "year": df["ano"],
    "month": df["mes"],
    "day": df["dia"]
})

# --------------------------------------------
# KPIs MILITARES
# --------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Waves",
    df["wave_number"].nunique()
)

col2.metric(
    "Total Armas",
    int(df["total_armas_ofensivas"].sum())
)

col3.metric(
    "Fatalidades",
    int(df["fatalidades"].sum())
)

col4.metric(
    "Taxa média interceptação",
    round(df["taxa_interceptacao"].mean(),2)
)

st.divider()

# --------------------------------------------
# MAPA OPERACIONAL
# --------------------------------------------

st.subheader("🗺️ Mapa Operacional")

coords = {
    "Irã": (32.4279,53.6880),
    "Israel": (31.0461,34.8516),
    "Iraque": (33.2232,43.6793),
    "Síria": (34.8021,38.9968),
    "Jordânia": (31.24,36.51),
    "Kuwait": (29.3759,47.9774),
    "Bahrein": (26.0667,50.5577),
    "Emirados Árabes Unidos": (23.4241,53.8478)
}

mapa = folium.Map(
    location=[32,45],
    zoom_start=4,
    tiles="cartodbdark_matter"
)

lat_ira, lon_ira = coords["Irã"]

for _, row in df.iterrows():

    pais = row["nome_pais_atacado"]

    if pais not in coords:
        continue

    lat, lon = coords[pais]

    intensidade = row["total_armas_ofensivas"]

    folium.PolyLine(
        [[lat_ira,lon_ira],[lat,lon]],
        color="red",
        weight=intensidade/8 + 1
    ).add_to(mapa)

    folium.CircleMarker(
        location=[lat,lon],
        radius=intensidade/5 + 4,
        color="yellow",
        fill=True
    ).add_to(mapa)

st_folium(mapa,width=1400,height=600)

st.divider()

# --------------------------------------------
# GRÁFICOS
# --------------------------------------------

col1,col2 = st.columns(2)

# intensidade das waves


fig1 = px.bar(
    df,
    x="wave_number",
    y="total_armas_ofensivas",
    title="Intensidade das Waves"
)

st.plotly_chart(fig1, use_container_width=True, key="waves")


fig2 = px.line(
    df,
    x="data",
    y="intensidade_wave",
    markers=True,
    title="Evolução Temporal"
)

st.plotly_chart(fig2, use_container_width=True, key="timeline")


fig3 = px.pie(
    df,
    names="nome_pais_atacado",
    title="Distribuição de Ataques por País"
)

st.plotly_chart(fig3, use_container_width=True, key="paises")
