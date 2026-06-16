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

from agents.rag_agent import answer_question

# import stock data function
from agents.stock_agent import get_stock_data

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

        # Search the vector database for the most relevant chunks
        # The question is converted into an embedding and compared
        # against all document chunk embeddings
        relevant_chunks = search_vector_store(
            collection,
            question
        )

        # Send the question and retrieved chunks to the llm
        # The llm will use the chunks as context to generate an answer
        answer = answer_question(
            question,
            relevant_chunks
        )

        # Display a heading for the generated answer
        st.subheader("AI Answer")

        # Display the llm response
        st.write(answer)

        # Display a heading for the retrieved source chunks
        st.subheader("Most Relevant Source Chunks")

        # Loop through each retrieved chunk
        for chunk in relevant_chunks:

            # Display the chunk text
            st.write(chunk)

            # Add a divider between chunks for readability
            st.divider()

       # create a horizontal divider
    # visually separates the rag section from stock analysis
    st.divider()

    # section heading
    st.header("Stock Comparison")

    # input for first company ticker
    # default value is apple
    ticker1 = st.text_input(
        "First Company Ticker",
        value="AAPL"
    )

    # input for second company ticker
    # default value is microsoft
    ticker2 = st.text_input(
        "Second Company Ticker",
        value="MSFT"
    )

    # button that starts the stock comparison
    if st.button("Compare Companies"):

        # get stock data for the first ticker
        company1 = get_stock_data(ticker1)

        # get stock data for the second ticker
        company2 = get_stock_data(ticker2)

        # create two columns
        # this lets us display both companies side by side
        col1, col2 = st.columns(2)

        # display first company
        with col1:

            # company name heading
            st.subheader(company1["company"])

            # display current stock price as a metric card
            st.metric("Stock Price", company1["price"])

            # display company market cap
            st.write("Market Cap:", company1["market_cap"])

            # display price-to-earnings ratio
            st.write("P/E Ratio:", company1["pe_ratio"])

            # display company sector
            st.write("Sector:", company1["sector"])

        # display second company
        with col2:

            # company name heading
            st.subheader(company2["company"])

            # display current stock price as a metric card
            st.metric("Stock Price", company2["price"])

            # display company market cap
            st.write("Market Cap:", company2["market_cap"])

            # display price-to-earnings ratio
            st.write("P/E Ratio:", company2["pe_ratio"])

            # display company sector
            st.write("Sector:", company2["sector"])