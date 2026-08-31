import streamlit as st
import pandas as pd 

caminhoCompras = "datasets/compras.csv"

dfCompras = pd.read_csv(caminhoCompras, sep=";", decimal=",")

st.dataframe(dfCompras)