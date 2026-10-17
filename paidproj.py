import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

prompt=ChatPromptTemplate([('system','you are a helpful AI assistant'),('human','Question:{Question}')])

def generate_response(query,llm,temperature,max_token):
    model=ChatOpenAI(model_name=llm,temperature=temperature,max_retries=max_token)
    parser=StrOutputParser()
    chain = prompt | model | parser
    result=chain.invoke({'Question':query})
    return result

st.title('Q and A chatbot')
query=st.text_input('What is your query')
llm=st.sidebar.selectbox('Select the LLM',{'gpt-3.5-turbo','gpt-4o','gpt-5','gpt-6'})
temperature=st.sidebar.slider('Select temperture',min_value=0.0,max_value=2.0,value=0.8)
max_token=st.sidebar.slider('Select token:', min_value=50,max_value=200,value=100)

if st.button('Answer'):
    if query:
        response=generate_response(query,llm,temperature,max_token)
        st.write(response)
    else:
        st.warning("Please enter some query")