# Day 4 - Semantic Search with Sentence Embeddings


This project demonstrates a **simple semantic search system** using sentence embeddings and cosine similarity.  
Instead of keyword matching, the system retrieves documents based on **semantic meaning**.

## Overview

The program converts documents and user queries into vector embeddings using a transformer model and finds the most similar documents using cosine similarity.

The system supports:
- Loading documents from a text file
- Accepting queries from the terminal
- Retrieving the **Top 3 most relevant documents**
- Displaying **similarity scores**
- Saving queries and results for record

## Technologies Used

- Python
- Sentence Transformers
- NumPy
- Scikit-learn

## Concepts Learned

- **Embeddings** – Convert text into numerical semantic vectors.
- **Semantic Search** – Retrieve results based on meaning.
- **Transformers** – Deep learning models for language understanding.
- **Cosine Similarity** – Measures similarity between vector representations.
- **Vector Representation** – Encodes text meaning in high-dimensional space.
- **Information Retrieval** – Finding relevant documents for queries.
- **Terminal Input Handling** – Accepting dynamic user queries.
- **File Handling in Python** – Reading and writing text files.

## Project Structure

```
simple_retrieval_day4_exercise/
│
├── documents.txt        # Input documents
├── queries.txt          # Stores user queries
├── results.txt          # Stores retrieved results
└── semantic_search.py   # Main semantic search program
```

## How It Works

1. Documents are loaded from `documents.txt`.
2. The model converts each document into embeddings.
3. User enters a query in the terminal.
4. The query is converted into an embedding.
5. Cosine similarity compares the query with document embeddings.
6. The system retrieves the **Top 3 most relevant documents**.

Example output:

```
Enter Query: What are embeddings?

Top 3 Results:
1. Embeddings convert text into vectors representing meaning. (0.89)
2. Transformers use self-attention for sequence modeling. (0.32)
3. Diffusion models generate images by gradually removing noise. (0.11)
```

## Installation

Create a virtual environment and install dependencies.

```bash
python -m venv ai_env
ai_env\Scripts\activate
pip install sentence-transformers scikit-learn numpy
```

## Run the Program

```bash
python semantic_search.py
```

Then enter queries directly from the terminal.

Example:

```
Enter Query: What are transformers?
```

## Files Generated

- `queries.txt` → stores all user queries
- `results.txt` → stores retrieved results with similarity scores

## Learning Outcome

This project demonstrates how **modern AI retrieval systems work internally** using embeddings and vector similarity.

It is a simplified introduction to **semantic search and retrieval systems used in RAG pipelines**.
