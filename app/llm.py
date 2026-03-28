from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(query, context, source=None):

    context_text = "\n".join(context)

    prompt = f"""
                    You are an intelligent AI assistant working on a document-based system.

                    STRICT RULES:

                    1. Primary Source:
                    - Always try to answer using ONLY the provided context.

                    2. Smart Extension:
                    - If the answer is not clearly present in the context,
                    you may use general knowledge ONLY IF the question is relevant to the document.

                    3. Allowed Cases for External Knowledge:
                    - Summarizing the document
                    - Generating questions/answers from the document
                    - Explaining terms mentioned in the document (e.g., AI, Amazon Connect, etc.)
                    - Expanding on document-related topics

                    4. Disallowed:
                    - Do NOT answer unrelated questions
                    - Do NOT hallucinate random information

                    5. If question is irrelevant or doesn't make sense:
                    → Reply exactly:
                    "Not able to recall it"

                    6. Style:
                    - Keep answers concise and clear
                    - Use simple language
                    - Prefer bullet points when helpful

                    ---------------------

                    Context:
                    {context_text}

                    Question:
                    {query}

                    Source :
                    {source}

                    Answer:
                    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content