import getpass
import os
from functools import wraps
from time import process_time
from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores.pgvector import PGVector
from langchain.chains import RetrievalQA

import warnings
warnings.filterwarnings('ignore')

MODEL_ID           = "codellama" #llama2
CONNECTION_STRING  = "postgresql+psycopg2://postgres:test@localhost:5432/vectordb"
COLLECTION_NAME    = "kbase"
DOCS_PATH          = "./kb"
OLLAMA_SERVICE_URL = 'http://localhost:11434'

def measure(func):
    """
    Realiza la medición del tiempo de ejecución total en milisegundos de las funciones
    que forman parte del procesamiento con LLM
    """
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(process_time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(process_time() * 1000)) - start
            print(f"Total execution time {func.__name__}: {end_ if end_ > 0 else 0} ms")
    return _time_it

@measure
def question_and_answer(qachain, question):
    TEMPLATE = """
    Contexto: Limitar las respuestas al contexto proporcionado. 
    Instrucciones: Utilizar solo español.
    Responder la siguiente pregunta {question}
    """
    result = qachain.invoke({"query": question})
    print(result['result'])

    return result['result']
    
@measure
def main():
    print("Copyright(c) 2024. IA LLM\n\nIngrese su consulta sobre KB (SIGO)\nIngrese 'salir' para finalizar la conversacion.\n")
    ollama = Ollama(base_url = OLLAMA_SERVICE_URL, model = MODEL_ID)
    ollama_emb = OllamaEmbeddings(base_url = OLLAMA_SERVICE_URL, model = MODEL_ID)
    #
    ## Define la base de datos vectorizads con la informacion
    ## personalizada.
    #
    vectorstore = PGVector(
            collection_name    = COLLECTION_NAME,
            connection_string  = CONNECTION_STRING,
            embedding_function = ollama_emb)
    #
    # Especifica la cadena de pasos para recuperar la respuesta
    #
    qachain = RetrievalQA.from_chain_type(
            llm       = ollama, 
            retriever = vectorstore.as_retriever(
                search_kwargs = {"k": 10}
            )
    )

    while True:
        question = input("\nPregunta: ")
        if question == 'salir':
            break
        question_and_answer(qachain, question)

if __name__ == "__main__":
    main()
