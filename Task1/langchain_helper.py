import os
import csv
from dotenv import load_dotenv
from ddgs import DDGS

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

# Load Environment Variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

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
VECTOR_DB = "faiss_index"
DATASET = "dataset.csv"
KNOWLEDGE_UPDATES = "knowledge_updates.csv"

# Create / Update Vector Database
def create_vector_db():
    documents = []
    # Load original dataset
    dataset_loader = CSVLoader(
        file_path=DATASET,
        source_column="prompt"
    )
    documents.extend(dataset_loader.load())
    # Load dynamically learned knowledge
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

# Load QA Chain
def get_qa_chain():
    vectordb = FAISS.load_local(
        VECTOR_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )
    retriever = vectordb.as_retriever(
        search_kwargs={"k": 3}
    )
    prompt = PromptTemplate(
        template="""
You are a helpful customer support chatbot.
Answer ONLY from the given context.
If the answer is NOT present in the context,
reply ONLY with:
I don't know.
Context:
{context}
Question:
{question}
Answer:
""",
        input_variables=["context", "question"]
    )
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    return chain

# Web Search + Gemini Answer
def search_web(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
        if len(results) == 0:
            return None
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
Use them to answer accurately.
If the search results are incomplete, you may use your general knowledge to produce a correct answer.
Web Search Results:
{web_context}
Provide a clear, concise and factual answer.
"""
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        print("Web Search Error:", e)
        return None

# Update Knowledge Base
def update_knowledge_base(question, answer):
    try:
        existing_questions = set()
        # Read dataset.csv
        if os.path.exists(DATASET):
            with open(DATASET, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    existing_questions.add(
                        row["prompt"].strip().lower()
                    )
        # Read knowledge_updates.csv
        if os.path.exists(KNOWLEDGE_UPDATES):
            with open(KNOWLEDGE_UPDATES, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    existing_questions.add(
                        row["prompt"].strip().lower()
                    )
        # Skip duplicate questions
        if question.strip().lower() in existing_questions:
            print("Question already exists.")
            return
        # Save only in knowledge_updates.csv
        with open(
            KNOWLEDGE_UPDATES,
            "a",
            newline="",
            encoding="utf-8"
        ) as f:
            writer = csv.writer(f)
            writer.writerow([question, answer])
        print("New knowledge added successfully.")
        # Rebuild FAISS using dataset.csv + knowledge_updates.csv
        create_vector_db()
        print("Vector Database Updated Successfully.")
    except Exception as e:
        print("Knowledge Base Update Error:", e)

# Test
if __name__ == "__main__":
    create_vector_db()
    print("Vector Database Created Successfully.")