from llama_index import GPTVectorStoreIndex
from llama_index import SimpleDirectoryReader


def create_storage_context():
    documents = SimpleDirectoryReader('docs').load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    index.storage_context.persist()


if __name__ == "__main__":
    create_storage_context()
