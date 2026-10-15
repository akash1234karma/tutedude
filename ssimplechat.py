import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

st.title("Simple chatbot")
input_text=st.text_input("Enter your question")
model=ChatOpenAI(model='gpt-3.5-turbo')


if input_text:
    response=model.invoke(input_text)
    st.write(response)