import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Prices ", page_icon="💸")

df_reviews = pd.read_csv("pages/customer reviews.csv")
df_top100 = pd.read_csv("pages/Top-100 Trending Books.csv")

price_max = df_top100["book price"].max()
price_min = df_top100["book price"].min()

max_price = st.sidebar.slider("Select Range Price", price_min, price_max, price_max)

df_books = df_top100[df_top100["book price"] <= max_price]

years = px.bar(df_books["year of publication"].value_counts())
prices = px.histogram(df_books["book price"])

df_books
col1, col2 = st.columns(2)
col1.plotly_chart(years)
col2.plotly_chart(prices)