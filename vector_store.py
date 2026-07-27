import os
import pickle
import faiss
import numpy as np

from .loader import load_markdown_chunks
from .embeddings import get_embedding

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "faiss.index")
METADATA_PATH = os.path.join(BASE_DIR, "metadata.pkl")


def build_vector_store():
    """
    Build FAISS index from Markdown chunks.
    """

    print("Loading Markdown files...")
    chunks = load_markdown_chunks()

    print(f"Loaded {len(chunks)} chunks")

    embeddings = []

    for i, chunk in enumerate(chunks, start=1):

        print(f"Embedding chunk {i}/{len(chunks)}...")

        vector = get_embedding(chunk["content"])

        embeddings.append(vector)

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)

    with open(METADATA_PATH, "wb") as f:
        pickle.dump(chunks, f)

    print("\n✅ Vector database created successfully!")
    print(f"Vectors stored: {index.ntotal}")


if __name__ == "__main__":
    build_vector_store()