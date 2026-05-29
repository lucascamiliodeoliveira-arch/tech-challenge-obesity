import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/obesity_model.pkl")

st.title("Predição de Obesidade")

age = st.slider("Idade", 10, 80, 25)
height = st.slider("Altura (m)", 1.40, 2.10, 1.70)
weight = st.slider("Peso (kg)", 30.0, 200.0, 70.0)

bmi = weight / (height ** 2)

st.write(f"IMC calculado: {bmi:.2f}")

gender = st.selectbox(
    "Sexo",
    ["Feminino", "Masculino"]
)

st.write("Sexo escolhido:", gender)

fcvc = st.slider(
    "Quantas porções de vegetais você come por dia?",
    1.0, 3.0, 2.0
)

ncp = st.slider(
    "Número de refeições principais por dia",
    1.0, 5.0, 3.0
)

ch2o = st.slider(
    "Litros de água por dia",
    1.0, 3.0, 2.0
)

faf = st.slider(
    "Frequência de atividade física",
    0.0, 3.0, 1.0
)

tue = st.slider(
    "Horas por dia usando celular/computador",
    0.0, 3.0, 1.0
)

family_history = st.selectbox(
    "Histórico familiar de obesidade?",
    ["Não", "Sim"]
)

favc = st.selectbox(
    "Consome alimentos altamente calóricos com frequência?",
    ["Não", "Sim"]
)

smoke = st.selectbox(
    "Fuma?",
    ["Não", "Sim"]
)

scc = st.selectbox(
    "Monitora o consumo de calorias?",
    ["Não", "Sim"]
)

caec = st.selectbox(
    "Come entre as refeições?",
    ["Não", "Às vezes", "Frequentemente"]
)

calc = st.selectbox(
    "Consumo de álcool",
    ["Não", "Às vezes", "Frequentemente"]
)

mtrans = st.selectbox(
    "Meio de transporte principal",
    [
        "Caminhada",
        "Bicicleta",
        "Moto",
        "Transporte Público"
    ]
)

if st.button("Prever Obesidade"):

    dados = {
        "Age": age,
        "Height": height,
        "Weight": weight,
        "FCVC": fcvc,
        "NCP": ncp,
        "CH2O": ch2o,
        "FAF": faf,
        "TUE": tue,
        "BMI": bmi,

        "Gender_Male": 1 if gender == "Masculino" else 0,

        "family_history_yes": 1 if family_history == "Sim" else 0,

        "FAVC_yes": 1 if favc == "Sim" else 0,

        "CAEC_Frequently": 1 if caec == "Frequentemente" else 0,
        "CAEC_Sometimes": 1 if caec == "Às vezes" else 0,
        "CAEC_no": 1 if caec == "Não" else 0,

        "SMOKE_yes": 1 if smoke == "Sim" else 0,

        "SCC_yes": 1 if scc == "Sim" else 0,

        "CALC_Frequently": 1 if calc == "Frequentemente" else 0,
        "CALC_Sometimes": 1 if calc == "Às vezes" else 0,
        "CALC_no": 1 if calc == "Não" else 0,

        "MTRANS_Bike": 1 if mtrans == "Bicicleta" else 0,
        "MTRANS_Motorbike": 1 if mtrans == "Moto" else 0,
        "MTRANS_Public_Transportation": 1 if mtrans == "Transporte Público" else 0,
        "MTRANS_Walking": 1 if mtrans == "Caminhada" else 0,
    }

    df = pd.DataFrame([dados])

    previsao = model.predict(df)

    st.success(f"Classificação prevista: {previsao[0]}")