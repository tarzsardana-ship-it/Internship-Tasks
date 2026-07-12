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


def create_vector_db():
    documents = []

    dataset_loader = CSVLoader(
        file_path=DATASET,
        source_column="prompt"
    )
    documents.extend(dataset_loader.load())

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
You are a helpful customer support chatbot.

Answer ONLY from the given context.

If the answer is not present in the context,
reply ONLY with:

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
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))

        if not results:
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

{web_context}

Using the search results, provide a clear, concise and factual answer.
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

        if os.path.exists(DATASET):
            with open(DATASET, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    existing_questions.add(
                        row["prompt"].strip().lower()
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

        create_vector_db()

        print("Knowledge Base Updated Successfully.")

    except Exception as e:
        print("Knowledge Base Update Error:", e)


# Test
if __name__ == "__main__":
    create_vector_db()
    print("Vector Database Created Successfully.")