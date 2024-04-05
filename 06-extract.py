import json
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain.chains import create_extraction_chain
from time import process_time
from langchain_community.llms import Ollama

MODEL_ID = "codellama" #llama2 mistral

if __name__ == '__main__':
    # Schema
    schema = {
            "properties": {
                "first name": {"type": "string"},
                "middle name": { "type": "string" },
                "last name": { "type": "string" },
                "height": {"type": "integer"},
                "hair_color": {"type": "string"},
            },
            "required": ["first name", "height"],
    }
    # Input
    input = """Ilver Anache mide 1.6 metros de altura, Ximena 1.3 metros de altura y Nicole mide 30 centimetros mas que Ximena. Ilver tiene el pelo color negro, ximena blanco y nicole castanio"""

    # Run chain
    llm = OllamaFunctions(model = "mistral", temperature=0)
    chain = create_extraction_chain(schema, llm)

    data  = chain.invoke(input)
    json_str = json.dumps(data, indent=4)

    print(json_str)
