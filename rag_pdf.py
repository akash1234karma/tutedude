''''from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage,SystemMessage
from dotenv import load_dotenv
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
import streamlit as st

load_dotenv()

st.title("RAG + history chat")'''


from langchain_community.tools import ShellTool
shell_tool=ShellTool()
result=shell_tool.invoke("whoami")
print(result)