from fastapi import FastAPI
from app.file_router import router as file_router
from app.rag_pipeline import ask_question

app = FastAPI()

app.include_router(file_router)

@app.get("/ask")
def ask(question: str):
    answer = ask_question(question)
    return {"answer": answer}