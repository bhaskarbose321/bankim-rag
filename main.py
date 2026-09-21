from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(
    title="Bankim RAG API",
    description="A simple RAG API using TF-IDF retrieval",
    version="1.0.0",
)


# Load document

with open("bankim.txt", "r", encoding="utf-8") as file:
    data = file.read()

chunks = data.split("\n\n")

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(chunks)


# Request model


class Question(BaseModel):
    question: str


# Home endpoint


@app.get("/")
def home():
    return {"message": "Bankim RAG API is running"}


# RAG endpoint


@app.post("/ask")
def ask_question(request: Question):

    question = request.question

    # Convert question to vector
    question_vector = vectorizer.transform([question])

    # Compare with document chunks
    similarity = cosine_similarity(question_vector, vectors)[0]

    # Get best chunk
    best_index = similarity.argmax()

    best_chunk = chunks[best_index]

    return {
        "question": question,
        "answer": best_chunk,
    }
