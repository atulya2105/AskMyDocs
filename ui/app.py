import streamlit as st
import requests

st.set_page_config(page_title="DocuChat AI", layout="wide")

st.title("📄 DocuChat AI Agent 🤖")

# Backend URL
BASE_URL = "http://127.0.0.1:8000"

# ----------------------
# Upload PDF
# ----------------------
st.header("📂 Upload PDF")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    if st.button("Upload"):
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        response = requests.post(f"{BASE_URL}/upload", files=files)

        if response.status_code == 200:
            st.success("✅ File uploaded & processed successfully!")
        else:
            st.error("❌ Upload failed")

# ----------------------
# Ask Question
# ----------------------
st.header("💬 Ask Questions")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("⚠️ Please enter a question")
    else:
        with st.spinner("Thinking... 🤔"):
            response = requests.get(f"{BASE_URL}/ask", params={"question": question})

            if response.status_code == 200:
                answer = response.json().get("answer", "")
                st.success("🤖 Answer:")
                st.write(answer)
            else:
                st.error("❌ Failed to get response")