import streamlit as st
import scipy.stats
import time
import pandas as pd

if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0
if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'interactions', 'media'])


st.header('Lanzar una moneda')

chart = st.line_chart([0.5])
def toss_coin(n):
    trail_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trail_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count +=1
        mean = outcome_1_count/outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)
    return mean

num_of_trails = st.slider('¿Número de intentos?',1,1000,10)
start_button = st.button('Ejecutar')
if start_button:
    st.write(f'Experimento con {num_of_trails} intentos en curso.')
    mean = toss_coin(num_of_trails)
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],num_of_trails, mean]], columns=['no', 'iterarions', 'mean'])     
    ], axis= 0)
    st.session_state['df_experiment_results']= \\
    st.session_state['df_experiment_results'].reset_index(drop=True)
st.write(st.session_state['df_experiment_results'])