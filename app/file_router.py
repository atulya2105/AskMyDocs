from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.readers.pdf_reader import read_pdf
from app.chunker import chunk_text
from app.vector_store import store_chunks
from app.embeddings import get_embedding

router = APIRouter()

UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = read_pdf(file_path)
    print("Extracted text:", text[:200])

    chunks = chunk_text(text)

    store_chunks(chunks, get_embedding)

    return {"message": "File processed successfully"}