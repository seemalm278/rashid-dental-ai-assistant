from .rag import RAGRetriever

rag = RAGRetriever()

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    response = rag.generate_answer(question)

    print("\nAssistant:\n")

    print(response["answer"])

    print("\nSources:")

    for source in response["sources"]:
        print("-", source)