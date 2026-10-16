from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
#-----------------------------
model1=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
model2=ChatOpenAI(model='gpt-3.5-turbo')
#-----------------------------
prompt1=PromptTemplate(template='Generate a summary on this {Topic}', input_variables=['Topic'])
prompt2=PromptTemplate(template='Generate 5 quiz question on {Topic}',input_variables=['Topic'])
#-----------------------------
parser=StrOutputParser()
#-----------------------------
parallel_chain=RunnableParallel({'summary': prompt1 | model1 | parser, 'quiz': prompt1 | model2 | parser})
prompt3=PromptTemplate(template='Merge the following {summary} and {quiz} together', input_variables=['summary','quiz'])

#-----------------------------
chain = prompt3 | model2 | parser
final_chain = parallel_chain | chain 
#-----------------------------
#result=final_chain.invoke({'Topic':'Generative AI'})
#print(result)

st.title("Simple chatbot")


question=st.text_input("Enter your question or topic:")

if question:
    response = final_chain.invoke({"Topic": question})
    st.write(response)