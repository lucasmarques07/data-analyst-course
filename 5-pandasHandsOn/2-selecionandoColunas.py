import streamlit as st
import pandas as pd 

caminhoArquivo = "datasets/compras.csv"

dfCompras = pd.read_csv(caminhoArquivo, sep=";", decimal=",", index_col=0)

colunas = list(dfCompras)
colunasSelecionadas = st.sidebar.multiselect("Selecione as colunas: ", colunas, colunas)

col1, col2 = st.sidebar.columns(2)

colFiltro = col1.selectbox("Seleciona a coluna",
                            [c for c in colunas if c not in ["id_compra"]])
valorFiltro = col2.selectbox("Selecione o valor",
                             list(dfCompras[colFiltro].unique()))

stFiltrar = col1.button("Filtrar")
stLimpar = col2.button("Limpar")

if stFiltrar:
    st.dataframe(dfCompras.loc[dfCompras[colFiltro] == valorFiltro, colunasSelecionadas])
elif stLimpar:
    st.dataframe(dfCompras[colunasSelecionadas])
else: 
    st.dataframe(dfCompras[colunasSelecionadas])