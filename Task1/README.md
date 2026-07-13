# 🤖 Customer Service Chatbot with Dynamic Knowledge Base

## 📌 Project Overview
This project is an AI-powered Customer Service Chatbot built using LangChain, Google Gemini, FAISS, Hugging Face Embeddings, and Streamlit.
The chatbot answers user queries using a custom knowledge base created from a CSV dataset. When the required information is unavailable in the knowledge base, it automatically searches the web, retrieves relevant information, stores it, and updates the vector database. This enables the chatbot to continuously expand its knowledge base and provide improved responses over time.
---

# 🔗 Project Links
**GitHub Repository**
https://github.com/tarzsardana-ship-it/Internship-Tasks/tree/main/Task1

**Live Streamlit Application**
https://internship-task-1.streamlit.app/
---

# 🎯 Problem Statement
Implement a system for dynamically expanding the chatbot's knowledge base. Create a mechanism to periodically update the vector database with new information from specified sources. The chatbot should automatically incorporate new information into its responses over time.
---

# 🚀 Features
- AI-powered Customer Service Chatbot
- Retrieval-Augmented Generation (RAG)
- Google Gemini Integration
- FAISS Vector Database
- Hugging Face Sentence Transformer Embeddings
- Automatic Web Search using DDGS
- Dynamic Knowledge Base Expansion
- Automatic Vector Database Update
- Duplicate Question Detection
- Interactive Streamlit Web Interface
---

# 🛠️ Technologies Used
- Python
- Streamlit
- LangChain
- Google Gemini API
- Hugging Face Sentence Transformers
- FAISS
- DDGS (DuckDuckGo Search)
- CSV
- python-dotenv
---

# 📂 Project Structure
Task1/
│
├── main.py
├── langchain_helper.py
├── dataset.csv
├── knowledge_updates.csv
├── requirements.txt
├── .env.example
└── README.md
---

# 📊 Dataset
The chatbot uses two CSV files:

- **dataset.csv** – Contains the initial knowledge base.
- **knowledge_updates.csv** – Stores newly discovered question-answer pairs obtained through web search.
Both datasets use the following columns: prompt and response
---

# ⚙️ Methodology
1. Load the dataset using LangChain's CSVLoader.
2. Generate embeddings using the **sentence-transformers/all-MiniLM-L6-v2** model.
3. Store embeddings in a FAISS Vector Database.
4. Retrieve relevant documents based on the user's query.
5. Generate responses using Google Gemini.
6. If the answer is unavailable:
   - Search the web using DDGS.
   - Retrieve relevant information.
   - Save the new question-answer pair in knowledge_updates.csv.
   - Rebuild the FAISS vector database automatically.
7. Return the updated response to the user.
---

# 🔄 Workflow

User Question
      │
      ▼
Retrieve Relevant Documents
      │
      ▼
 Google Gemini
      │
      ▼
Answer Available?
      │
 ┌────┴────┐
 │         │
Yes        No
 │         │
 ▼         ▼
Return   Search Web
Answer      │
            ▼
Store New Knowledge
            │
            ▼
Update FAISS Database
            │
            ▼
Return Updated Answer

---

# ▶️ Installation

Clone the repository:
git clone https://github.com/tarzsardana-ship-it/Internship-Tasks.git

Navigate to the project folder:
cd Internship-Tasks/Task1

Install the required dependencies:
pip install -r requirements.txt

Create a .env file (or configure Streamlit Secrets) and add your Google Gemini API key:
GOOGLE_API_KEY=YOUR_API_KEY

Run the application:
streamlit run main.py

---

# 📈 Results
The chatbot successfully:
- Answers questions using a custom knowledge base.
- Retrieves contextual information using FAISS.
- Searches the web when information is unavailable.
- Automatically stores newly acquired knowledge.
- Updates the vector database without manual intervention.
- Provides continuously improving responses through dynamic knowledge expansion.
