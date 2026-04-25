# AI Learning Notebooks

A collection of Jupyter notebooks covering key AI/ML topics: GANs, multimodal AI, LangChain, LangGraph, RAG, CrewAI, and more.

## Topics

| Folder | Topic | Description |
|--------|-------|-------------|
| `gan-mnist` | GANs | Generative Adversarial Network trained on MNIST dataset |
| `image-captioning-gemini` | Multimodal | Image captioning model using Google Gemini Pro |
| `multimodal` | Multimodal AI | Working with text, images, audio, and chat conversations using Gemini |
| `langchain` | LangChain | LLM apps, RAG, chatbots, SQL agents, semantic search |
| `rag-with-pdfs` | RAG | Retrieval-Augmented Generation over PDF documents, building RAG pipelines |
| `sql-rag` | SQL RAG | Natural language to SQL query generation |
| `langgraph-and-agents` | LangGraph | Agent workflows, parallelization, routing, web scraping |
| `gemini-basics` | Gemini | Getting started with Google Gemini — first script, image-to-text |
| `prompt-engineering` | Prompt Engineering | Prompt techniques with Together AI and Gemini, user-input workflows |
| `huggingface` | HuggingFace | GPT-2 text generation, image scaling (Swin2SR), text-to-image (Diffusion) |
| `crewai` | CrewAI | Multi-agent orchestration and collaboration |

## Tech Stack
- Google Gemini API
- LangChain / LangGraph
- CrewAI
- HuggingFace Transformers
- ChromaDB
- PyTorch (GANs)
- Diffusers (text-to-image)
- Together AI

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
