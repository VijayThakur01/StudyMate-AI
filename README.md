# 🤖 StudyMate AI

StudyMate AI is an AI-powered study assistant that allows students to upload their study material in PDF format and ask questions based on the uploaded content.

The application extracts text from the PDF, divides it into smaller chunks, creates embeddings for those chunks, retrieves the most relevant information for a question, and uses Google Gemini to generate a clear answer.

## 🚀 Live Demo

https://studymate-ai-q49m45cvhv6o66aldvylh3.streamlit.app/

## ✨ Features

- 📄 Upload study material in PDF format
- 🔍 Extract text from uploaded PDFs
- 🧩 Divide large text into smaller chunks
- 🧠 Generate embeddings using Sentence Transformers
- 🎯 Retrieve the most relevant chunks for a question
- 🤖 Generate answers using Google Gemini
- 💬 Maintain conversation history
- 🔄 Handle follow-up questions using previous conversation context
- ⚡ Cache models, PDF processing, and embeddings for better performance
- 🛡️ Handle missing API keys and unreadable PDFs
- ☁️ Deployed online using Streamlit Community Cloud

## 🔄 How It Works

```text
PDF Upload
    ↓
Text Extraction
    ↓
Text Chunking
    ↓
Embeddings Generation
    ↓
Question
    ↓
Relevant Chunks Retrieval
    ↓
Context + Question
    ↓
Google Gemini
    ↓
AI Answer

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


