# import streamlit and give it the short name "st"
# streamlit is used to build the web application ui
import streamlit as st

# import our pdf text extraction function
# this reads the uploaded pdf and returns its text
from utils.pdf_loader import extract_text_from_pdf

# import the text chunking function
# this splits large documents into smaller pieces
from utils.text_chunker import chunk_text

# import vector database functions
# create_vector_store stores embeddings in chromadb
# search_vector_store finds relevant chunks for a question
from utils.vector_store import create_vector_store, search_vector_store

# import rag answer function
# this sends the question and retrieved chunks to the llm
from agents.rag_agent import answer_question

# import stock data function
# this gets financial data from yahoo finance
from agents.stock_agent import get_stock_data


# configure the streamlit page
st.set_page_config(
    page_title="FinSight AI",
    page_icon="📊",
    layout="wide"
)


# create sidebar
st.sidebar.title("FinSight AI")

st.sidebar.write(
    "Multi-agent financial research platform using RAG, LLMs, vector search, and market data."
)

st.sidebar.markdown("### Features")
st.sidebar.write("- Annual report Q&A")
st.sidebar.write("- Source-grounded answers")
st.sidebar.write("- Stock comparison")
st.sidebar.write("- Financial research workflow")


# main page title
st.title("📊 FinSight AI")

# better subtitle
st.subheader("Multi-Agent Financial Research Platform")

st.write(
    "Upload an annual report, ask questions using RAG, and compare public companies using market data."
)


# create tabs for cleaner layout
rag_tab, stock_tab = st.tabs(
    ["📄 Annual Report Q&A", "📈 Stock Comparison"]
)


# annual report rag tab
with rag_tab:

    # section heading
    st.header("Annual Report Question Answering")

    # explain what this section does
    st.write(
        "Upload a company annual report PDF and ask questions grounded in the document."
    )

    # create a file upload widget
    uploaded_file = st.file_uploader(
        "Upload Annual Report PDF",
        type=["pdf"]
    )

    # check whether a pdf has been uploaded
    if uploaded_file:

        # show spinner while extracting text
        with st.spinner("extracting text from pdf..."):

            # extract all text from the pdf
            text = extract_text_from_pdf(uploaded_file)

        # display success message
        st.success("PDF uploaded and text extracted successfully")

        # split the report into smaller chunks
        with st.spinner("splitting report into chunks..."):

            # chunk the extracted report text
            chunks = chunk_text(text)

        # show number of chunks created
        st.info(f"Created {len(chunks)} document chunks")

        # create the vector database
        with st.spinner("creating vector database..."):

            # convert chunks into embeddings and store them in chromadb
            collection = create_vector_store(chunks)

        # confirm vector database creation
        st.success("Vector database created successfully")

        # expandable section for extracted text preview
        with st.expander("View extracted text preview"):

            # show only first 3000 characters
            st.text_area(
                "Preview",
                text[:3000],
                height=300
            )

        # expandable section for first chunk
        with st.expander("View first document chunk"):

            # show first chunk for debugging and transparency
            st.write(chunks[0])

        # create question input
        question = st.text_input(
            "Ask a question about the annual report"
        )

        # create preset question buttons
        # these make the app easier to demo
        st.write("Quick Analysis")

        col_a, col_b, col_c, col_d = st.columns(4)

        with col_a:
            summary_clicked = st.button("Summarise Report")

        with col_b:
            risks_clicked = st.button("Find Key Risks")

        with col_c:
            revenue_clicked = st.button("Revenue Drivers")

        with col_d:
            outlook_clicked = st.button("Future Outlook")


        # set the question based on which button is clicked
        if summary_clicked:
            question = "summarise this report in 5 bullet points"

        if risks_clicked:
            question = "what are the key risks mentioned in this report?"

        if revenue_clicked:
            question = "what are the main revenue drivers mentioned in this report?"

        if outlook_clicked:
            question = "what does the report say about future outlook?"

        # check whether user entered a question
        if question:

            # retrieve relevant chunks
            with st.spinner("searching relevant report sections..."):

                # search chromadb for chunks similar to the question
                relevant_chunks = search_vector_store(
                    collection,
                    question
                )

            # generate answer
            with st.spinner("generating ai answer..."):

                # send question and chunks to groq llm
                answer = answer_question(
                    question,
                    relevant_chunks
                )

            # display generated answer first
            st.subheader("AI Answer")

            # show answer
            st.write(answer)
            
            # allow user to download the generated answer
            st.download_button(
                label="Download Answer",
                data=answer,
                file_name="finsight_ai_answer.txt",
                mime="text/plain"
            )

            # show source chunks after answer
            st.subheader("Source Chunks Used")

            # loop through chunks
            for chunk in relevant_chunks:

                # display source chunk
                st.write(chunk)

                # divider for readability
                st.divider()

    # message shown before a pdf is uploaded
    else:
        st.info("Upload an annual report PDF to start asking questions.")


# stock comparison tab
with stock_tab:

    # section heading
    st.header("Stock Comparison")

    # explain what this section does
    st.write(
        "Compare two public companies using live market data from Yahoo Finance."
    )

    # create two columns for ticker inputs
    input_col1, input_col2 = st.columns(2)

    # first ticker input
    with input_col1:
        ticker1 = st.text_input(
            "First Company Ticker",
            value="AAPL"
        )

    # second ticker input
    with input_col2:
        ticker2 = st.text_input(
            "Second Company Ticker",
            value="MSFT"
        )

    # button to start comparison
    if st.button("Compare Companies"):

        # show spinner while fetching stock data
        with st.spinner("fetching stock data..."):

            # get stock data for first company
            company1 = get_stock_data(ticker1)

            # get stock data for second company
            company2 = get_stock_data(ticker2)

        # create two columns for comparison results
        col1, col2 = st.columns(2)

        # display first company
        with col1:

            # company name heading
            st.subheader(company1["company"])

            # display current stock price
            st.metric("Stock Price", company1["price"])

            # display market cap
            st.write("Market Cap:", company1["market_cap"])

            # display p/e ratio
            st.write("P/E Ratio:", company1["pe_ratio"])

            # display sector
            st.write("Sector:", company1["sector"])

        # display second company
        with col2:

            # company name heading
            st.subheader(company2["company"])

            # display current stock price
            st.metric("Stock Price", company2["price"])

            # display market cap
            st.write("Market Cap:", company2["market_cap"])

            # display p/e ratio
            st.write("P/E Ratio:", company2["pe_ratio"])

            # display sector
            st.write("Sector:", company2["sector"])