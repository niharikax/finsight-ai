# Import PdfReader from the pypdf library 
from pypdf import PdfReader

def extract_text_from_pdf(uploaded_file): # this functions allows you to extract all text from a PDF file

    
    reader = PdfReader(uploaded_file) # creates a PdfReader object to access the PDF's contents
    text = ""  # creates an empty string so that it will store text from all pages

    for page in reader.pages:

        text += page.extract_text()  # extracting the text from the current page and add it to the text variable 

    return text # returning the complete extracted text