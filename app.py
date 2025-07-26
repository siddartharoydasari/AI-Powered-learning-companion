import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load Gemini API key
load_dotenv()
GEMINI_API_KEY =("AIzaSyBTXbOpIVuvwnmU-NYSkXMB2J46L4sAwjE")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


st.set_page_config(page_title="AI Learning Companion", layout="centered")
st.title("📚 AI-Powered Learning Companion")

st.markdown("""
This app helps you understand code and technical concepts.
Choose a mode:
- **Explain Simply**: Breaks down complex code or concepts.
- **Quiz Me**: Generates quiz questions.
- **Debug This**: Identifies and explains issues in your code.
""")

# Mode selection
mode = st.selectbox("Choose a mode:", ["Explain Simply", "Quiz Me", "Debug This"])

# Input box
user_input = st.text_area("Enter code or concept:", height=300)

# Prompt templates
PROMPTS = {
    "Explain Simply": "You are a friendly teacher. Explain the following concept or code in simple terms, like you're teaching a beginner:\n\n{input}",
    "Quiz Me": "You are a tutor. Create 3 quiz questions (MCQ or short answer) based on the following content:\n\n{input}",
    "Debug This": "You are an expert developer. Analyze the following code and identify any bugs or logic issues. Explain clearly what the issues are and suggest fixes:\n\n{input}"
}

if st.button("🤖 Generate Response"):
    if not user_input.strip():
        st.warning("Please enter some input.")
    else:
        with st.spinner("Thinking..."):
            prompt = PROMPTS[mode].format(input=user_input)
            try:
                response = model.generate_content(prompt)
                st.markdown("### 🧠 AI Response")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error during Gemini API call: {e}")
