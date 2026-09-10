import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np
import os
import io
from google import genai


# -----------------------------------------
# Chat History Initialization
# -----------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# -----------------------------------------
# Streamlit Page Configuration
# -----------------------------------------

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------------------
# Sidebar
# -----------------------------------------

with st.sidebar:

    st.header("🤖 StudyMate AI")

    st.write(
        "Your AI-powered personal study assistant."
    )

    st.divider()

    st.subheader("📌 How to use")

    st.write("1. Upload a PDF")
    st.write("2. Ask a question")
    st.write("3. Get an AI-powered answer")

    st.divider()

    st.caption(
        "💡 StudyMate AI answers questions "
        "using your uploaded study material."
    )


# -----------------------------------------
# Load Embedding Model
# -----------------------------------------

@st.cache_resource
def load_embedding_model():

    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


embedding_model = load_embedding_model()


# -----------------------------------------
# Gemini API Key
# -----------------------------------------

api_key = os.getenv("GOOGLE_API_KEY")


if not api_key:

    st.error(
        "❌ GOOGLE_API_KEY is not set. "
        "Please configure your Gemini API key."
    )

    st.stop()


client = genai.Client(
    api_key=api_key
)


# -----------------------------------------
# Create Text Chunks
# -----------------------------------------

def create_chunks(
    text,
    chunk_size=1000,
    overlap=200
):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        if chunk.strip():

            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# -----------------------------------------
# Process PDF
# -----------------------------------------

@st.cache_data
def process_pdf(pdf_bytes):

    pdf_reader = PdfReader(
        io.BytesIO(pdf_bytes)
    )

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

    if not text.strip():

        return None, None

    chunks = create_chunks(
        text
    )

    return text, chunks


# -----------------------------------------
# Generate Embeddings
# -----------------------------------------

@st.cache_data
def generate_embeddings(
    chunks
):

    return embedding_model.encode(
        chunks
    )


# -----------------------------------------
# Find Most Relevant Chunks
# -----------------------------------------

def find_most_relevant_chunks(
    question,
    chunks,
    embeddings,
    model,
    top_k=3
):

    question_embedding = model.encode(
        question
    )

    similarities = np.dot(
        embeddings,
        question_embedding
    )

    top_indices = np.argsort(
        similarities
    )[-top_k:][::-1]

    relevant_chunks = []

    for index in top_indices:

        relevant_chunks.append(
            chunks[index]
        )

    return relevant_chunks


# -----------------------------------------
# Generate Answer using Gemini
# -----------------------------------------

def generate_answer(
    question,
    relevant_chunks,
    chat_history
):

    study_material = "\n\n".join(
        relevant_chunks
    )

    # Use only the last 5 conversations

    recent_history = chat_history[-5:]

    conversation = ""

    for chat in recent_history:

        conversation += f"""
Previous Question:
{chat["question"]}

Previous Answer:
{chat["answer"]}

"""

    prompt = f"""
You are StudyMate AI, a helpful study assistant.

Your task is to answer the user's question using the study
material and previous conversation provided below.

Instructions:

1. Use the study material as the primary source.

2. Use previous conversation to understand follow-up questions.

3. If the user uses words like "it", "its", "they", or "that",
   use the previous conversation to understand what they mean.

4. Combine information from all relevant chunks when necessary.

5. If the exact answer is not directly written but the provided
   information is clearly related, give the best answer that can
   be supported by the study material.

6. Do not invent facts that are not supported by the study material.

7. If there is genuinely no relevant information in the study
   material, say:
   "I could not find this information in the uploaded PDF."

8. Keep the answer clear, simple and useful for a student.


Previous Conversation:
{conversation}


Study Material:
{study_material}


Current Question:
{question}


Answer:
"""

    try:

        response = client.interactions.create(
            model="gemini-3.6-flash",
            input=prompt
        )

        return response.output_text

    except Exception as e:

        return (
            "❌ Sorry, I could not generate an answer "
            "because of a Gemini API error."
        )


