🤖 Customer Service Chatbot with Dynamic Knowledge Base
📌 Project Overview
This project is an AI-powered Customer Service Chatbot developed using LangChain, Google Gemini, FAISS, and Streamlit.
The chatbot answers user queries using a vector database created from a CSV knowledge base. If an answer is unavailable, it automatically searches the web, returns the retrieved information, stores it in a new knowledge file, and updates the vector database without manual intervention.
This enables the chatbot to continuously expand its knowledge over time.
🎯 Problem Statement
Develop a customer service chatbot capable of answering user queries using Retrieval-Augmented Generation (RAG). The chatbot should automatically update its knowledge base whenever new information is found, allowing continuous learning without modifying the original dataset.
🚀 Features
Customer Service Chatbot
Google Gemini LLM
FAISS Vector Database
Retrieval-Augmented Generation (RAG)
Automatic Web Search for Unknown Questions
Dynamic Knowledge Base Updates
Automatic Vector Database Recreation
Streamlit Web Interface
Duplicate Question Detection
Easy Deployment on Streamlit Cloud
🛠 Technologies Used
Python
Streamlit
LangChain
Google Gemini API
FAISS
HuggingFace Embeddings
CSV Dataset
DuckDuckGo Search (DDGS)
📂 Project Structure
Task1/
│
├── main.py
├── langchain_helper.py
├── dataset.csv
├── knowledge_updates.csv
├── requirements.txt
├── README.md
└── .env.example
📊 Dataset
The chatbot uses a CSV dataset containing two columns:
prompt,response
Whenever a new question is answered through web search, it is automatically stored inside:
knowledge_updates.csv
⚙ Methodology
Step 1
Load the dataset from CSV.
Step 2
Generate embeddings using HuggingFace sentence-transformer.
Step 3
Store embeddings inside a FAISS Vector Database.
Step 4
User enters a question.
Step 5
Relevant documents are retrieved from FAISS.
Step 6
Gemini generates the final response.
Step 7
If the answer is not found:
Search the web
Return the answer
Save the new question-answer pair
Rebuild the FAISS database automatically
This enables dynamic expansion of the chatbot's knowledge.
🔄 Dynamic Knowledge Base
Whenever Gemini cannot answer a question:
Search the web
Retrieve the answer
Save it in knowledge_updates.csv
Recreate the FAISS vector database
Future users receive the updated answer directly from the knowledge base
📈 Results
The chatbot successfully:
Answers questions from the existing dataset
Searches the web for unknown questions
Updates the knowledge base automatically
Prevents duplicate entries
Rebuilds the vector database dynamically
Supports continuous learning without manual dataset modification
▶️ Installation
Install dependencies:
pip install -r requirements.txt
▶️ Run the Project
streamlit run main.py
☁️ Deployment
The application is deployed using Streamlit Community Cloud.
Deployment includes:
GitHub Repository
Streamlit Cloud
Google Gemini API Key stored in Streamlit Secrets
📸 Sample Workflow
Create Knowledge Base
Ask a question
Retrieve answer from FAISS
If unavailable, search the web
Save the new knowledge
Update FAISS automatically
Answer future queries directly