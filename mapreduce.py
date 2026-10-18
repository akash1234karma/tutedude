from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model='gpt-4o')

loader=PyPDFLoader('sample-text-only-pdf-a4-size.pdf')
docs=loader.load()
splitter=RecursiveCharacterTextSplitter(chunk_size=2000,chunk_overlap=200)
data=splitter.split_documents(docs)

initial_prompt=PromptTemplate(template='write a concise summary od the following text \n {text}', input_variable=['text'])
refine_prompt=PromptTemplate(template='you current is {existing_answer} now refine and improve by using following next text:{text} Provide and updated improved summary that includes imp details from both old and new text', input_variable=['existing_text','text'])

chain=load_summarize_chain(llm=model,chain_type='refine',question_prompt=initial_prompt,refine_prompt=refine_prompt, verbose=True)
response=chain.run(data)
response