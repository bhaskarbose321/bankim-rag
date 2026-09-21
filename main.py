from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI(
    title="Bankim RAG API",
    description="A simple RAG API using Semantic Vector retrieval",
    version="2.0.0",
)

# 1. Load the free, local embedding model
# (It will download automatically the very first time you run the server)
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Load and split the document
with open("bankim.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Filter out empty chunks to prevent index errors
chunks = [chunk.strip() for chunk in data.split("\n\n") if chunk.strip()]

# 3. Generate semantic vectors for all document chunks
# (This replaces vectorizer.fit_transform)
vectors = model.encode(chunks, convert_to_numpy=True)


# Request model
class Question(BaseModel):
    question: str


# Home endpoint
@app.get("/")
def home():
    return {"message": "Bankim RAG API is running with Semantic Search"}


# RAG endpoint
@app.post("/ask")
def ask_question(request: Question):
    question = request.question

    # 4. Convert user question to a semantic vector
    question_vector = model.encode(question, convert_to_numpy=True)

    # 5. Calculate Cosine Similarity manually via dot product
    # (SentenceTransformer vectors are pre-normalized, so dot product equals cosine similarity)
    similarity = np.dot(vectors, question_vector)

    # 6. Get the index of the best matching chunk
    best_index = similarity.argmax()
    best_chunk = chunks[best_index]

    return {
        "question": question,
        "answer": best_chunk,
        "confidence_score": float(
            similarity[best_index]
        ),  # Added to show how strong the match is
    }
