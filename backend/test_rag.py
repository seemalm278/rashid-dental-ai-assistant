from .rag import RAGRetriever

rag = RAGRetriever()

question = "What are your opening hours?"

results = rag.search(question)

print("\nQUESTION:")
print(question)

print("\nRESULTS\n")

for i, item in enumerate(results, start=1):

    print("=" * 60)

    print(f"Result {i}")

    print("Source:", item["source"])

    print("Metadata:", item["metadata"])

    print(item["content"])