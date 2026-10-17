from langchain_community.tools import StructuredTool
from pydantic import BaseModel ,Field


class MultiplyInput(BaseModel):
    a: int=Field(required=True, description="First num to add")
    b: int=Field(required=True, description="Second num to add")

def multiple_func(a: int, b:int)->int:
    return a*b

multiple_tool=StructuredTool.from_function(
    func=multiple_func,
    name="multiply",
    description="Multiple two numbers",
    args_schema=MultiplyInput
)

result=multiple_tool.invoke({'a':3,'b':3})
print(result)
print(multiple_tool.name)