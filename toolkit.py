from langchain_core.tools import tool
@tool
def add(a:int, b:int) ->int:
    """Adding two number"""
    return a+b
@tool
def multi(a:int, b:int) ->int:
    """Multiple two number"""
    return a*b

class MathToolkit:
    def get_tool(self):
        return[add,multi]

toolkit=MathToolkit()
tools=toolkit.get_tool()

for tool in tools:
    print(tool.name, "->" ,tool.description)


