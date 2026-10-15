import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import load_prompt

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

st.title("CHATBOT")
role=st.selectbox('Select your role:', ['AI engineer','Data scientist','Data engineer','Data analyst'])
goal=st.text_input('What is your goal')
context=st.text_area('Tell me about you experience')

#template=load_prompt('promptT.json')
pt=PromptTemplate(template="""you are a senior{role} working in company. you always have a {goal} in mind and you have {context} """, input_variables=['role',"goal","context"])
prompt=pt.invoke({'role':role,'goal':goal,'context':context})
model=ChatOpenAI(model='gpt-3.5-turbo')
response=model.invoke(prompt)

if st.button('answer'):
    st.write(response.content)