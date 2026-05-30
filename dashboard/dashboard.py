import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Obesidade")

st.title("Dashboard Analítico - Obesidade")

df = pd.read_csv("data/Obesity.csv")


st.write(df.head())
st.stop()

st.subheader("Distribuição dos Níveis de Obesidade")

st.bar_chart(
    df["Obesity"].value_counts()
)

st.subheader("Histórico Familiar x Obesidade")

hist = pd.crosstab(
    df["family_history_with_overweight"],
    df["Obesity"]
)

st.bar_chart(hist)

st.subheader("Atividade Física Média")

atividade = (
    df.groupby("Obesity")["FAF"]
    .mean()
)

st.bar_chart(atividade)

df["BMI"] = (
    df["Weight"] /
    (df["Height"] ** 2)
)

st.subheader("IMC Médio por Classe")

imc = (
    df.groupby("Obesity")["BMI"]
    .mean()
)

st.bar_chart(imc)