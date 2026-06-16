import streamlit as st

st.set_page_config(page_title="FinSight AI", layout="wide")

st.title("FinSight AI")
st.subheader("Multi-Agent Financial Research Platform")

st.write("Upload annual reports, ask financial questions, compare stocks, and evaluate AI answers.")

uploaded_file = st.file_uploader("Upload an annual report PDF", type=["pdf"])

question = st.text_input("Ask a question about the report")

if uploaded_file:
    st.success("PDF uploaded successfully.")

if question:
    st.write("Your question:", question)