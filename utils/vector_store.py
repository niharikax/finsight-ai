# Import ChromaDB (vector database)
# Used to store and search embeddings efficiently
import chromadb

# Import embedding model
# Converts text into numerical vectors that capture meaning
from sentence_transformers import SentenceTransformer


# Load a pre-trained embedding model
# all-MiniLM-L6-v2 is lightweight, fast, and commonly used for RAG
model = SentenceTransformer("all-MiniLM-L6-v2")


# Create a vector database from text chunks
def create_vector_store(chunks):

    # c
    client = chromadb.Client()

    # Create a collection (like a table in a database)
    # If it already exists, use the existing one
    collection = client.get_or_create_collection(
        name="annual_report"
    )

    # Loop through every chunk
    for i, chunk in enumerate(chunks):

        # Convert chunk into an embedding vector
        # Example output:
        # [0.12, -0.44, 0.91, ...]
        embedding = model.encode(chunk).tolist()

        # Store chunk and its embedding in ChromaDB
        collection.add(
            ids=[str(i)],            # Unique ID
            embeddings=[embedding], # Numerical representation
            documents=[chunk]       # Original text
        )

    # Return the completed collection
    return collection

# search the vector database for chunks most similar to the question
def search_vector_store(collection, question, n_results=3):

    # convert the user's question into an embedding
    question_embedding = model.encode(question).tolist()

    # search chromadb for similar embeddings
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )

    # return the retrieved document chunks
    return results["documents"][0]