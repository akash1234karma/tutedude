from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_classic.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model='gpt-4o')
loader=PyPDFLoader('sample-text-only-pdf-a4-size.pdf')
docs=loader.load()

prompt=PromptTemplate(template='Write a detailed summary of the following text :\n {text}', input_variables=['text'])
chain=load_summarize_chain(llm=model, chain_type='stuff',prompt=prompt, verbose=True)

response=chain.run(docs)
print(response)