import streamlit as st
import numpy as np

# header
_, logo_limit, _ = st.columns([0.5,5,1])
head = st.container()
# subheaders
# subh1, subh2 = st.columns([2,1])
# input data
col1, col2 = st.columns([2,1], gap='large')

c1, c2 = st.columns([2,1], gap='large')

logo_limit.image('logo_lightheart.png', use_column_width='always')
head.title('Diagnóstico da Doença Arterial Coronariana')

sex = ['Selecione o sexo do paciente', 'Masculino', 'Feminino']
# chest pain types
cp_types = ['Angina típica', 'Angina atípica', 'Dor não anginosa', 'Sem dor']

with st.container():
    col1.header('Informações básicas')
    name = col1.text_input('Nome').title()
    age = col1.number_input('Idade', min_value=0)
    sex = col1.selectbox('Sexo', sex,)
    weight = col1.number_input('Peso (kg)', min_value=0.0)
    height = col1.number_input('Altura (m)', min_value=0.0)

    col2.header('Sintomas')
    chest_pain = col2.radio('Dor no peito', cp_types, index=len(cp_types)-1)

with st.container():
    col1.header('Exames')

bld_sugar = ['Maior ou igual 120 mg/dL', 'Menor que 120 mg/dL']
ecg_result = ['Normal', 'Anomalias ST-T', 'Sinais de HVE']
slope_opt = ['Subindo', 'Descendo', 'Sem inclinação']

with st.container():
    trestbps = c1.number_input('Pressão sanguínea (mmHg)', min_value=0.0)
    chol = c1.number_input('Colesterol (mg/dL)', min_value=0.0)
    exang = c2.checkbox('Angina desencadeada por exercício')
    fbs = c2.radio('Glicose em jejum', bld_sugar, index=len(bld_sugar)-1)
    restecg = c2.radio('Eletrocardiograma', ecg_result)
    thalach = c1.number_input('Máxima frequência cardíaca', min_value=0.0)
    oldpeak = c1.number_input('Depressão ST desencadeada por exercício', min_value=0.0)
    slope = c2.radio('Inclinação do pico ST', slope_opt, index=len(slope_opt)-1)
    ca = c1.number_input('Número de vasos coloridos na fluoroscopia', 0, 3)
