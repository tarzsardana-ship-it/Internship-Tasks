# 🤖 AI Knowledge & Research Chatbot

## 📌 Project Overview

This project is an AI-powered Knowledge & Research Chatbot developed using **Streamlit, LangChain, Google Gemini, FAISS, HuggingFace Embeddings, and multiple datasets**.

The chatbot can answer questions from:

- Customer Service Dataset
- Medical Dataset (MedQuAD)
- Computer Science Research Papers (arXiv)

It also supports **research paper search, paper summarization, concept explanation, research statistics visualization, and image analysis** using Google Gemini.

If an answer is unavailable in the knowledge base, the chatbot automatically performs a web search, generates a response using Google Gemini, and updates its knowledge base for future queries.

---

# 🌐 Live Demo

### Streamlit App

https://internship-task-4.streamlit.app/

### GitHub Repository

https://github.com/tarzsardana-ship-it/Internship-Tasks/tree/main/Task4

---

# 📌 Problem Statement

Build an AI-powered Knowledge & Research Chatbot capable of answering customer support, medical, and research-related questions using multiple knowledge sources.

The chatbot should:

- Answer questions from customer service and medical datasets.
- Search and retrieve relevant Computer Science research papers.
- Summarize research papers.
- Explain technical concepts in simple language.
- Analyze uploaded images using Google Gemini Vision.
- Search the web when information is unavailable.
- Dynamically update its knowledge base for future queries.

---

# 🚀 Features

### 💬 General AI Chat

- Customer Service Question Answering
- Medical Question Answering
- Computer Science Research Question Answering

### 📚 Research Paper Features

- Search Research Papers
- Paper Summarization
- Concept Explanation
- Research Statistics Visualization

### 🧠 AI Features

- Google Gemini Integration
- FAISS Vector Database
- HuggingFace Embeddings
- Dynamic Knowledge Base Updates
- Automatic Web Search
- Image Analysis using Gemini Vision

### 📊 Data Visualization

- Top Research Categories
- Papers Published by Year

### 🌐 User Interface

- Interactive Streamlit Web Application
- Multiple Chat Modes
- Fast Semantic Search

---

# 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API
- HuggingFace Embeddings
- FAISS
- DuckDuckGo Search (DDGS)
- Pandas
- Matplotlib
- Pillow

---

# 📂 Project Structure

```
Task4/

│── main.py
│── langchain_helper.py
│── dataset.csv
│── medical_dataset.csv
│── arxiv_dataset.csv
│── knowledge_updates.csv
│── faiss_index/
│── requirements.txt
│── .env.example
│── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/tarzsardana-ship-it/Internship-Tasks.git
```

## 2. Navigate to the Project Folder

```bash
cd Internship-Tasks/Task4
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Create a .env File

Add your Google Gemini API key:

```text
GOOGLE_API_KEY=your_api_key_here
```

## 5. Run the Application

```bash
streamlit run main.py
```

---

# 📸 How It Works

1. Create the FAISS knowledge base using:
   - Customer Service Dataset
   - Medical Dataset (MedQuAD)
   - arXiv Research Paper Dataset
   - Knowledge Updates

2. Choose a chat mode from the Streamlit interface.

3. Ask a question, search for a research paper, summarize a paper, explain a concept, or upload an image.

4. If the answer exists in the knowledge base, it is retrieved instantly.

5. If the answer is unavailable, the chatbot searches the web using DuckDuckGo.

6. Google Gemini generates a response from the retrieved web information.

7. The newly generated answer is automatically stored in the knowledge base for future queries.

---

# 💡 Chat Modes

### 🧠 General Chat

Answers questions using:

- Customer Service Dataset
- Medical Dataset
- Research Paper Dataset
- Dynamic Knowledge Base
- Web Search (if required)

### 🔍 Research Paper Search

Searches relevant Computer Science research papers from the arXiv dataset.

### 📄 Paper Summarization

Generates an easy-to-understand summary of research papers using Google Gemini.

### 💡 Concept Explanation

Explains technical concepts in beginner-friendly language using research paper abstracts.

### 📊 Research Statistics

Displays:

- Top Research Categories
- Number of Papers Published by Year

---

# 📷 Image Analysis

Upload an image and ask questions related to it.

Google Gemini Vision analyzes the uploaded image and generates an intelligent response.

---

# 📊 Results

- Successfully built an AI-powered Knowledge & Research Chatbot.
- Retrieves information from Customer Service, Medical, and Research Paper datasets.
- Supports semantic search using FAISS.
- Searches Computer Science research papers.
- Generates paper summaries.
- Explains technical concepts in simple language.
- Displays research statistics through interactive visualizations.
- Performs image analysis using Google Gemini Vision.
- Automatically searches the web when required.
- Dynamically updates its knowledge base with newly learned information.
- Successfully deployed on Streamlit Cloud with an interactive user interface.
