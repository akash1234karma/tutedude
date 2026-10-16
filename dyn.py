from langchain_core.prompts import  ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model='gpt-3.5-turbo')
domain=input("Domain:" )
query=input("Query:" )


message=ChatPromptTemplate.from_messages([('system','''You are an expert in the {domain} and have been helping people'''),
                                   ('human','''help me with explaining {query} in less than 50 words''')])

prompt=message.invoke({'domain':domain, 'query':query})

response=model.invoke(prompt)
print(response.content)

