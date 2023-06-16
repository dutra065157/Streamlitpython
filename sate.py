import streamlit as st
import  pandas as pd

st.set_page_config(page_title="meu sate streamlit")
with st.container():
    st.subheader("quero muito apreder a programar")
    st.write("vamo nessa boy")
    st.write("acessar sate[Clique aqui](https://www.youtube.com/watch?v=0sxWFeFlsHs&t=636s)")
    st.line_chart()
@st.cache_data
def carregar_dados():


    tabela= pd.read_csv("resultados.csv")
    return tabela


with st.container():
    st.write("---")
    quantidades_dias= st.selectbox("selecionar o periodo", ["7D", "15D", "21D", "30D"])
    numeros_dias= int(quantidades_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[numeros_dias:]
    st.area_chart(dados, x="Data", y="Contratos")


















