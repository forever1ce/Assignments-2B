import streamlit as st
import tempfile
import os
import time

from pdf_reader import read_pdf
from chunker import chunk_pages
from embedder import create_embeddings, get_model
from retriever import build_index, search
from llm import ask_llm

st.set_page_config(page_title="RAG Chatbot", page_icon="📄")

st.title("📄 PDF RAG Chatbot")

# -----------------------------
# Session State
# -----------------------------
if "loaded" not in st.session_state:
    st.session_state.loaded = False

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("Options")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    if st.button("📄 Load New PDF"):
        st.session_state.loaded = False
        st.session_state.messages = []

        for key in ["chunks", "index", "model"]:
            if key in st.session_state:
                del st.session_state[key]

        st.rerun()

# -----------------------------
# Upload PDF
# -----------------------------
if not st.session_state.loaded:

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    if uploaded_file:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(uploaded_file.read())
            pdf_path = temp_pdf.name

        with st.spinner("Processing PDF..."):

            pages = read_pdf(pdf_path)

            chunks = chunk_pages(pages)

            embeddings = create_embeddings(chunks)

            index = build_index(embeddings)

            model = get_model()

        st.session_state.chunks = chunks
        st.session_state.index = index
        st.session_state.model = model
        st.session_state.loaded = True

        os.remove(pdf_path)

        st.success("✅ PDF Loaded!")

        st.rerun()

# -----------------------------
# Chat
# -----------------------------
if st.session_state.loaded:

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask a question...")

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                start = time.time()

                results = search(
                    st.session_state.index,
                    st.session_state.model,
                    st.session_state.chunks,
                    question
                )

                print(f"Search took: {time.time() - start:.3f} seconds")

                start = time.time()

                answer = ask_llm(question, results)

                print(f"LLM took: {time.time() - start:.3f} seconds")

                source_pages = sorted(
                    set(r["page"] for r in results)
                )

                final_answer = (
                    answer
                    + "\n\n---\n"
                    + "**📄 Source Pages:** "
                    + ", ".join(map(str, source_pages))
                )

                st.markdown(final_answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": final_answer
            }
        )