from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_core.messages import HumanMessage

if __name__ == "__main__":
    model = OllamaFunctions(model="mistral")
    model = model.bind(
        functions=[
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, " "e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["location"],
            },
        }],
        function_call={"name": "get_current_weather"}
    )

    from langchain_core.messages import HumanMessage
    data = model.invoke("what is the weather in Boston?")
    print(data)
