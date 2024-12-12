# Chat with Doc

## Introduction

Welcome to the Chat with Doc project! This project aims to create a robust application for chatting with any type of document. The application is designed to be a plug-and-play module that can be easily integrated into various tech stacks. Our goal is to provide a seamless experience for developers by offering SDKs for multiple languages, starting with Python and JavaScript.

## Philosophy

The core philosophy of this project is to create a flexible and scalable solution that can be used across different programming languages and platforms. By developing a core library with language-specific wrappers, we ensure that the main functionality is centralized and easy to maintain. This approach also allows for easier updates and scalability in the future.

## Core Library Setup

To set up the core library, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/sachinincubyte/chat-with-doc.git
   cd chat-with-doc
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the core library:
   ```bash
   python core_library/core.py
   ```

## Using the Python SDK

To use the Python SDK, follow these steps:

1. Install the Python SDK:
   ```bash
   pip install chat-with-doc-python-sdk
   ```

2. Import the SDK in your Python application:
   ```python
   from chat_with_doc_python_sdk import ChatWithDoc

   chat = ChatWithDoc()
   response = chat.ask("What is the capital of France?")
   print(response)
   ```

## Using the JavaScript SDK

To use the JavaScript SDK, follow these steps:

1. Install the JavaScript SDK:
   ```bash
   npm install chat-with-doc-js-sdk
   ```

2. Import the SDK in your JavaScript application:
   ```javascript
   const ChatWithDoc = require('chat-with-doc-js-sdk');

   const chat = new ChatWithDoc();
   chat.ask("What is the capital of France?")
       .then(response => console.log(response))
       .catch(error => console.error(error));
   ```
