# app.py

import streamlit as st
from vector import add_files_to_vectorstore, get_context_for_query
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialize model and prompt
llm = OllamaLLM(model="llama3.2")
template = """You are a helpful assistant. Answer the following question based on the provided context.
Context: {context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm

st.set_page_config(page_title="🧠 Chat with Your Documents")
st.title("📚 Chat with Your Uploaded Documents")

# File uploader
st.sidebar.header("📤 Upload Documents")
uploaded_files = st.sidebar.file_uploader("Supported: pdf, txt, docx, csv, pptx, images", type=["pdf", "txt", "csv", "docx", "pptx", "png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    success = add_files_to_vectorstore(uploaded_files)
    if success:
        st.sidebar.success("✅ Documents added to vector store.")
    else:
        st.sidebar.error("❌ Failed to extract text from files.")

# Chat interface
st.subheader("💬 Ask a Question")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your question here...", placeholder="e.g. What do the reviews say about the service?")

if user_input:
    with st.spinner("🤖 Thinking..."):
        context = get_context_for_query(user_input)
        answer = chain.invoke({"context": context, "question": user_input})

    # Display chat
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", answer))

# Display full chat history
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
