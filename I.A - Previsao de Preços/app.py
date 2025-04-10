import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

tabela = pd.read_csv("pizzas.csv")

#Criando o Modelo

modelo = LinearRegression()

# Treinando o Modelo
x = tabela[["diametro"]]
y = tabela[["preco"]]
modelo.fit(x, y)

st.title("Prevendo o valor de uma Pizza")
st.divider()
diamentro = st.number_input("Digite o tamanho do diâmetro da pizza:")

if diamentro:
    preco_previsto = modelo.predict([[diamentro]])[0][0]
    st.write(f"O valor da pizza com diâmetro de {diamentro:.2f}cm é de R${preco_previsto:.2f}")
    st.balloons()
