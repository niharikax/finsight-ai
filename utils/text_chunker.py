# Function to split a large text into smaller chunks
def chunk_text(text, chunk_size=1000):

    # Empty list to store all chunks
    chunks = []

    # Loop through the text in steps of chunk_size
    for i in range(0, len(text), chunk_size):

        # Extract a portion of the text and add it to the chunks list
        # text[start:end]
        chunks.append(text[i:i + chunk_size])

    # Return the list of text chunks
    return chunks