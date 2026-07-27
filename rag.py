import os
import pickle
import faiss
import numpy as np

from google import genai

from .embeddings import get_embedding
from .config import GEMINI_API_KEY

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "faiss.index")
METADATA_PATH = os.path.join(BASE_DIR, "metadata.pkl")

# Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)


class RAGRetriever:

    def __init__(self):
        self.index = faiss.read_index(INDEX_PATH)

        with open(METADATA_PATH, "rb") as f:
            self.chunks = pickle.load(f)

    def search(self, question, top_k=3):
        """
        Search the FAISS index and return the most relevant chunks.
        """

        question_embedding = np.array(
            [get_embedding(question)],
            dtype="float32"
        )

        distances, indices = self.index.search(question_embedding, top_k)

        results = []

        for idx in indices[0]:
            if idx < len(self.chunks):
                results.append(self.chunks[idx])

        return results

    def generate_answer(self, question, history=None):
        """
        Generate an answer using retrieved context and conversation history.
        """

        # Retrieve relevant chunks
        results = self.search(question)

        context = ""
        sources = []

        for item in results:
            context += item["content"] + "\n\n"

            if item["source"] not in sources:
                sources.append(item["source"])

        # Build conversation history
        history_text = ""

        if history:
            for item in history:
                history_text += f"{item['role']}: {item['message']}\n"

        # Create prompt
        prompt = f"""
You are the AI Assistant for Rashid Dental Clinic.

Conversation History:
{history_text}

Context:
{context}

User Question:
{question}

IMPORTANT RULES:
- Answer ONLY using the provided context.
- Never invent clinic information.
- Never diagnose diseases.
- Never recommend medication.
- If information is unavailable, clearly say so.
- Keep answers short and professional.
- If the answer is not in the context, say that you don't have verified information.
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return {
            "answer": response.text.strip(),
            "sources": sources
        }