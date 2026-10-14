import streamlit as st
import pandas as pd
import tensorflow
from tensorflow.keras.models import load_model
import pickle

st.title("Passenger survive")
pclass=st.slider("passenger class", 1,3)
gender=st.selectbox('Gender', ['male','Female'])
sibsp=st.slider('sibling',1,8)
parch=st.slider('parent child',0,6)
fare=st.number_input('Fare')
embarked=st.selectbox('enter station',['Queensland','Cheboung','Southamton'])

