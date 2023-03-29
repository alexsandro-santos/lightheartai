import streamlit as st
import pickle
import numpy as np

st.set_page_config(
     page_title="Light Heart AI",
     page_icon="icon_lightheart.png",
     layout="wide",
 )

# header
# _, logo_limit, _ = st.columns([0.5,5,1])
head = st.container()
# subheaders
# subh1, subh2 = st.columns([2,1])
# input data
col1, col2 = st.columns([2,1], gap='large')

c1, c2 = st.columns([2,1], gap='large')

_, button_position, _ = st.columns(3)

head.image('logo_lightheart.png')
head.title('Diagnóstico da Doença Arterial Coronariana')

sex_opt = ['Selecione o sexo do paciente', 'Masculino', 'Feminino']
# chest pain types
cp_types = ['Angina típica', 'Angina atípica', 'Dor não anginosa', 'Sem dor']

with st.container():
    col1.header('Informações básicas')
    name = col1.text_input('Nome').title()
    age = col1.number_input('Idade', min_value=0)
    sex = col1.selectbox('Sexo', sex_opt)
    weight = col1.number_input('Peso (kg)', min_value=0.0)
    height = col1.number_input('Altura (m)', min_value=0.0)

    col2.header('Sintomas')
    cp = col2.radio('Dor no peito', cp_types, index=len(cp_types)-1)

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
    thal = 6.0

m = st.markdown(""" <style> div.stButton > button:first-child { background-color: #0352fc; color: white; height: 3em; width: 12em} </style>""", unsafe_allow_html=True)

exec_button = button_position.button('Obter o diagnóstico')

rest_cg_values = [0,1,2]
fbs_values = [1,0]
slope_values = [1,3,2] 
cp_values = [1,2,3,4]
sex_values = ['', 1, 0]

map_sex = {chave:valor for chave, valor in zip(sex_opt,sex_values)}
map_restecg = {chave:valor for chave, valor in zip(ecg_result,rest_cg_values)}
map_fbs = {chave:valor for chave, valor in zip(bld_sugar, fbs_values)}
map_cp = {chave:valor for chave, valor in zip(cp_types, cp_values)}
map_slope = {chave:valor for chave, valor in zip(slope_opt, slope_values)}

# modelo
trained_model = open('model.pkl', 'rb')

model = pickle.load(trained_model)

X = np.array([age, map_sex[sex], map_cp[cp], trestbps, chol, map_fbs[fbs], map_restecg[restecg], thalach, exang, oldpeak, map_slope[slope], ca, thal]) 

if exec_button:
    st.subheader('Resultado')
    st.write(f'Nome do paciente: **{name}**')
    prob = model.predict_proba(X.reshape(-1,1).T)
    if prob[0, 1] <= 0.5:
        result = 'risco baixo'
    elif prob[0, 1] <= 0.75:
        result = 'risco médio'
    else:
        result = 'risco alto'
    st.write(f'Foi detectado um **{result}** do paciente estar com a Doença Arterial Coronariana.')
