import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_answer(
    question: str,
    context: str
) -> str:

    prompt = f"""
You are a helpful assistant answering questions about a document.

Answer the question using ONLY the information provided in the context.

If the answer cannot be found in the context, say:

"I couldn't find the answer in the provided document."

CONTEXT:
{context}

QUESTION:
{question}
"""

    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents = prompt
    )

    return response.text