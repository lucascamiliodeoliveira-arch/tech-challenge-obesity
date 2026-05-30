import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Obesidade")

st.title("Dashboard Analítico - Obesidade")

df = pd.read_csv("data/Obesity.csv")


st.write(df.columns.tolist())
st.stop()


st.subheader("Distribuição dos Níveis de Obesidade")

st.bar_chart(
    df["NObeyesdad"].value_counts()
)

st.subheader("Histórico Familiar x Obesidade")

hist = pd.crosstab(
    df["family_history_with_overweight"],
    df["NObeyesdad"]
)

st.bar_chart(hist)

st.subheader("Atividade Física Média")

atividade = (
    df.groupby("NObeyesdad")["FAF"]
    .mean()
)

st.bar_chart(atividade)

df["BMI"] = (
    df["Weight"] /
    (df["Height"] ** 2)
)

st.subheader("IMC Médio por Classe")

imc = (
    df.groupby("NObeyesdad")["BMI"]
    .mean()
)

st.bar_chart(imc)