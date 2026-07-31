# 🩺 AI Medical Question Answering Assistant

## 📌 Project Overview

This project is an AI-powered Medical Question Answering Assistant developed using Streamlit, LangChain, Google Gemini, FAISS, HuggingFace Embeddings, and the MedQuAD dataset.

The assistant answers medical questions using a FAISS-based knowledge base created from the MedQuAD dataset. If the required answer is not available in the knowledge base, it searches the web, generates an answer using Google Gemini, and automatically updates its knowledge base for future queries.

---

## 🌐 Live Demo

**Streamlit App:**  
https://internship-task-3.streamlit.app/

**GitHub Repository:**  
https://github.com/tarzsardana-ship-it/Internship-Tasks/tree/main/Task3

---

## 📌 Problem Statement

Build an AI-powered Medical Question Answering Assistant capable of answering healthcare-related questions using the MedQuAD dataset. If the answer is unavailable, the assistant should retrieve relevant information from the web, generate a response using Google Gemini, and update its knowledge base dynamically.

---

## 🚀 Features

- 🩺 Medical Question Answering
- 📚 FAISS-based Medical Knowledge Base
- 🤖 Google Gemini Integration
- 🌐 Automatic Web Search for Unknown Questions
- 🔄 Dynamic Knowledge Base Updates
- 📄 MedQuAD Dataset Integration
- ⚡ Streamlit Web Application

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API
- HuggingFace Embeddings
- FAISS
- DuckDuckGo Search (DDGS)
- Pandas
- XML Parser (ElementTree)

---

## 📂 Project Structure

```text
Task3/
│── main.py
│── langchain_helper.py
│── convert_medquad_to_csv.py
│── dataset.csv
│── medical_dataset.csv
│── knowledge_updates.csv
│── requirements.txt
│── .env.example
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/tarzsardana-ship-it/Internship-Tasks.git
```

### 2. Navigate to the Project Folder

```bash
cd Internship-Tasks/Task3
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

Add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the Application

```bash
streamlit run main.py
```

---

## 📸 How It Works

1. Convert the MedQuAD XML dataset into a CSV file using `convert_medquad_to_csv.py`.
2. Create the FAISS knowledge base from the customer dataset, medical dataset, and knowledge updates.
3. Ask a medical question through the Streamlit interface.
4. If the answer exists in the knowledge base, it is retrieved instantly.
5. If the answer is unavailable, the assistant searches the web and generates an answer using Google Gemini.
6. The newly generated answer is automatically saved and added to the knowledge base for future use.

---

## 📊 Results

- Successfully built an AI-powered Medical Question Answering Assistant.
- Retrieves medical answers from a FAISS-based knowledge base.
- Uses the MedQuAD dataset containing thousands of medical question-answer pairs.
- Performs automatic web search when required.
- Dynamically updates the knowledge base with newly learned information.
- Successfully deployed on Streamlit Cloud with an interactive user interface.