from datetime import datetime
import streamlit as st
import pandas as pd

caminhoDatasets = "datasets"

dfCompras = pd.read_csv(f"{caminhoDatasets}/compras.csv", sep=";", decimal=",", index_col=0)
dfLojas = pd.read_csv(f"{caminhoDatasets}/lojas.csv", sep=";", decimal=",")
dfProdutos = pd.read_csv(f"{caminhoDatasets}/produtos.csv", sep=";", decimal=",")

dfLojas["cidade/estado"] = dfLojas["cidade"] + '/' + dfLojas["estado"]
listaLojas = dfLojas["cidade/estado"].tolist()

lojaSelecionada = st.sidebar.selectbox("Selecione a loja: ", listaLojas)

listaVendedores = dfLojas.loc[dfLojas["cidade/estado"] == lojaSelecionada, "vendedores"].iloc[0]

listaVendedores = listaVendedores.strip("][").replace("'", "").split(", ")
st.sidebar.selectbox("Selecione o vendedor: ", listaVendedores)

listaProdutos = dfProdutos()