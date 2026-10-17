import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()

prompt=ChatPromptTemplate([('system','you are an helpful assistant'),('human','Question:{Question}')])

def generate_response(llm,temperature,query):

    model=Ollama(model=llm,temperature=temperature)
    parser=StrOutputParser()
    chain = prompt | model | parser
    result=chain.invoke({'Question': query})
    return result

st.title("Ollama QA chatbot")
query=st.text_input("Enter your question")

st.sidebar.title("Setting")
temperature=st.sidebar.slider('Temperature',min_value=0.0,max_value=1.0,value=0.5)
model=st.sidebar.selectbox("Model is ", {'gemma3:latest','nomic-embed-text:latest','gemma3:1b'})

resposne=generate_response(model,temperature,query)

if st.button("Answer"):
    if query:
        st.write(resposne)
    else:
        st.warning("nothing")