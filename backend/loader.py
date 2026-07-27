import os
from langchain_text_splitters import MarkdownHeaderTextSplitter

# Path to the knowledge base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWLEDGE_BASE = os.path.join(BASE_DIR, "knowledge_base")


def load_markdown_chunks():
    """
    Load all markdown files and split them into chunks
    using markdown headings.
    """

    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "Heading 1"),
            ("##", "Heading 2"),
        ]
    )

    chunks = []

    for filename in os.listdir(KNOWLEDGE_BASE):

        if filename.endswith(".md"):

            filepath = os.path.join(KNOWLEDGE_BASE, filename)

            with open(filepath, "r", encoding="utf-8") as f:

                text = f.read()

            docs = splitter.split_text(text)

            for doc in docs:

                chunks.append(
                    {
                        "source": filename,
                        "content": doc.page_content,
                        "metadata": doc.metadata,
                    }
                )

    return chunks


if __name__ == "__main__":

    docs = load_markdown_chunks()

    print("=" * 60)

    print(f"Loaded {len(docs)} chunks\n")

    for i, chunk in enumerate(docs, start=1):

        print(f"Chunk {i}")

        print("Source:", chunk["source"])

        print("Metadata:", chunk["metadata"])

        print(chunk["content"])

        print("-" * 60)