from google import genai
from .config import GEMINI_API_KEY

# Initialize Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)


def get_embedding(text: str):
    """
    Generate embedding for a text using Gemini.
    """

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values