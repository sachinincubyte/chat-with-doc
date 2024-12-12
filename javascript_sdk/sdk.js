const core = require('../core_library/core');

class ChatWithDoc {
    constructor() {
        this.core = new core.ChatWithDocCore();
    }

    addDocument(docId, content) {
        this.core.addDocument(docId, content);
    }

    removeDocument(docId) {
        this.core.removeDocument(docId);
    }

    getDocument(docId) {
        return this.core.getDocument(docId);
    }

    ask(docId, question) {
        return this.core.ask(docId, question);
    }
}

module.exports = ChatWithDoc;
