🤖 AI Knowledge & Research Chatbot
📌 Project Overview

This project is an AI-powered Knowledge & Research Chatbot developed using Streamlit, LangChain, Google Gemini, FAISS, HuggingFace Embeddings, DDGS (DuckDuckGo Search), and multiple knowledge sources including Customer Support, Medical (MedQuAD), and Computer Science Research Papers (arXiv).

The chatbot answers questions using a FAISS-based knowledge base built from multiple datasets. If the requested information is unavailable, it automatically searches the web, generates an answer using Google Gemini, updates its knowledge base, and remembers the answer for future queries.

In addition to general question answering, the chatbot also supports research paper search, paper summarization, concept explanation, research statistics visualization, and image analysis using Gemini Vision.

🌐 Live Demo
Streamlit App

https://internship-task-4.streamlit.app/

GitHub Repository

https://github.com/tarzsardana-ship-it/Internship-Tasks/tree/main/Task4

📌 Problem Statement

Build an AI-powered Knowledge & Research Chatbot capable of answering questions from multiple domains including customer support, healthcare, and computer science research papers. The chatbot should retrieve answers from a FAISS knowledge base and, when necessary, search the web using DuckDuckGo, generate responses using Google Gemini, and dynamically update its knowledge base for future interactions.

🚀 Features
🤖 AI-powered Knowledge Chatbot
📚 Multi-Dataset Knowledge Base
🩺 Medical Question Answering (MedQuAD)
💼 Customer Support Question Answering
📄 Computer Science Research Paper Search (arXiv)
📝 Research Paper Summarization
💡 Technical Concept Explanation
📊 Research Statistics Visualization
🖼️ Image Analysis using Gemini Vision
🌐 Automatic Web Search for Unknown Questions
🔄 Dynamic Knowledge Base Updates
⚡ FAISS Vector Search
🧠 Google Gemini Integration
🌍 Streamlit Interactive Web Application
🛠️ Technologies Used
Python
Streamlit
LangChain
Google Gemini API
HuggingFace Embeddings
FAISS
DuckDuckGo Search (DDGS)
Pandas
Matplotlib
Pillow
MedQuAD Dataset
arXiv Research Papers Dataset
📂 Project Structure
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
⚙️ Installation
1. Clone the Repository
git clone https://github.com/tarzsardana-ship-it/Internship-Tasks.git
2. Navigate to the Project Folder
cd Internship-Tasks/Task4
3. Install Dependencies
pip install -r requirements.txt
4. Create a .env File

Add your Google Gemini API Key:

GOOGLE_API_KEY=your_api_key_here
5. Run the Application
streamlit run main.py
📸 How It Works
Load the Customer Support, Medical (MedQuAD), Research Paper (arXiv), and Knowledge Updates datasets.
Create a FAISS vector database from all available datasets.
Select a chatbot mode from the Streamlit interface.
Ask a question, search for research papers, summarize papers, explain concepts, upload an image, or explore research statistics.
If the answer exists in the FAISS knowledge base, it is retrieved instantly.
If the answer is unavailable, the chatbot performs a DuckDuckGo web search, generates an answer using Google Gemini, and stores it in the knowledge base.
Future queries for the same question are answered directly from the updated knowledge base.
💬 Chat Modes
🧠 General Chat

Answers questions using Customer Support, Medical, Research Paper, and dynamically learned knowledge.

📄 Research Paper Search

Searches the arXiv dataset and displays matching research papers with their title, authors, category, publication date, and abstract.

📝 Paper Summarization

Generates an easy-to-understand summary of a selected research paper.

💡 Concept Explanation

Explains technical concepts using relevant research paper abstracts in beginner-friendly language.

📊 Research Statistics

Displays visual statistics including:

Top Research Categories
Papers Published by Year
🖼️ Image Analysis

Analyzes uploaded images and answers questions about them using Google Gemini Vision.

📊 Results
Successfully built an AI-powered multi-domain Knowledge & Research Chatbot.
Retrieves answers from Customer Support, Medical, and Research Paper datasets.
Supports semantic search using FAISS vector embeddings.
Searches Computer Science research papers from the arXiv dataset.
Generates simplified paper summaries and concept explanations.
Performs image understanding using Google Gemini Vision.
Automatically searches the web when answers are unavailable.
Dynamically updates the knowledge base with newly learned information.
Visualizes research statistics using interactive charts.
Successfully deployed on Streamlit Cloud with an interactive user interface.