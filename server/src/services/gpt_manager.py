from src.services.interface import GPTInterface
from llama_index import StorageContext
from llama_index import load_index_from_storage


class GPTManager(GPTInterface):
    def __init__(self) -> None:
        storage_context = StorageContext.from_defaults(persist_dir='./storage')
        index = load_index_from_storage(storage_context)
        self.query_engine = index.as_query_engine()

    def get_gpt_answer(self, user_question: str) -> str:
        gpt_answer = self.query_engine.query(user_question)
        return f"""{gpt_answer}"""
