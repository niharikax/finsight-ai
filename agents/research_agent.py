# import os to access environment variables
import os

# load variables from the .env file
from dotenv import load_dotenv

# import groq client
from groq import Groq


# load environment variables from .env
load_dotenv()


# create groq client using api key
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# function for broader company research questions
def research_company(question):

    # create research prompt
    prompt = f"""
you are a financial research assistant.

answer the user's company research question in a clear, structured way.

focus on:
- business model
- growth drivers
- risks
- competitive position
- future outlook

if the question asks for current or recent information, mention that live web search is not yet connected.

question:
{question}

return the answer with headings and bullet points.
"""

    # send prompt to groq model
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    # return generated research response
    return response.choices[0].message.content