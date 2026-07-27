from .embeddings import get_embedding

text = "Teeth whitening services"

embedding = get_embedding(text)

print("Embedding Length:", len(embedding))
print(embedding[:10])