import os
import streamlit as st
from dotenv import load_dotenv

from html_template import css, user_template, bot_template, source_template

from src.pdf_loader import load_pdf_documents
from src.chunk_splitter import split_documents
from src.vector_db import (
    check_qdrant_connection,
    create_vector_db,
    load_vector_db,
    reset_vector_db,
)
from src.llm import (
    DEFAULT_GEMINI_MODEL,
    DEFAULT_HUGGINGFACE_MODEL,
    DEFAULT_OLLAMA_MODEL,
    get_llm,
)
from src.rag import ask_question


load_dotenv('key1.env')

st.set_page_config(
    page_title="Research Lens",
    layout="wide"
)

st.write(css, unsafe_allow_html=True)

UPLOAD_DIR = "data"
QDRANT_ERROR = "Qdrant is not running. Please start it with Docker first."
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_uploaded_files(uploaded_files):
    pdf_paths = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        pdf_paths.append(file_path)

    return pdf_paths


def initialize_session():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "vectorstore_ready" not in st.session_state:
        st.session_state.vectorstore_ready = False

    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None


initialize_session()


with st.sidebar:
    st.title("Research Helper")
    qdrant_connected = check_qdrant_connection()

    if not qdrant_connected:
        st.error(QDRANT_ERROR)

    uploaded_files = st.file_uploader(
        "Upload research PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:
        names_html = "".join(
            f'<div class="selected-file-item">{uploaded_file.name}</div>'
            for uploaded_file in uploaded_files
        )
        st.markdown(
            f'<div class="selected-file-list">{names_html}</div>',
            unsafe_allow_html=True,
        )

    llm_provider = st.selectbox(
        "LLM provider",
        ["huggingface", "ollama", "gemini"]
    )

    if llm_provider == "ollama":
        llm_model = st.text_input(
            "Ollama LLM model",
            value=DEFAULT_OLLAMA_MODEL,
            key="ollama_llm_model",
        )
    elif llm_provider == "huggingface":
        llm_model = st.text_input(
            "Hugging Face LLM model",
            value=DEFAULT_HUGGINGFACE_MODEL,
            key="huggingface_llm_model",
        )
    else:
        llm_model = st.text_input(
            "Gemini LLM model",
            value=DEFAULT_GEMINI_MODEL,
            key="gemini_llm_model",
        )

    k = st.slider(
        "Number of retrieved chunks",
        min_value=3,
        max_value=10,
        value=5
    )

    process_button = st.button("Process PDFs")

    reset_button = st.button("Reset Vector DB")

    if reset_button:
        if not qdrant_connected:
            st.error(QDRANT_ERROR)
        else:
            st.session_state.vectorstore = None
            reset_vector_db()
            st.session_state.vectorstore_ready = False
            st.session_state.chat_history = []
            st.success("Qdrant collection reset successfully.")

    if process_button:
        if not uploaded_files:
            st.warning("Please upload at least one PDF.")
        elif not qdrant_connected:
            st.error(QDRANT_ERROR)
        else:
            with st.spinner("Processing PDFs..."):
                try:
                    st.session_state.vectorstore = None

                    pdf_paths = save_uploaded_files(uploaded_files)

                    documents = load_pdf_documents(pdf_paths)

                    chunks = split_documents(documents)

                    vectorstore = create_vector_db(chunks)

                    st.session_state.vectorstore = vectorstore
                    st.session_state.vectorstore_ready = True

                    st.success(f"Processed {len(uploaded_files)} PDFs")
                    st.info(f"Created {len(chunks)} chunks")
                except ConnectionError:
                    st.session_state.vectorstore_ready = False
                    st.error(QDRANT_ERROR)
                except Exception as exc:
                    st.session_state.vectorstore_ready = False
                    st.error(f"Failed to process PDFs: {exc}")


st.markdown(
    """
    <div class="top-bar" style="display:none;"></div>

    <div class="hero-shell">
        <h1 class="hero-title"><span style="background: linear-gradient(90deg, #b38bff 0%, #8ec5ff 48%, #e4d8ff 100%); -webkit-background-clip: text; background-clip: text; color: transparent;">AI</span> Research Lens</h1>
        <div class="hero-divider"></div>
        <div class="hero-copy">Upload one or more research papers,<br>then ask questions about them.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(
            user_template.replace("{{MSG}}", message["content"]),
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            bot_template.replace("{{MSG}}", message["content"]),
            unsafe_allow_html=True
        )

        if message.get("sources"):
            sources_html = "<br>".join(message["sources"])
            st.markdown(
                source_template.replace("{{SOURCES}}", sources_html),
                unsafe_allow_html=True
            )


question = st.chat_input("Ask a question about your uploaded research papers...")

if question:
    st.session_state.chat_history.append({
        "role": "user",
        "content": question
    })

    st.markdown(
        user_template.replace("{{MSG}}", question),
        unsafe_allow_html=True
    )

    if not st.session_state.vectorstore_ready:
        st.warning("Please upload and process PDFs first.")
    elif not check_qdrant_connection():
        st.error(QDRANT_ERROR)
    else:
        with st.spinner("Thinking..."):
            try:
                vectorstore = load_vector_db()
                st.session_state.vectorstore = vectorstore
                llm = get_llm(
                    provider=llm_provider,
                    model_name=llm_model,
                )

                answer, sources = ask_question(
                    vectorstore=vectorstore,
                    llm=llm,
                    question=question,
                    k=k
                )

                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })

                st.markdown(
                    bot_template.replace("{{MSG}}", answer),
                    unsafe_allow_html=True
                )

                sources_html = "<br>".join(sources)
                st.markdown(
                    source_template.replace("{{SOURCES}}", sources_html),
                    unsafe_allow_html=True
                )
            except ConnectionError:
                st.error(QDRANT_ERROR)
            except Exception as exc:
                st.error(f"Failed to answer question: {exc}")