# -----------------------------------------
# StudyMate AI UI
# -----------------------------------------

st.title("🤖 StudyMate AI")

st.caption(
    "📚 Your AI-powered personal study assistant"
)

st.write(
    "Upload your study material and ask questions to learn smarter."
)

st.divider()


# -----------------------------------------
# PDF Upload
# -----------------------------------------

st.header("📄 Upload Study Material")

st.write(
    "Upload your study material in PDF format "
    "and StudyMate AI will use it to answer your questions."
)

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
    help="Only PDF files are supported."
)


if uploaded_file is not None:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    # -----------------------------------------
    # Process PDF
    # -----------------------------------------

    pdf_bytes = uploaded_file.getvalue()

    text, chunks = process_pdf(
        pdf_bytes
    )

    if text is None:

        st.error(
            "❌ This PDF does not contain readable text."
        )

        st.stop()

    st.success(
        f"✅ PDF processed successfully — "
        f"{len(chunks)} text chunks created."
    )

    # -----------------------------------------
    # Generate Embeddings
    # -----------------------------------------

    embeddings = generate_embeddings(
        chunks
    )

    st.success(
        "🧠 Embeddings generated successfully."
    )

    # -----------------------------------------
    # PDF Processing Details
    # -----------------------------------------

    with st.expander(
        "📊 PDF Processing Details"
    ):

        st.write(
            f"🧩 Text chunks: {len(chunks)}"
        )

        st.write(
            f"🔢 Embedding shape: {embeddings.shape}"
        )

    # -----------------------------------------
    # View Chunks
    # -----------------------------------------

    with st.expander(
        "🧩 View chunks"
    ):

        for i, chunk in enumerate(chunks):

            st.write(
                f"### Chunk {i + 1}"
            )

            st.write(
                chunk
            )

    # -----------------------------------------
    # View Extracted Text
    # -----------------------------------------

    with st.expander(
        "📖 View extracted text"
    ):

        st.write(
            text
        )


# -----------------------------------------
# Ask Question
# -----------------------------------------

st.divider()

st.header("💬 Ask a Question")

st.write(
    "Ask anything related to the information in your uploaded PDF."
)

question = st.text_input(
    "Enter your question",
    placeholder="e.g. What is Python?"
)


if st.button("Find Answer"):

    if question:

        if uploaded_file is not None:

            relevant_chunks = find_most_relevant_chunks(
                question,
                chunks,
                embeddings,
                embedding_model
            )

            st.success(
                "Most relevant information found!"
            )

            # -----------------------------------------
            # Show Relevant Chunks
            # -----------------------------------------

            st.write(
                "### 🔎 Relevant Chunks"
            )

            for i, chunk in enumerate(
                relevant_chunks
            ):

                st.write(
                    f"#### Chunk {i + 1}"
                )

                st.write(
                    chunk
                )

            # -----------------------------------------
            # Generate Answer
            # -----------------------------------------

            answer = generate_answer(
                question,
                relevant_chunks,
                st.session_state.chat_history
            )

            # -----------------------------------------
            # Save Chat History
            # -----------------------------------------

            st.session_state.chat_history.append(
                {
                    "question": question,
                    "answer": answer
                }
            )

            # -----------------------------------------
            # Display Answer
            # -----------------------------------------

            st.write(
                "### 🤖 StudyMate AI Answer"
            )

            st.info(
                answer
            )

        else:

            st.warning(
                "Please upload a PDF first."
            )

    else:

        st.warning(
            "Please enter a question first."
        )


# -----------------------------------------
# Chat History
# -----------------------------------------

st.divider()

st.header(
    "💬 Chat History"
)


if st.session_state.chat_history:

    for i, chat in enumerate(
        st.session_state.chat_history
    ):

        with st.chat_message("user"):

            st.write(
                chat["question"]
            )

        with st.chat_message("assistant"):

            st.write(
                chat["answer"]
            )

else:

    st.info(
        "No questions asked yet. Ask your first question above!"
    )