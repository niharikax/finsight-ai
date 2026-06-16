# import os to access environment variables
import os

# load variables from the .env file
from dotenv import load_dotenv

# import groq client
from groq import Groq


# load environment variables
load_dotenv()


# create groq client using api key
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# function to evaluate an ai-generated answer
def evaluate_answer(question, answer, relevant_chunks):

    # combine retrieved chunks into one context string
    context = "\n\n".join(relevant_chunks)

    # create evaluation prompt
    prompt = f"""
you are an evaluation agent for a financial rag system.

evaluate the answer based on:

1. faithfulness - is the answer supported by the source context?
2. relevance - does the answer address the question?
3. completeness - does the answer cover the important points?
4. clarity - is the answer easy to understand?

question:
{question}

source context:
{context}

answer:
{answer}

return your evaluation in this format:

faithfulness: /10
relevance: /10
completeness: /10
clarity: /10

overall score: /10

feedback:
"""

    # send evaluation prompt to groq
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    # return evaluation text
    return response.choices[0].message.content