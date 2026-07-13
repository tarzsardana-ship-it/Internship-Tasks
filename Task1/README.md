# 🤖 Customer Service Chatbot with Dynamic Knowledge Base
## 📌 Project Overview
This project is an AI-powered Customer Service Chatbot built using LangChain, Google Gemini, FAISS, Hugging Face Embeddings, and Streamlit.
The chatbot answers user queries using a custom knowledge base created from a CSV dataset. If an answer is unavailable, it automatically searches the web, returns the result, stores the new information, and updates its vector database. This enables the chatbot to continuously expand its knowledge over time.

# 🎯 Problem Statement
Develop a chatbot capable of dynamically expanding its knowledge base.
The chatbot should:
- Answer questions using a custom dataset.
- Detect when information is unavailable.
- Search the web for missing information.
- Store newly discovered knowledge.
- Update the vector database automatically.
- Improve responses over time without manual dataset editing.

# 🚀 Features
- Customer Service Chatbot
- Retrieval-Augmented Generation (RAG)
- Google Gemini LLM
- FAISS Vector Database
- Hugging Face Sentence Transformers
- Automatic Web Search using DDGS
- Dynamic Knowledge Base Expansion
- Automatic Vector Database Update
- Duplicate Question Detection
- Streamlit Web Interface

# 🛠 Technologies Used
- Python
- Streamlit
- LangChain
- Google Gemini API
- Hugging Face Embeddings
- FAISS
- DDGS (DuckDuckGo Search)
- CSV
- dotenv

# 📂 Project Structure
Task1/
│
├── main.py
├── langchain_helper.py
├── dataset.csv
├── knowledge_updates.csv
├── .env.example
├── requirements.txt
├── .streamlit/
│   └── secrets.toml
└── README.md

# 📊 Dataset
The chatbot uses:
- dataset.csv (original knowledge)
- knowledge_updates.csv (new knowledge learned automatically)
Dataset Columns:
| prompt | response |
|---------|-----------|

# ⚙️ Methodology
### Step 1
Load the dataset using CSVLoader.
### Step 2
Generate embeddings using:
sentence-transformers/all-MiniLM-L6-v2
### Step 3
Store embeddings in a FAISS Vector Database.
### Step 4
User enters a question.
### Step 5
Retrieve the most relevant documents using FAISS.
### Step 6
Google Gemini generates an answer.
### Step 7
If Gemini cannot answer:
- Perform web search using DDGS.
- Retrieve relevant information.
- Save the new Question–Answer pair in knowledge_updates.csv.
- Rebuild the FAISS knowledge base automatically.
This allows the chatbot to continuously learn from new information.

# 🔄 Workflow
User Question
      │
      ▼
 FAISS Search
      │
      ▼
Gemini Response
      │
      ▼
Answer Found?
      │
 ┌────┴────┐
 │         │
Yes        No
 │         │
 ▼         ▼
Return   Web Search
Answer      │
            ▼
 Save to knowledge_updates.csv
            │
            ▼
 Rebuild FAISS Index
            │
            ▼
 Return Updated Answer

# ▶️ Installation
Clone the repository:
git clone 

Install dependencies:
pip install -r requirements.txt

Add your Gemini API Key.
For Streamlit Cloud:
.streamlit/secrets.toml
GOOGLE_API_KEY="YOUR_API_KEY"

Run the application:
streamlit run main.py

# 📸 Application
The application provides:
- Create Knowledge Base button
- Question Input
- AI Generated Answer
- Automatic Web Search
- Dynamic Knowledge Base Update
  
# 📈 Results
Successfully implemented:
✅ Customer Service Chatbot
✅ Dynamic Knowledge Base
✅ Automatic Web Search
✅ FAISS Vector Database
✅ Retrieval-Augmented Generation (RAG)
✅ Automatic Knowledge Base Expansion
✅ Streamlit Deployment
