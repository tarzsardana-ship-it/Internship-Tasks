# 🤖 AI Knowledge & Research Chatbot

An AI-powered chatbot developed during my internship using Python, Streamlit, LangChain, Google Gemini, FAISS, HuggingFace Embeddings, and NLP technologies.

The project was completed through 6 progressive tasks, adding customer service Q&A, medical Q&A, research paper analysis, image understanding, sentiment analysis, multilingual support, conversation memory, and dynamic knowledge-base updates.

## 🚀 Live Demo

🌐 Streamlit Application  
https://internship-tasks.streamlit.app/

💻 GitHub Repository  
https://github.com/tarzsardana-ship-it/Internship-Tasks

## 📌 Problem Statement

The objective of this internship project was to develop an intelligent AI chatbot capable of answering questions from multiple knowledge sources.

The chatbot was progressively enhanced over 6 tasks with features such as customer service assistance, medical question answering, research paper analysis, image understanding, sentiment analysis, multilingual communication, conversation memory, and automatic web-based knowledge updates.

## 🎯 Tasks Completed

### Task 1 – Basic Chatbot

- Developed the initial AI chatbot.
- Implemented basic question-answering functionality.
- Created the foundation for the complete chatbot system.

### Task 2 – Customer Service Chatbot

- Added Customer Service Dataset.
- Implemented LangChain-based question answering.
- Integrated FAISS vector database for knowledge retrieval.
- Added web search for questions unavailable in the knowledge base.
- Implemented dynamic knowledge updates.

### Task 3 – Medical Question Answering

- Integrated the MedQuAD medical dataset.
- Added medical question answering.
- Extended the chatbot knowledge base with healthcare information.
- Used FAISS for retrieval from the medical dataset.

### Task 4 – AI Knowledge & Research Chatbot

- Added Computer Science research papers from arXiv.
- Implemented research paper search.
- Added research paper summarization.
- Added technical concept explanation.
- Added research statistics.
- Added image understanding using Gemini Vision.

### Task 5 – Sentiment Analysis

- Added sentiment analysis to the chatbot.
- Detects Positive, Negative, and Neutral sentiments.
- Generates context-aware responses according to the detected sentiment.

### Task 6 – Multilingual AI Knowledge & Research Chatbot

- Added multilingual question-answering.
- Detects the language of the user's question.
- Translates questions into English for knowledge-base retrieval.
- Translates answers back into the user's language.
- Added conversation history.
- Added follow-up question support.
- Improved dynamic knowledge-base functionality.

## 📚 Datasets Used

### Customer Service Dataset

`dataset.csv`

Used for customer support-related questions and answers.

### MedQuAD Medical Dataset

`medical_dataset.csv`

Used for healthcare and medical question answering.

### arXiv Research Dataset

`arxiv_dataset.csv`

Used for:

- Research paper search
- Paper summarization
- Technical concept explanation
- Research statistics

### Dynamic Knowledge Base

`knowledge_updates.csv`

Stores new information obtained through web search when the chatbot does not have the required information.

## ✨ Features

### 🤖 Customer Service Q&A

Answers customer support questions using the Customer Service Dataset.

### 🏥 Medical Q&A

Answers healthcare-related questions using the MedQuAD dataset.

### 📄 Research Paper Search

Searches Computer Science research papers from the arXiv dataset.

### 📝 Research Paper Summarization

Generates simple and concise summaries of research papers using Google Gemini.

### 💡 Concept Explanation

Explains technical concepts in beginner-friendly language using research paper information.

### 📊 Research Statistics

Displays research categories and publication trends using Matplotlib charts.

### 📷 Image Understanding

Allows users to upload an image and ask questions about it using Gemini Vision.

### 😊 Sentiment Analysis

Detects the sentiment of the user's message.

Supported sentiments:

- 😊 Positive
- 😔 Negative
- 🙂 Neutral

### 🌐 Multilingual Support

The chatbot can detect the user's language, translate the question into English for processing, and translate the final answer back into the user's language.

### 💬 Conversation Memory

Maintains recent conversation history and supports follow-up questions such as:

