# Import Streamlit and give it the short name "st"
# Streamlit is used to build the web application UI
import streamlit as st

# Import our PDF text extraction function
# This reads the uploaded PDF and returns its text
from utils.pdf_loader import extract_text_from_pdf

# Import the text chunking function
# This splits large documents into smaller pieces
from utils.text_chunker import chunk_text

# Import vector database functions
# create_vector_store -> stores embeddings in ChromaDB
# search_vector_store -> finds relevant chunks for a question
from utils.vector_store import create_vector_store, search_vector_store


# Configure the Streamlit page settings
st.set_page_config(
    page_title="FinSight AI",
    page_icon="📊",
    layout="wide"
)

# Main title shown at the top of the application
st.title("FinSight AI")

# Smaller subtitle below the title
st.subheader("Multi-Agent Financial Research Platform")


# Create a file upload widget
# Only PDF files can be uploaded
uploaded_file = st.file_uploader(
    "Upload Annual Report",
    type=["pdf"]
)


# Check whether the user has uploaded a PDF
# Everything below runs only after a file is uploaded
if uploaded_file:

    # Extract all text from the PDF
    # The result is one large string containing the report text
    text = extract_text_from_pdf(uploaded_file)

    # Display a success message
    st.success("PDF uploaded successfully")

    # Section heading
    st.subheader("Extracted Text Preview")

    # Display the first 3000 characters of the report
    # This prevents huge reports from flooding the screen
    st.text_area(
        "Preview",
        text[:3000],
        height=300
    )

    # Split the report into smaller chunks
    # Large documents must be broken into pieces before embedding
    chunks = chunk_text(text)

    # Display how many chunks were created
    st.success(f"Created {len(chunks)} chunks")

    # Show the first chunk for debugging and understanding
    st.subheader("First Chunk")

    # chunks[0] means the first item in the chunks list
    st.write(chunks[0])

    # Create the vector database
    # Each chunk is converted into an embedding and stored
    collection = create_vector_store(chunks)

    # Confirm the vector database was created
    st.success("Vector database created")

    # Create a text input box for user questions
    question = st.text_input(
        "Ask a question about the annual report"
    )

    # Check if the user entered a question
    if question:

        # Convert the question into an embedding
        # Search the vector database for the most similar chunks
        relevant_chunks = search_vector_store(
            collection,
            question
        )

        # Display section heading
        st.subheader("Most Relevant Source Chunks")

        # Loop through each retrieved chunk
        for chunk in relevant_chunks:

            # Display the chunk text
            st.write(chunk)

            # Add a horizontal divider for readability
            st.divider()