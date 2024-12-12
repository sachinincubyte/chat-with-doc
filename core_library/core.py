class ChatWithDocCore:
    def __init__(self):
        self.documents = {}

    def add_document(self, doc_id, content):
        self.documents[doc_id] = content

    def remove_document(self, doc_id):
        if doc_id in self.documents:
            del self.documents[doc_id]

    def get_document(self, doc_id):
        return self.documents.get(doc_id, None)

    def ask(self, doc_id, question):
        document = self.get_document(doc_id)
        if document:
            return self._process_question(document, question)
        return "Document not found."

    def _process_question(self, document, question):
        # Placeholder for the actual implementation of question processing
        return f"Processing question: {question} on document: {document}"
