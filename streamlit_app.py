import pickle
import numpy as np
import streamlit as st

# Load the trained model from the file
model = pickle.load(open('model.pkl', 'rb'))

# Create the header with centered title
col0, col1, col2, col3, col4, col5, col6 = st.columns(7)
with col0:
    st.write('')
with col1:
    st.write('')
with col2:
    st.write('')    
with col3:
    st.markdown('<h1 style="color:B284BE; font-family:Papyrus; font-size:22px;">PetalPro</h1>', unsafe_allow_html=True)
with col4:
    st.write('')
with col5:
    st.write('')
with col6:
    st.write('')

# Welcome message
col7, col8, col9 = st.columns(3)
with col7:
    st.write('')    
with col8:
    st.markdown("<h6 style='font-family:Futura;text-align: center;'>Welcome to PetalPro. A simple web app to predict Iris species</h6>", unsafe_allow_html=True)
with col9:
    st.write('')

# Create two columns: one for the image and the other for sliders
col_img, col_sliders = st.columns([1, 2])

# Place image on the left column
with col_img:
    st.image("Rose2.jpg", caption="", use_column_width=True)

# Place sliders on the right column
with col_sliders:
    s_length = st.slider('Enter Sepal Length', 4.0, 8.0)
    s_width = st.slider('Enter Sepal Width', 2.0, 5.0)
    p_length = st.slider('Enter Petal Length', 1.0, 7.0)
    p_width = st.slider('Enter Petal Width', 0.1, 3.0)

# Button to predict Iris species
col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')
with col11:
    st.write('')    
with col12:
    predict_btn = st.button('Predict Iris Species')
with col13:
    st.write('')
with col14:
    st.write('')

# Predict the Iris species
species_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

if predict_btn:
    inp1 = float(s_length)
    inp2 = float(s_width)
    inp3 = float(p_length)
    inp4 = float(p_width)
    
    # Prepare input data
    X = [[inp1, inp2, inp3, inp4]]
    
    # Predict the species
    species_index = model.predict(X)[0]
    predicted_species = species_names[species_index]
    
    # Display the predicted species
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('')    
    with col16:
        st.text(f"Iris Species: {predicted_species}")
    with col17:
        st.write('')
