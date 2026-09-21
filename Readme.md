# Bankim Chandra Chattopadhyay RAG System

A Retrieval-Augmented Generation (RAG) system for searching biographical information about Bankim Chandra Chattopadhyay using semantic search.

## Features

- Semantic search using sentence transformers
- FAISS vector indexing for fast similarity search
- Web interface for easy querying
- Deployed on Render

## Tech Stack

- **Backend**: Flask
- **Embeddings**: Sentence-Transformers (all-MiniLM-L6-v2)
- **Vector Search**: FAISS
- **Frontend**: HTML/CSS/JavaScript

## Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Open your browser and navigate to `http://localhost:5000`

## Usage

- Enter your question about Bankim Chandra Chattopadhyay in the search box
- Click "Search" or press Enter
- View the most relevant information chunks from the knowledge base

## Deployment

This application is configured for deployment on Render using:
- `render.yaml` - Render configuration
- `Procfile` - Process configuration
- `requirements.txt` - Python dependencies

## Data Source

The system uses biographical information about Bankim Chandra Chattopadhyay stored in `bankim_chandra_chattopadhyay_rag.txt`.
