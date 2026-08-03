import os
import csv
from dotenv import load_dotenv
from ddgs import DDGS
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
import streamlit as st
from google import genai
from PIL import Image
from langchain_core.documents import Document
import pandas as pd
from collections import Counter
from textblob import TextBlob
# Load Environment Variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is missing. Add it to Streamlit Secrets or your .env file."
    )
client = genai.Client(api_key=GOOGLE_API_KEY)
# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.1,
)

# Embedding Model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VECTOR_DB = os.path.join(BASE_DIR, "faiss_index")
DATASET = os.path.join(BASE_DIR, "dataset.csv")
MEDICAL_DATASET = os.path.join(BASE_DIR, "medical_dataset.csv")
KNOWLEDGE_UPDATES = os.path.join(BASE_DIR, "knowledge_updates.csv")
ARXIV_DATASET = os.path.join(BASE_DIR, "arxiv_dataset.csv")


def create_vector_db():
    documents = []

    # Customer Service Dataset
    if os.path.exists(DATASET):
        dataset_loader = CSVLoader(
            file_path=DATASET,
            source_column="prompt"
        )
        documents.extend(dataset_loader.load())

    # Medical Dataset
    if os.path.exists(MEDICAL_DATASET):
        medical_df = pd.read_csv(MEDICAL_DATASET)
        for _, row in medical_df.iterrows():
         documents.append(
            Document(
                page_content=f"Question: {row['prompt']}\nAnswer: {row['response']}"
            )
        )
    
    # arXiv Research Papers Dataset
    if os.path.exists(ARXIV_DATASET):
        arxiv_df = pd.read_csv(ARXIV_DATASET)

        for _, row in arxiv_df.iterrows():
            documents.append(
                Document(
                    page_content=(
                        f"Research Paper Title: {row['title']}\n"
                        f"Abstract: {row['abstract']}\n"
                        f"Authors: {row['authors']}\n"
                        f"Categories: {row['categories']}\n"
                        f"Published: {row['published']}"
                    )
                )
            )


    # Knowledge Updates
    if os.path.exists(KNOWLEDGE_UPDATES):
        updates_loader = CSVLoader(
            file_path=KNOWLEDGE_UPDATES,
            source_column="prompt"
        )
        documents.extend(updates_loader.load())

    vectordb = FAISS.from_documents(
        documents,
        embeddings
    )

    vectordb.save_local(VECTOR_DB)

def get_qa_chain():
    if not os.path.exists(VECTOR_DB):
        create_vector_db()

    vectordb = FAISS.load_local(
        VECTOR_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 3}
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an AI Knowledge Chatbot.

You are an expert in:
- Customer Support
- Medical Knowledge
- Computer Science Research Papers

Rules:
1. Answer ONLY using the provided context.
2. When answering from research papers, explain concepts in simple language.
3. If the user asks to summarize a paper, provide a concise summary from the context.
4. If the answer is not in the context, reply ONLY:
I don't know.

Context:
{context}

Question:
{input}
"""
    )

    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    return retrieval_chain
# Web Search + Gemini Answer
def search_web(query):
    try:
        print("Starting DDGS")
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
        print("DDGS Finished")
        if not results:
            return None
        print("Sending to Gemini") 
        web_context = ""

        for result in results:
            title = result.get("title", "")
            body = result.get("body", "")

            web_context += f"Title: {title}\n"
            web_context += f"Content: {body}\n\n"

        prompt = f"""
You are an intelligent AI assistant.

The user asked:
{query}

Below are web search results.

{web_context}

