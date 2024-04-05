from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_core.messages import HumanMessage

model = OllamaFunctions(temperture=0.1, model="mistral");

GET_CITAS = {
    "name": "get_citas",
    "description": "obtener datos de las citas",
    "parameters": {
        "type": "object",
        "properties": {
            "motor": {
                "type": "string",
                "description": "numero del motor"
            }
        },
        "required": ["motor"]
    }
}

if __name__ == "__main__":
    model.bind(
            functions = [ GET_CITAS ],
            function_call={"name": "get_citas"},
    )

    data = model.invoke("obtener datos de la cita para motor C1QA12345566")
