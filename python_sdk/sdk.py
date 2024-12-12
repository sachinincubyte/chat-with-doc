from core_library.core import ChatWithDocCore

class ChatWithDoc:
    def __init__(self):
        self.core = ChatWithDocCore()

    def add_document(self, doc_id, content):
        self.core.add_document(doc_id, content)

    def remove_document(self, doc_id):
        self.core.remove_document(doc_id)

    def get_document(self, doc_id):
        return self.core.get_document(doc_id)

    def ask(self, doc_id, question):
        return self.core.ask(doc_id, question)