Using the search results, provide a clear, concise and factual answer.
"""

        response = llm.invoke(prompt)
        print("Gemini response received")
        return response.content

    except Exception as e:
        print("Web Search Error:", e)
        return None
# sentiment analysis
def analyze_sentiment(text):

    text_lower = text.lower()

    positive_words = [
        "thank", "thanks", "great", "awesome",
        "excellent", "good", "happy", "love",
        "amazing", "wonderful"
    ]

    negative_words = [
        "bad", "worst", "hate", "angry",
        "disappointed", "issue", "problem",
        "poor", "terrible", "sad", "frustrated"
    ]

    if any(word in text_lower for word in positive_words):
        return (
            "Positive",
            "😊",
            "I'm glad you're having a positive experience!\n\n"
        )

    if any(word in text_lower for word in negative_words):
        return (
            "Negative",
            "😔",
            "I'm sorry you're facing this issue. I'll do my best to help.\n\n"
        )

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.2:
        return (
            "Positive",
            "😊",
            "I'm glad you're having a positive experience!\n\n"
        )

    elif polarity < -0.2:
        return (
            "Negative",
            "😔",
            "I'm sorry you're facing this issue. I'll do my best to help.\n\n"
        )

    return (
        "Neutral",
        "🙂",
        ""
    )
# Update Knowledge Base
def update_knowledge_base(question, answer):
    try:
        existing_questions = set()

        if os.path.exists(DATASET):
            with open(DATASET, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    existing_questions.add(
                        row["prompt"].strip().lower()
                    )
        if os.path.exists(MEDICAL_DATASET):
            with open(MEDICAL_DATASET, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    existing_questions.add(
                        row["prompt"].strip().lower()
                    )
        if os.path.exists(ARXIV_DATASET):
            with open(ARXIV_DATASET, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    existing_questions.add(
                    row["title"].strip().lower()
                    )         

        if os.path.exists(KNOWLEDGE_UPDATES):
            with open(KNOWLEDGE_UPDATES, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    existing_questions.add(
                        row["prompt"].strip().lower()
                    )

        if question.strip().lower() in existing_questions:
            print("Question already exists.")
            return

        file_exists = os.path.exists(KNOWLEDGE_UPDATES)

        with open(
            KNOWLEDGE_UPDATES,
            "a",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(["prompt", "response"])

            writer.writerow([question, answer])

        # Add only the new document to the existing FAISS index
        new_doc = Document(
            page_content=f"prompt: {question}\nresponse: {answer}"
        )

        vectordb = FAISS.load_local(
            VECTOR_DB,
            embeddings,
            allow_dangerous_deserialization=True
        )

        vectordb.add_documents([new_doc])

        vectordb.save_local(VECTOR_DB)

        print("Knowledge Base Updated Successfully.")

    except Exception as e:
        print("Knowledge Base Update Error:", e)

#analyze image
def analyze_image(image_file, question):
    try:

        image = Image.open(image_file)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                question,
                image
            ]
        )

        return response.text

    except Exception as e:
        return f"Image Analysis Error: {e}"
#search paper
def search_research_papers(query):
    try:
        if not os.path.exists(ARXIV_DATASET):
            return pd.DataFrame()

        df = pd.read_csv(ARXIV_DATASET)

        query = query.lower()

        results = df[
            df["title"].str.lower().str.contains(query, regex=False, na=False)|
            df["abstract"].str.lower().str.contains(query, regex=False, na=False)
        ]
        return results.head(5)

    except Exception as e:
        print("Research Search Error:", e)
        return pd.DataFrame()
#summarize paper
def summarize_paper(title):
    papers = search_research_papers(title)

    if len(papers) == 0:
        return None

    paper = papers.iloc[0]

    prompt = f"""
You are a research assistant.

Summarize the following research paper in simple language.

Title:
{paper['title']}

Abstract:
{paper['abstract']}
"""

    response = llm.invoke(prompt)

    return response.content
#explain concept
def explain_concept(topic):
    papers = search_research_papers(topic)

    if len(papers) == 0:
        return None

    context = ""

    for _, row in papers.iterrows():
        context += f"""
Title:
{row['title']}

Abstract:
{row['abstract']}

"""

    prompt = f"""
You are an expert Computer Science professor.

Using the research paper abstracts below, explain:

{topic}

Keep the explanation beginner-friendly.

Research Context:

{context}
"""

    response = llm.invoke(prompt)

    return response.content
#research statistics
def get_research_statistics():
    if not os.path.exists(ARXIV_DATASET):
        return [], pd.Series(dtype=int)

    df = pd.read_csv(ARXIV_DATASET)

   

    categories = []

    for cat in df["categories"]:
        categories.extend(str(cat).split())

    top_categories = Counter(categories).most_common(10)

    years = (
        df["published"]
        .astype(str)
        .str[:4]
        .value_counts()
        .sort_index()
    )

    return top_categories, years
# Test
if __name__ == "__main__":
    create_vector_db()
    print("Vector Database Created Successfully.")
