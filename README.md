# 🤖 StudyMate AI

## 📌 Project Overview

StudyMate AI is a document-based AI study assistant that lets students upload study material in PDF format and ask questions about its content.

The application extracts and chunks the PDF text, generates embeddings using Sentence Transformers, retrieves the most relevant information for each question, and uses Google Gemini to generate a grounded answer.

The project was built to understand and implement the core workflow of a RAG-based question-answering system, from document processing and retrieval to conversation handling, error handling, caching, and deployment.

---

## 🚀 Live Demo

https://studymate-ai-q49m45cvhv6o66aldvylh3.streamlit.app/

---

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

---

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
```

### 🔍 Workflow Explanation

**1. PDF Upload**  
The user uploads a study material PDF through the Streamlit interface.

**2. Text Extraction**  
Text is extracted from the PDF using PyPDF.

**3. Text Chunking**  
The extracted text is divided into smaller overlapping chunks to make retrieval more effective.

**4. Embeddings Generation**  
Each text chunk is converted into a numerical vector using the `all-MiniLM-L6-v2` Sentence Transformer model.

**5. User Question**  
The user enters a question related to the uploaded study material.

**6. Relevant Chunk Retrieval**  
The question is converted into an embedding and compared with the document embeddings. The top 3 most relevant chunks are retrieved.

**7. Context Construction**  
The retrieved chunks are combined with the user's question and recent conversation history to provide context for the AI model.

**8. Answer Generation**  
Google Gemini receives the constructed context and generates the answer.

**9. Final Answer**  
The generated response is displayed to the user through the Streamlit interface.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- PyPDF
- Sentence Transformers
- NumPy
- Google Gemini API
- Git
- GitHub
- Streamlit Community Cloud

---

## 🧠 RAG-Based Approach

StudyMate AI follows a Retrieval-Augmented Generation (RAG-style) workflow.

Instead of directly asking the AI model to answer from general knowledge, the application first retrieves relevant information from the uploaded study material and provides that information as context to the Gemini model.

This helps the application generate answers grounded in the user's uploaded document.

---

## 💻 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/VijayThakur01/StudyMate-AI.git
cd StudyMate-Ai
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API Key

Create a Google Gemini API key and set it as the `GOOGLE_API_KEY` environment variable.

The application reads the API key from the `GOOGLE_API_KEY` environment variable. Never hard-code your API key in `app.py` or commit it to GitHub.

**For Windows PowerShell:**

```powershell
$env:GOOGLE_API_KEY="YOUR_API_KEY"
```

> ⚠️ Replace `YOUR_API_KEY` with your actual API key only in your local environment. Do not put your real API key in this README or upload it to GitHub.

### 5. Run the Application

```powershell
python -m streamlit run app.py
```

The application will open in the browser.

---

---

## ☁️ Deployment

StudyMate AI is deployed using Streamlit Community Cloud.

### Deployment Steps

1. Push the project to a GitHub repository.
2. Connect the GitHub repository to Streamlit Community Cloud.
3. Select `app.py` as the main application file.
4. Add the `GOOGLE_API_KEY` as a secret in the Streamlit Community Cloud settings.
5. Deploy the application.

The deployed application can be accessed through the Live Demo link provided above.

> 🔐 API keys and other secrets should be stored using Streamlit's secrets management and should never be committed to the GitHub repository.


## 📁 Project Structure

```text
StudyMate-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

> `venv/` is used for the local Python virtual environment and is excluded from Git using `.gitignore`.

---

## 🎯 Project Objective

The main objective of StudyMate AI is to build a practical AI-powered study assistant while understanding the core concepts behind document-based question answering, including text extraction, chunking, embeddings, similarity-based retrieval, prompt construction, conversation handling, caching, error handling, and deployment.

---

## 📌 Future Improvements

- Improve retrieval accuracy using normalized cosine similarity
- Add support for more document formats
- Improve conversational context handling
- Add better user interface features
- Improve retrieval and answer evaluation
- Add more advanced RAG techniques

---

## 👨‍💻 Author

**Vijay Kumar Thakur**

GitHub: https://github.com/VijayThakur01

---

⭐ If you find this project useful, consider giving it a star!