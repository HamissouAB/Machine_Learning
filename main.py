from fastapi import FastAPI
import uvicorn
import streamlit as st
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go


def load_data ()  :
    ## Chargement des données###
    base_achats = pd.read_csv("achats.csv", parse_dates=['timestamp'])
    base_clics = pd.read_csv("clics.csv", parse_dates=['timestamp'])
    base_impression = pd.read_csv("impressions.csv", parse_dates=['timestamp'])
    base_merge = pd.merge(base_impression, base_clics, on='cookie_id', how='left')
    base_finale = pd.merge(base_merge, base_achats, on='cookie_id', how='left')
    return base_finale

#Titres
st.title("Hamissou ALAJI BOUHARI ")

st.write("Bonjour et bienvenue")
df = load_data()
st.write(df)
check_box = st.sidebar.checkbox(label = 'display dataset')

fig = go.Figure(
    data=[go.Bar(y=df['age'])],
    layout_title_text="Distribution des âges"
)
#fig.show()
st.write(fig)
#st.write(ba)
chiffre_affaires = df['price'].sum()
st.write(f"<span style='color:red; font-size:40px;'>Chiffre d'affaires : {chiffre_affaires} € </span>", unsafe_allow_html=True)

#diagramme circulaire

diagramme  = px.pie(df, values='dept', names='gender')
st.plotly_chart(diagramme)

st.subheader('Produits en fonction des ages')
box= px.box(df, x= 'product_id' , y= 'age')
st.plotly_chart(box)