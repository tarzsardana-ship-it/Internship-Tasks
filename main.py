import streamlit as st
import matplotlib.pyplot as plt
from langchain_helper import (
    create_vector_db,
    get_qa_chain,
    search_web,
    update_knowledge_base,
    analyze_image,
    search_research_papers,
    summarize_paper,
    explain_concept,
    get_research_statistics,
    analyze_sentiment
)
from translator_helper import (
    detect_language,
    translate_to_english,
    translate_from_english
)

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="AI Knowledge & Research Chatbot",
    page_icon="🤖"
)
st.title("🤖 AI Knowledge & Research Chatbot")
# Conversation Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.write("""
### Features

This chatbot can answer questions from:

• Customer Service Dataset

• Medical Dataset (MedQuAD)

• Computer Science Research Papers (arXiv)

• Uploaded Images

If information is unavailable, it searches the web and updates its knowledge base automatically.

You can also:

• Search research papers

• Summarize research papers

• Explain technical concepts

• Ask follow-up questions
""")
st.subheader("📷 Image Upload")

uploaded_image = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image:
    st.image(uploaded_image)
# ---------------------------------
# Create Knowledge Base
# ---------------------------------
if st.button("Create Knowledgebase"):

    with st.spinner("Creating Knowledge Base..."):

        create_vector_db()

    st.success("Knowledge Base Created Successfully!")

# ---------------------------------
# Ask Question
# ---------------------------------
st.subheader("🧠 Chat Mode")

chat_mode = st.selectbox(
    "Choose a mode",
    [
        "General Chat",
        "Research Paper Search",
        "Paper Summarization",
        "Concept Explanation",
        "Research Statistics"
    ]
)
question = st.text_input(
    "Ask a question or enter a research topic"
)

if question:

    # -----------------------------
    # Image Analysis
    # -----------------------------
    if uploaded_image:

        with st.spinner("Analyzing Image..."):

            answer = analyze_image(
                uploaded_image,
                question
            )

        st.subheader("Image Analysis")
        st.write(answer)
        st.stop()

    # -----------------------------
    # Research Paper Search
    # -----------------------------
    if chat_mode == "Research Paper Search":

        papers = search_research_papers(question)

        st.subheader("Research Papers")

        if len(papers) == 0:
            st.warning("No matching papers found.")

        else:

            for _, row in papers.iterrows():

                st.markdown(f"### {row['title']}")

                st.write(f"**Authors:** {row['authors']}")

                st.write(f"**Category:** {row['categories']}")

                st.write(f"**Published:** {row['published']}")

                st.write(row["abstract"])

                st.divider()

    # -----------------------------
    # Paper Summarization
    # -----------------------------
    elif chat_mode == "Paper Summarization":

        summary = summarize_paper(question)

        if summary:

            st.subheader("Paper Summary")

            st.write(summary)

        else:

            st.warning("Paper not found.")

    # -----------------------------
    # Concept Explanation
    # -----------------------------
    elif chat_mode == "Concept Explanation":

        explanation = explain_concept(question)

        if explanation:

            st.subheader("Concept Explanation")

            st.write(explanation)

        else:

            st.warning("Concept not found.")

    # -----------------------------
    # General Chat
    # -----------------------------
    else:

        with st.spinner("Searching..."):
            #detect user's language
            user_language = detect_language(question)
            #translate to english if needed
            english_question = translate_to_english(question,user_language)
            sentiment, emoji, prefix = analyze_sentiment(question)
            chain = get_qa_chain()

            history = ""

            for q, a in st.session_state.chat_history:
                history += f"User: {q}\nAssistant: {a}\n"

            full_question = f"""
            Conversation History:
            {history}

            Current Question:
            {english_question}
            """

            response = chain.invoke({"input": full_question})

            answer = response["answer"].strip()

            if "don't know" in answer.lower():

                st.info("Searching the web...")

                web_answer = search_web(question)

                if web_answer:

                    update_knowledge_base(question, web_answer)

                    answer = web_answer

                    st.success("Knowledge Base Updated Successfully!")

                else:

                    answer = "Sorry, I couldn't find an answer."
            #translate answer back to user's language
            answer = translate_from_english(answer,user_language)
            # Save conversation history (stored in English)
            st.session_state.chat_history.append(
                (english_question, answer)
            )

            # Keep only the latest 10 exchanges
            if len(st.session_state.chat_history) > 10:
                st.session_state.chat_history.pop(0)

        st.subheader("Detected Language")
        st.success(user_language.upper())
        st.subheader("Detected Sentiment")
        st.success(f"{emoji} {sentiment}")
        st.subheader("Answer")
        st.write(prefix + answer)
        
if chat_mode == "Research Statistics":

    st.subheader("Research Statistics")

    categories, years = get_research_statistics()

    st.write("### Top Research Categories")

    cat_names = [x[0] for x in categories]
    cat_counts = [x[1] for x in categories]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(cat_names, cat_counts)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

    st.write("### Papers by Year")

    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.plot(years.index, years.values, marker="o")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig2)