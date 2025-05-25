# 🎯 Semantic Search Q&A from Transcript (CLI-Based NLP Project)

> 🚀 Ask any question and get meaningful answers extracted from a timestamped transcript using modern NLP techniques like TF-IDF, OpenAI Embeddings, and Hugging Face transformers.

---

## 📌 Project Description

This project implements a **semantic search system** that processes a **timestamped transcript** and allows users to query it using natural language questions. The system returns the **most relevant paragraph** with its associated **timestamp** not just keyword matches.

### 💡 Use Cases:

- Extract key information from transcripts, podcasts, or interviews
- Build educational assistants for lecture videos
- Enable deep Q&A over structured documents

---

```bash
git clone https://github.com/rgmhacks/semantic-search-transcript
cd semantic-search-transcript
pip install -r requirements.txt
set OPENAI_API_KEY=your-key-here  # Required for using OPENAI model i.e. llm1
```

### 🚀 Usage

```bash
python transcript.py transcript.txt tfidf   # TF-IDF mode
python transcript.py transcript.txt llm1    # OpenAI Embedding mode
python transcript.py transcript.txt llm2    # Hugging Face model mode
```

### 📚 Project Structure:

semantic-search-transcript/
├── transcript.py # CLI entry point
├── transcript.txt # Timestamped transcript
├── tfidf_search.py # TF-IDF implementation
├── openai_search.py # OpenAI embedding-based search
├── hf_search.py # Hugging Face model (all-MiniLM-L6-v2)
├── utils.py # Chunking and preprocessing
├── output.txt # Output
├── requirements.txt # Python dependencies
└── README.md # Project overview and instructions
