import streamlit as st
st.header('Lanzar una moneda')
num_of_trails = st.slider('¿Número de intentos',1,1000,10)
start_button = st.button('Ejecutar')
if start_button:
    st.write(f'experimento con {num_of_trails} intentos en curso.')

st.write('Esta app aún se encuentra en desarrollo')