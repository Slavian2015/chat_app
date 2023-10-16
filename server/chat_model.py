from llama_index import GPTVectorStoreIndex
from llama_index import SimpleDirectoryReader
from llama_index import StorageContext
from llama_index import load_index_from_storage


def create_storage_context():
    documents = SimpleDirectoryReader('docs').load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    index.storage_context.persist()
    return index


def rebuild_storage_context():
    storage_context = StorageContext.from_defaults(persist_dir='./storage')
    index = load_index_from_storage(storage_context)
    return index


# index = create_storage_context()
index = rebuild_storage_context()
query_engine = index.as_query_engine()
result = query_engine.query("How can I test more data in Forex Tester?")

print(result)