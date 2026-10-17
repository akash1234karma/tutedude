import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
load_dotenv()

model=ChatOpenAI(model='gpt-3.5-turbo')
prompt=ChatPromptTemplate.from_template('''Answer from the following context only. Please provide the most accurate result based on the context only {context} Question:{input}''')

def generate_embeddings():
    if 'vectors' not in st.session_state:
        st.session_state.embeddings=OpenAIEmbeddings()
        st.session_state.loader=PyPDFDirectoryLoader('DATA')
        st.session_state.docs=st.session_state.loader.load()
        st.session_state.splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.splitted=st.session_state.splitter.split_documents(st.session_state.docs)
        st.session_state.vectors=FAISS.from_documents(st.session_state.splitted, embedding=OpenAIEmbeddings())
        st.write("Vector database is ready")

st.title("CHATBOT")
st.write('Plesae check the button below to add embedding of your personal data')

if st.button("Generate embedding"):
    generate_embeddings()

user_prompt=st.text_input("Enter your query from uploaded docs")

if st.button("Answer"):
    if user_prompt:
        document_context=create_stuff_documents_chain(model,prompt)
        retriever=st.session_state.vectors.as_retriever()
        retrieved_data=create_retrieval_chain(retriever,document_context)
        response=retrieved_data.invoke({'input':user_prompt})

        st.write("Answer")
        st.write(response['answer'])
        with st.expander("Context from the document"):
            if "context" in response:
                for i, doc in enumerate(response['context']):
                    st.write(doc.page_content)
                    st.write("------------")