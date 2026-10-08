import streamlit as st
import pandas as pd

st.header("welcome to streamlit")

if st.button("click me"):
    st.write("say hi")

agree=st.checkbox("i agree")
if agree:
    st.write("you agree")

level=st.slider("select level:" , 1,10,5)
st.write(f'select level {level}')

uploaded_file=st.file_uploader("upload a file", type=["txt","csv"])
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df.head())