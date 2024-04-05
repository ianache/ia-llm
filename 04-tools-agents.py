from langchain.agents import tool
from langchain_community.chat_models import ChatOllama
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_structured_chat_agent
#from langchain.agents.format_scratchpad.
from langchain_core.messages import HumanMessage


MODEL_ID           = "codellama"

@tool
def query_cars(model: str) -> dict:
    """Fetch all cars available by car model"""
    return {'id': 1, 'estado': 'CANCELADA'}

def chat_humman_message(llm):
    messages = [
      HumanMessage(
        content="What color is the sky at different times of the day? Respond using JSON"
      )
    ]
    chat_model_response = llm.invoke(messages)
    print(chat_model_response)

import json

def chat_prompt(llm):
    json_schema = {
            "title": "Person",
            "description": "Identifying information about a person",
            "type": "object",
            "properties": {
                "name": {"title": "Name", "description": "The person's name", "type": "string"},
                "age": {"title": "Age", "description": "The person's age", "type": "integer"},
                "fav_food": {
                    "title": "Fav Food",
                    "description": "The person's favorite food",
                    "type": "string",
                },
            },
            "required": ["name", "age"],
    }
    messages = [
            HumanMessage(content = "Please tell me about the person using the following JSON schema:"),
            HumanMessage(content = "{dumps}"),
            HumanMessage(content = "Now, considering th schema, tell me about a person named Jhon who is 35 years old and loves pizza")
    ]

    prompt = ChatPromptTemplate.from_messages(messages)
    dumps  = json.dumps(json_schema, indent = 2)
    chain  = prompt | llm | StrOutputParser()

    print(chain.invoke({"dumps": dumps}))


if __name__ == '__main__':
    llm = ChatOllama(model = MODEL_ID, format = "json", temperature = 0)
    
    #chat_humman_message(llm)
    chat_prompt(llm)

    #wikipedia = WikipediaQueryRun(api_wrapper = WikipediaAPIWrapper())
    #
    #tools = [query_cars, wikipedia]
    #prompt = ChatPromptTemplate.from_messages([
    #    ( "system", """
    #    You are a very powerful assistant for travel planning, your final result should be user-friendly for their visit.
    #    You can use the tool 'query_cars' to fetch all possible cars availables.
    #    You can use the tool 'wikipedia' to search on wikipedia for travels in peru. 
    #    """),
    #    ("user", "{input}"),
    #    MessagesPlaceholder(variable_name = "agent_scratchpad")
    #])
    #
    #agent_chain = create_structured_chat_agent(llm, tools, prompt)
    #
    #llm_with_tools = llm.bind_tools(tools)
    #agent = (
    #        { 
    #            "input": lambda x: x["input"],
    #            "agent_scratchpad": lambda x: format_to_llama_tool_message(x["intermediate_steps"])
    #        }
    #        | prompt
    #        | llm_with_tools
    #        | StrOutputParser
    #)

    #agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)
    #list(agent_executor.stream({"input": "Find a travel from Lima (Peru) to Arequipa (Peru)"}))
