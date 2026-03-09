from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# File paths for documents, queries, and results
DOCUMENT_FILE = "documents.txt"
QUERY_FILE = "queries.txt"
RESULT_FILE = "results.txt"


def load_documents():
    # Read documents from file and remove empty lines
    with open(DOCUMENT_FILE, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def save_query(query):
    # Append the user's query to queries.txt
    with open(QUERY_FILE, "a", encoding="utf-8") as file:
        file.write(query + "\n")


def save_results(output):
    # Save retrieved results to results.txt
    with open(RESULT_FILE, "a", encoding="utf-8") as file:
        file.write(output)


def main():
    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Load documents and convert them to embeddings
    documents = load_documents()
    document_embeddings = model.encode(documents)

    print("\nSemantic Search Ready")
    print("Type 'exit' to quit\n")

    while True:
        # Get query from terminal
        query = input("Enter Query: ")

        if query.lower() == "exit":
            break

        # Save query to file
        save_query(query)

        # Convert query to embedding
        query_embedding = model.encode([query])

        # Compute cosine similarity between query and documents
        similarities = cosine_similarity(query_embedding, document_embeddings)[0]

        # Get indices of top 3 most similar documents
        top_indices = np.argsort(similarities)[::-1][:3]

        print("\nTop 3 Results:\n")

        output = f"Query: {query}\nTop 3 Results:\n"

        for rank, idx in enumerate(top_indices, start=1):
            document = documents[idx]
            score = similarities[idx]

            # Display result with similarity score
            print(f"{rank}. {document} ({score:.2f})")

            output += f"{rank}. {document} ({score:.2f})\n"

        output += "---------------------------------\n"

        # Save results to file
        save_results(output)

        print("\n---------------------------------\n")


if __name__ == "__main__":
    # Entry point of the program
    main()