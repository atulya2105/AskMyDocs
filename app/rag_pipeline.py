from app.vector_store import query_chunks
from app.embeddings import get_embedding
from app.llm import generate_answer
from app.tools.web_search import search_web
from app.vector_store import search_similar_chunks

chat_memory = []
def get_context(question):
    chunks = query_chunks(question, get_embedding)
    print("Context:", chunks)
    return chunks

def ask_question(question):
    context = get_context(question)

    if not context:
        return "No relevant data found. Please upload a PDF."

    answer = generate_answer(question, context)
    return answer

# def ask_question(question):

    context = search_similar_chunks(question)
    

    # 🔥 CONDITION (Agent decision)
    if not context or len(context) < 2:
        print("⚠️ No strong context found → using web search")

        web_results = search_web(question)

        return generate_answer(
            question,
            context=web_results,
            source="web"
        )

    # ✅ Normal RAG flow
    return generate_answer(question, context, source="pdf")    

def ask_question(question):
    global chat_memory

    # 🔥 Step 1: Get context from PDF
    context = search_similar_chunks(question)

    # 🔥 Step 2: Combine previous conversation
    history = "\n".join(chat_memory)

    # 🔥 Step 3: Final context
    full_context = history + "\n" + " ".join(context)

    # 🔥 Step 4: Generate answer
    answer = generate_answer(question, full_context)

    # 🔥 Step 5: Save memory
    chat_memory.append(f"User: {question}")
    chat_memory.append(f"AI: {answer}")

    return answer