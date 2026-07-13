# 🤖 Multimodal AI Customer Support Assistant 

## 📌 Project Overview

This project is a Multimodal AI Customer Support Assistant developed using Streamlit, LangChain, Google Gemini, FAISS, and DuckDuckGo Search.

The assistant answers customer questions using a FAISS knowledge base. If an answer is not available in the dataset, it searches the web, generates an answer using Gemini, and updates its knowledge base automatically. It also allows users to upload an image and ask questions related to it using Gemini Vision.

---

## 🌐 Live Demo

**Streamlit App:**  
https://internship-task-2.streamlit.app/

**GitHub Repository:**  
https://github.com/tarzsardana-ship-it/Internship-Tasks/tree/main/Task2

---

## 📌 Problem Statement

Build a Multimodal AI Customer Support Assistant that can answer customer queries using a knowledge base, search the web when required, update its knowledge automatically, and understand uploaded images using Google's Gemini Vision model.

---

## 🚀 Features

- 📚 Knowledge Base using FAISS
- 💬 Customer Question Answering
- 🌐 Automatic Web Search for Unknown Questions
- 🔄 Dynamic Knowledge Base Updates
- 🖼️ Image Upload Support
- 🤖 Image Analysis using Gemini Vision
- ⚡ Streamlit Web Application

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API
- Google GenAI SDK
- HuggingFace Embeddings
- FAISS
- DuckDuckGo Search (DDGS)
- Pillow

---

## 📂 Project Structure

```
Task2/
│── main.py
│── langchain_helper.py
│── dataset.csv
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
cd Internship-Tasks/Task2
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

1. Create the Knowledge Base.
2. Ask customer support questions.
3. If the answer exists in the dataset, it is retrieved from the FAISS knowledge base.
4. If the answer is not found, the assistant searches the web, generates an answer using Gemini, and updates its knowledge base automatically.
5. Upload an image and ask questions related to it.
6. Gemini Vision analyzes the image and provides an intelligent response.

---

## 📊 Results

- Successfully built and deployed a Multimodal AI Customer Support Assistant.
- Retrieves answers from a FAISS-based knowledge base.
- Performs automatic web search when an answer is unavailable in the dataset.
- Updates the knowledge base dynamically with newly learned information.
- Accepts image uploads and answers questions based on image content using Gemini Vision.
- Successfully deployed on Streamlit Cloud with an interactive user interface.

