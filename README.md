# 🤖 StudyMate AI

## 📌 Project Overview

StudyMate AI is a document-based AI study assistant that lets students upload study material in PDF format and ask questions about its content.

The application extracts and chunks the PDF text, generates embeddings using Sentence Transformers, retrieves the most relevant information for each question, and uses Google Gemini to generate a grounded answer.

The project was built to understand and implement the core workflow of a RAG-based question-answering system, from document processing and retrieval to conversation handling, error handling, caching, and deployment.

## 🚀 Live Demo

https://studymate-ai-q49m45cvhv6o66aldvylh3.streamlit.app/

## ✨ Features

- 📄 Upload study material in PDF format
- 🔍 Extract text from uploaded PDF documents
- 🧩 Split extracted text into smaller overlapping chunks
- 🧠 Generate text embeddings using Sentence Transformers
- 🎯 Retrieve the top relevant chunks for each question
- 🤖 Generate grounded answers using Google Gemini
- 💬 Maintain conversation history during the session
- 🔄 Support follow-up questions using previous conversation context
- ⚡ Cache the embedding model, PDF processing, and embeddings for better performance
- 🛡️ Handle missing API keys and unreadable PDFs gracefully
- ☁️ Deploy and run the application online using Streamlit Community Cloud

## 🔄 How It Works

StudyMate AI processes the uploaded study material through the following workflow:

```text
1. PDF Upload
      ↓
2. Text Extraction using PyPDF
      ↓
3. Text Chunking
      ↓
4. Embeddings Generation
      ↓
5. User Question
      ↓
6. Relevant Chunk Retrieval
      ↓
7. Context + Question + Conversation History
      ↓
8. Google Gemini
      ↓
9. Grounded AI Answer

🛠️ Technologies Used
Python
Streamlit
PyPDF
Sentence Transformers
NumPy
Google Gemini API
Git
GitHub
Streamlit Community Cloud
🧠 RAG-Based Approach

StudyMate AI follows a Retrieval-Augmented Generation (RAG-style) workflow.

Instead of directly asking the AI model to answer from general knowledge, the application first retrieves relevant information from the uploaded study material and provides that information as context to the Gemini model.

This helps the application generate answers grounded in the user's uploaded document.

💻 Run Locally
1. Clone the repository
git clone https://github.com/VijayThakur01/StudyMate-AI.git
cd StudyMate-Ai
2. Create and activate a virtual environment
python -m venv venv

Windows PowerShell:

.\venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Configure Gemini API Key

Create a Google Gemini API key and set it as the GOOGLE_API_KEY environment variable.

For Windows PowerShell:

$env:GOOGLE_API_KEY="YOUR_API_KEY"

Do not upload or expose your API key publicly.

5. Run the application
python -m streamlit run app.py

The application will open in the browser.

📁 Project Structure
StudyMate-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/

venv/ is used for the local Python virtual environment and is excluded from Git using .gitignore.

🎯 Project Objective

The main objective of StudyMate AI is to build a practical AI-powered study assistant while understanding the core concepts behind document-based question answering, including text extraction, chunking, embeddings, similarity-based retrieval, prompt construction, conversation handling, caching, error handling, and deployment.

📌 Future Improvements
Improve retrieval accuracy using normalized cosine similarity
Add support for more document formats
Improve conversational context handling
Add better user interface features
Improve retrieval and answer evaluation
Add more advanced RAG techniques
👨‍💻 Author

Vijay Kumar Thakur

GitHub: https://github.com/VijayThakur01

⭐ If you find this project useful, consider giving it a star!


