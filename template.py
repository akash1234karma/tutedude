from langchain_core.prompts import PromptTemplate

template=PromptTemplate(template="""you are a Senior {role} working in company, you always have a {goal} in mind and you have {context} """, input_variable=['role','goal','context'])

template.save('promptT.json')