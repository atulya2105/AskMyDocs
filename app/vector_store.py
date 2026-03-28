import chromadb
from app.embeddings import get_embedding

client = chromadb.Client()

collection = client.get_or_create_collection(name="docs")

def store_chunks(chunks, embed_fn):
    print("Storing chunks:", len(chunks))

    if len(chunks) == 0:
        return

    embeddings = embed_fn(chunks)

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[str(i) for i in range(len(chunks))]
    )

def query_chunks(query, embed_fn):
    query_embedding = embed_fn([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    return results["documents"][0] if results["documents"] else []

def search_similar_chunks(query, top_k=3):
    # Convert question to embedding
    query_embedding = get_embedding(query)

    # Search in vector DB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    # Extract text chunks
    chunks = results["documents"][0]

    return chunks