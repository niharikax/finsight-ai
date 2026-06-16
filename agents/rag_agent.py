# import os so we can access environment variables
import os

# load variables from the .env file
from dotenv import load_dotenv

# import the groq client
from groq import Groq


# load all variables from .env into the application
load_dotenv()


# create a groq client using the api key stored in .env
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# function that generates an answer using retrieved chunks
def answer_question(question, relevant_chunks):

    # combine all retrieved chunks into one large context string
    context = "\n\n".join(relevant_chunks)

    # create the prompt sent to the llm
    # we tell it to answer only from the retrieved source text
    prompt = f"""
you are a financial research assistant.

answer the user's question using only the source context below.

if the answer is not available in the source context, say:
"i could not find this information in the uploaded report."

source context:
{context}

user question:
{question}
"""

    # send the prompt to the groq model
    response = client.chat.completions.create(

        # model being used for generation
        model="llama-3.1-8b-instant",

        # user message containing the prompt
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        # lower temperature = more factual and less creative
        temperature=0.2
    )

    # return only the generated answer text
    return response.choices[0].message.content