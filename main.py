import streamlit as st
import numpy as np
import joblib


# Load model
stunting_model = joblib.load('model_deteksi_stunting.pkl')
status_gizi_model = joblib.load ('model_deteksi_status_berat_badan.pkl')


# Streamlit app

st.markdown('---')
st.title('Klasifikasi Stunting dan Status Gizi Balita Dengan SVM')
st.markdown('---')


Umur = st.number_input ('Inputkan umur balita (0 - 60 bulan)', min_value=0, max_value=60)
if Umur < 0 or Umur > 60:
    st.error("Umur harus berada di rentang 0 sampai 60 bulan")
JenisKelamin = st.radio('Jenis Kelamin', ['laki-laki', 'perempuan'])
Tinggi = st.text_input ('Masukkan tinggi badan (cm). Contoh : 98.3')
Berat = st.text_input('Masukkan berat badan (kg). Contoh : 8.2')

JK = 0 if JenisKelamin == 'laki-laki' else 1

#code klasifikasi
stunting_klasifikasi = ''
status_gizi = ''
#tombol
if st.button('Submit'):
    st.subheader('Hasil Klasifikasi')
    stunting_klasifikasi = stunting_model.predict([[Umur, JK, Tinggi]])

    if(stunting_klasifikasi[0] == 0):
        stunting_klasifikasi = 'Kondisi Balita : Severely Stunted'
    elif(stunting_klasifikasi[0] == 1):
        stunting_klasifikasi = 'Kondisi Balita : Stunted'
    elif(stunting_klasifikasi[0] == 2):
        stunting_klasifikasi = 'Kondisi Balita : Normal'
    elif (stunting_klasifikasi[0] == 3):
        stunting_klasifikasi = 'Kondisi Balita : Tinggi'

    st.success(stunting_klasifikasi)

    status_gizi = status_gizi_model.predict([[Umur, Berat, JK]])

    if (status_gizi[0] == 0):
        status_gizi = 'Status Berat Badan : Severely Underweight'
    elif (status_gizi[0] == 1):
        status_gizi = 'Status Berat Badan : Underweight'
    elif (status_gizi[0] == 2):
        status_gizi = 'Status Berat Badan : Normal'
    elif (status_gizi[0] == 3):
        status_gizi = 'Status Berat Badan : Overweight'
    st.success(status_gizi)
