from app.file_router import process_file
from app.chunker import chunk_text
from app.embeddings import get_embedding
from app.vector_store import store_chunks
from app.rag_pipeline import get_context

# Step 1: load file
text = process_file("sample.pdf")

# Step 2: chunk
chunks = chunk_text(text)

# Step 3: store
store_chunks(chunks, get_embedding)

# Step 4: query
query = "What is AI?"
context = get_context(query)

print("Context:\n", context)

text = process_file("sample.pdf")
print("Extracted text:", text[:500])