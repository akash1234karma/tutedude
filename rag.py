import streamlit as st
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
#-------------------------
excel=CSVLoader('smallfile.csv',encoding="utf-8")   
splitter=RecursiveCharacterTextSplitter(chunk_size=550,chunk_overlap=120)
documents = excel.load()
chunks = splitter.split_documents(documents)

embeddings=OpenAIEmbeddings(model='text-embedding-3-large')
vector_store = FAISS.from_documents(chunks, embeddings)

retriever=vector_store.as_retriever(search_kwargs={"k":2})

prompt=PromptTemplate(template="""you are a ITIL Problem manager, Answer from the context, if context is insufficient then directly say I don't know {context} Question {question}""",
               input_variable=['context', 'question'])

#question='Could you please tell me step by step how this problem "Life Cornerstone Intermittent Log In Errors"  is closed and its root cause? '


st.title("Simple chatbot")
question=st.text_input("Enter your question:")
context=retriever.invoke(question)

model=ChatOpenAI(model='gpt-3.5-turbo')
final=prompt.invoke({'question':question,'context':context})


if question:
    response=model.invoke(final)
    st.write(response.content)