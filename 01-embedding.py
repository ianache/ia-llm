import getpass
import os
from functools import wraps
from time import process_time
from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores.pgvector import PGVector
from langchain.chains import RetrievalQA


#from dotenv import load_dotenv

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
def load_from_url(url):
    """
    Realizar la descarga del contenido desde una URL con acceso publico
    """
    print(f"Loading content from url: {url}")

    loader = WebBaseLoader(url)
    data = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 0)
    docs = text_splitter.split_documents(data)
    #print(docs)
    return data, docs

@measure
def load_from_glob(path):
    #loader = TextLoader(path)
    loader = DirectoryLoader(path)
    data   = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 0)
    docs = text_splitter.split_documents(data)
    return data, docs

@measure
def generate_embeddings( embeddings, docs, collection_name = COLLECTION_NAME):
    print(f"Generando embeddings into {collection_name}")
    print(docs)
    db_vector_store = PGVector.from_documents(
            embedding = embeddings,
            documents = docs,
            collection_name   = collection_name,
            connection_string = CONNECTION_STRING
    )
    return db_vector_store

@measure
def search_similarities(db, query):
    docs_with_score = db.similarity_search_with_score(query)
    for doc, score in docs_with_score:
        print("-" * 80)
        print("Score: ", score)
        print(doc.page_content)
        print("-" * 80)
    return docs_with_score

@measure
def search_similarities_max_marginal_relevance(db, query):
     docs_with_score = db.max_marginal_relevance_search_with_score(query)
     for doc, score in docs_with_score:
        print("-" * 80)
        print("Score: ", score)
        print(doc.page_content)
        print("-" * 80)
     return docs_with_score
 
@measure
def main():
    print("""
      Copyright(c) 2024. IA LLM
      Generando Base de Conocimientos personalizada.
      Procesando base en ruta './kb'
    """)

    ollama = Ollama(base_url = OLLAMA_SERVICE_URL, model = MODEL_ID)
    ollama_emb = OllamaEmbeddings(base_url = OLLAMA_SERVICE_URL, model = MODEL_ID) # "llama:7b",

    #data, docs = load_from_url(url = "https://www.gutenberg.org/files/1727/1727-h/1727-h.htm")
    data, docs = load_from_glob(f"{DOCS_PATH}")
    vector_store = generate_embeddings(ollama_emb, docs)

    #search_similarities(db, "What did the president say about Ketanji Brown Jackson")
    #question = "Para que sirve SIGO?"
    #search_similarities(vector_store, question)

if __name__ == "__main__":
    main()
