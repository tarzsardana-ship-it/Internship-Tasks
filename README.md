# 🤖 AI Knowledge & Research Chatbot with Sentiment Analysis

An intelligent AI-powered chatbot developed using **Streamlit**, **LangChain**, **Google Gemini 2.5 Flash**, and **FAISS**. This chatbot answers queries from multiple knowledge sources, performs image understanding, searches research papers, automatically updates its knowledge base using web search, and detects user sentiment to provide context-aware responses.

---

# 🚀 Live Demo

### 🌐 Streamlit Application

https://internship-task-5.streamlit.app/

### 💻 GitHub Repository

https://github.com/tarzsardana-ship-it/Internship-Tasks/tree/main/Task5

---

# 📌 Problem Statement

The objective of this project is to enhance an AI-powered chatbot by integrating **Sentiment Analysis** into the existing knowledge-based chatbot developed in previous tasks. The chatbot should identify the emotional tone of user queries (Positive, Negative, or Neutral) and respond appropriately while continuing to provide accurate answers from multiple knowledge sources.

The chatbot also supports image understanding, research paper analysis, medical question answering, customer service assistance, and dynamic knowledge base updates through web search when information is unavailable.

---

# 📚 Datasets Used

### Customer Service Dataset
Used to answer customer support-related queries.

### MedQuAD Dataset
Provides answers to healthcare and medical-related questions.

### arXiv Computer Science Dataset
Used for:
- Research paper search
- Paper summarization
- Concept explanation
- Research statistics

### Dynamic Knowledge Base
`knowledge_updates.csv`

Stores newly learned information obtained from web search so the chatbot continuously improves over time.

---

# ✨ Features

## ✅ Customer Service Question Answering
Answers customer support questions using the customer service dataset.

## ✅ Medical Question Answering
Answers healthcare-related questions using the MedQuAD dataset.

## ✅ Research Paper Search
Searches Computer Science research papers from the arXiv dataset.

## ✅ Research Paper Summarization
Generates concise summaries of research papers using Google Gemini.

## ✅ Concept Explanation
Explains complex technical concepts in simple language.

## ✅ Research Statistics Dashboard
Displays research statistics with charts using Matplotlib.

## ✅ Image Understanding
Allows users to upload an image and ask questions about it using Gemini Vision.

## ✅ Dynamic Knowledge Base
When the answer is unavailable:
- Searches the web using DuckDuckGo.
- Generates an answer using Gemini.
- Saves the new knowledge into `knowledge_updates.csv`.
- Updates the FAISS knowledge base automatically.

## ✅ Sentiment Analysis (Task 5)
Detects the user's sentiment before answering.

Supported sentiments:
- 😊 Positive
- 😔 Negative
- 🙂 Neutral

The chatbot generates an appropriate response based on the detected sentiment while continuing to answer the user's query.

---

# ⚙️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini 2.5 Flash
- Google Gemini Vision
- FAISS Vector Database
- HuggingFace Embeddings
- Sentence Transformers
- DuckDuckGo Search (DDGS)
- TextBlob
- Pandas
- Matplotlib
- Pillow

---

# 📂 Project Structure

```
Task5/
│
├── main.py
├── langchain_helper.py
├── dataset.csv
├── medical_dataset.csv
├── arxiv_dataset.csv
├── knowledge_updates.csv
├── prepare_arxiv_dataset.py
├── convert_medquad_to_csv.py
├── requirements.txt
├── README.md
├── faiss_index/
└── Screenshots/
```

---

# 🔄 Methodology / Workflow

1. User enters a question.
2. Sentiment Analysis detects whether the message is Positive, Negative, or Neutral.
3. The chatbot searches the FAISS knowledge base.
4. Gemini generates an answer using the retrieved documents.
5. If the answer is unavailable:
   - DuckDuckGo web search is performed.
   - Gemini generates an answer from web results.
   - The new information is stored in `knowledge_updates.csv`.
   - The FAISS knowledge base is updated automatically.
6. If an image is uploaded, Gemini Vision analyzes the image and answers image-related questions.
7. The chatbot displays:
   - Detected Sentiment
   - Final AI Response

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/tarzsardana-ship-it/Internship-Tasks.git
```

Go to the project folder:

```bash
cd Internship-Tasks/Task5
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
GITHUB_TOKEN=YOUR_GITHUB_TOKEN
```

Run the application:

```bash
streamlit run main.py
```

---

# 📸 Results

### 😊 Positive Sentiment

**Input**

```
Thank you so much for helping me.
```

**Output**
- Sentiment: Positive
- Friendly response generated before answering the query.

---

### 😔 Negative Sentiment

**Input**

```
I am very disappointed.
```

**Output**
- Sentiment: Negative
- Empathetic response generated before answering.

---

### 🙂 Neutral Sentiment

**Input**

```
What is diabetes?
```

**Output**
- Sentiment: Neutral
- Medical answer retrieved from the knowledge base.

---

### 📚 Research Paper Search
Searches relevant Computer Science papers using the arXiv dataset.

---

### 📄 Paper Summarization
Generates concise summaries of research papers.

---

### 💡 Concept Explanation
Explains technical concepts in simple language.

---

### 📷 Image Analysis
Analyzes uploaded images using Gemini Vision.

---

### 📊 Research Statistics
Displays charts showing research categories and publication trends.
