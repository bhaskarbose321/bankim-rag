# Bankim RAG API 🤖

A lightweight, high-performance Retrieval-Augmented Generation (RAG) API built with **FastAPI** and **Sentence-Transformers**. It uses local, open-source dense vector embeddings (`all-MiniLM-L6-v2`) to perform accurate semantic searches over unstructured markdown text profiles.

Unlike traditional keyword-matching systems (like TF-IDF), this API understands user intent, synonyms, and context.

## 🚀 Features
* **Semantic Search:** Evaluates the contextual meaning of sentences rather than exact word matching.
* **Header-Based Chunking:** Intelligently groups markdown subsections to preserve full text context.
* **FastAPI Backend:** Built-in high-performance asynchronous API endpoints with automatic documentation.
* **100% Free & Local:** Runs completely on your local CPU without requiring paid API keys or cloud services.

## 🛠️ Tech Stack
* **Python 3.8+**
* **FastAPI** (API framework)
* **Sentence-Transformers** (Local embedding generation)
* **NumPy** (Vector similarity operations)

## 📦 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com
   cd bankim-rag-api
   ```

2. **Install Dependencies**
   Make sure you have the required Python modules installed:
   ```bash
   pip install fastapi uvicorn sentence-transformers numpy pydantic
   ```

3. **Prepare the Data**
   Ensure your text profile data is saved as `bankim.txt` in the root directory of the project.

## 🏃 How to Run the Server

Start the local server using the Python module execution flag to bypass system environment path restrictions:

```bash
python -m uvicorn main:app --reload
```

*Note: The server will automatically download the lightweight embedding model (`all-MiniLM-L6-v2`, ~90MB) on its very first execution.*

Once started, the API will be live at `http://127.0.0.1:8000`.

## 📡 API Endpoints

### 1. Home Check
* **URL:** `/`
* **Method:** `GET`
* **Response:**
  ```json
  { "message": "Bankim RAG API is running with Semantic Search" }
  ```

### 2. Ask RAG Query
* **URL:** `/ask`
* **Method:** `POST`
* **Payload:**
  ```json
  { "question": "when bankimchandra was born?" }
  ```
* **Response:**
  ```json
  {
    "question": "when bankimchandra was born?",
    "answer": "## Personal Overview\n- **Full Name**: Bankim Chandra Chattopadhyay CIE...\n- **Birth**: 26 June 1838...",
    "confidence_score": 0.7241
  }
  ```

## 🧪 Interactive Testing
You can interactively test all requests directly from your browser via the built-in Swagger UI documentation. Navigate to:
👉 **[http://127.0.0](http://127.0.0)**