- Explain this
- Explain it
- Translate this
- Summarize this

### 🔎 Web Search

If the required information is not available in the knowledge base, the chatbot searches the web using DuckDuckGo.

### 🧠 Dynamic Knowledge Base

When an unknown question is answered using web search:

1. Web search is performed.
2. Gemini generates the answer.
3. The answer is stored in `knowledge_updates.csv`.
4. The new information is added to the FAISS index.

## ⚙️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini 2.5 Flash
- Gemini Vision
- FAISS Vector Database
- HuggingFace Embeddings
- Sentence Transformers
- DuckDuckGo Search (DDGS)
- TextBlob
- Pandas
- Matplotlib
- Pillow
- Regular Expressions

## 📂 Project Structure

~~~text
Internship-Tasks/
│
├── faiss_index/
├── .env.example
├── .gitignore
├── arxiv_dataset.csv
├── convert_medquad_to_csv.py
├── dataset.csv
├── knowledge_updates.csv
├── langchain_helper.py
├── main.py
├── medical_dataset.csv
├── prepare_arxiv_dataset.py
├── README.md
├── requirements.txt
└── translator_helper.py
~~~

## 🔄 Workflow

1. User enters a question.
2. The chatbot detects the user's language.
3. If required, the question is translated into English.
4. The question is processed using the knowledge base.
5. FAISS retrieves relevant information.
6. LangChain passes the retrieved context to Gemini.
7. Gemini generates the answer using the available context.
8. If the answer is unavailable, the chatbot performs a web search.
9. Gemini generates an answer using the web results.
10. The new information is stored in `knowledge_updates.csv`.
11. The FAISS knowledge base is updated.
12. The answer is translated back into the user's language.
13. The chatbot displays the final response along with detected language and sentiment.

## 🧠 RAG Architecture

The chatbot uses Retrieval-Augmented Generation (RAG).

~~~text
User Question
      ↓
Language Detection
      ↓
Translation to English
      ↓
FAISS Vector Database
      ↓
Relevant Documents Retrieved
      ↓
LangChain Retrieval Chain
      ↓
Google Gemini
      ↓
Answer
      ↓
Translation to User Language
      ↓
Final Response
~~~

If the information is not available:

~~~text
Question
   ↓
FAISS Retrieval
   ↓
"I don't know"
   ↓
DuckDuckGo Web Search
   ↓
Gemini
   ↓
New Answer
   ↓
knowledge_updates.csv
   ↓
FAISS Updated
~~~

## ⚙️ Installation

Clone the repository:

~~~bash
git clone https://github.com/tarzsardana-ship-it/Internship-Tasks.git
~~~

Go to the project directory:

~~~bash
cd Internship-Tasks
~~~

Install the required dependencies:

~~~bash
pip install -r requirements.txt
~~~

Create a `.env` file and add your Google API key:

~~~text
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
~~~

Run the Streamlit application:

~~~bash
streamlit run main.py
~~~

The application will open in your browser.

## 🔐 Environment Variables

The project uses environment variables for API credentials.

~~~text
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
~~~

For deployment, the API key can be added through Streamlit Secrets.

## 📊 Output

The chatbot can provide:

- Customer service answers
- Medical answers
- Research paper information
- Research paper summaries
- Technical concept explanations
- Image-based answers
- Sentiment detection
- Multilingual responses
- Follow-up answers
- Web-based answers for unknown questions
- Automatically updated knowledge

## 📸 Main Functionalities

### Customer Service

Answers questions related to customer support using the dataset.

### Medical Questions

Retrieves answers from the MedQuAD medical dataset.

### Research

Provides research paper search, summarization, concept explanation, and statistics.

### Image Analysis

Users can upload an image and ask questions about it using Gemini Vision.

### Multilingual Chat

Users can ask questions in different languages and receive answers in the same language.

### Sentiment Analysis

The chatbot identifies whether the user's message is Positive, Negative, or Neutral and provides an appropriate response.

### Dynamic Knowledge

Unknown questions are searched on the web and the newly obtained information is added to the knowledge base.
