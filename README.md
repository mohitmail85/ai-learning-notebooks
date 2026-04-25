# AI Learning Notebooks

A collection of Jupyter notebooks covering key AI/ML topics: GANs, multimodal AI, LangChain, LangGraph, RAG, CrewAI, and more.

## Topics

| Folder | Topic | Description |
|--------|-------|-------------|
| `gan-mnist` | GANs | Generative Adversarial Network trained on MNIST dataset |
| `image-captioning-gemini` | Multimodal | Image captioning model using Google Gemini Pro |
| `multimodal` | Multimodal AI | Working with text, images, and audio using Gemini |
| `langchain` | LangChain | LLM apps, RAG, chatbots, SQL agents, semantic search |
| `rag-with-pdfs` | RAG | Retrieval-Augmented Generation over PDF documents |
| `sql-rag` | SQL RAG | Natural language to SQL query generation |
| `langgraph-and-agents` | LangGraph | Agent workflows, parallelization, routing, web scraping |
| `crewai` | CrewAI | Multi-agent orchestration and collaboration |

## Tech Stack
- Google Gemini API
- LangChain / LangGraph
- CrewAI
- HuggingFace Transformers
- ChromaDB
- PyTorch (GANs)

## Setup

```bash
git clone https://github.com/mohitmail85/ai-learning-notebooks.git
cd ai-learning-notebooks
```

Each notebook may have different dependencies. Install as needed:
```bash
pip install google-generativeai langchain langgraph crewai chromadb
```

Set your API keys:
```bash
export GOOGLE_API_KEY=your_key_here
export OPENAI_API_KEY=your_key_here
export TOGETHERAI_API_KEY=your_key_here
```
