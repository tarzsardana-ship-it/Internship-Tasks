import streamlit as st
import matplotlib.pyplot as plt
import re

from langchain_helper import (
    create_vector_db,
    get_qa_chain,
    get_dataset_answer,
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


# ---------------------------------
# Conversation Memory
# ---------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---------------------------------
# Features
# ---------------------------------

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


# ---------------------------------
# Image Upload
# ---------------------------------

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
# Chat Mode
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


# ---------------------------------
# Question Handling
# ---------------------------------

if question:

    # ---------------------------------
    # Image Analysis
    # ---------------------------------

    if uploaded_image:

        with st.spinner("Analyzing Image..."):

            answer = analyze_image(
                uploaded_image,
                question
            )

        st.subheader("Image Analysis")
        st.write(answer)

        st.stop()


    # ---------------------------------
    # Research Paper Search
    # ---------------------------------

    if chat_mode == "Research Paper Search":

        papers = search_research_papers(question)

        st.subheader("Research Papers")

        if len(papers) == 0:

            st.warning("No matching papers found.")

        else:

            for _, row in papers.iterrows():

                st.markdown(
                    f"### {row['title']}"
                )

                st.write(
                    f"**Authors:** {row['authors']}"
                )

                st.write(
                    f"**Category:** {row['categories']}"
                )

                st.write(
                    f"**Published:** {row['published']}"
                )

                st.write(
                    row["abstract"]
                )

                st.divider()


    # ---------------------------------
    # Paper Summarization
    # ---------------------------------

    elif chat_mode == "Paper Summarization":

        summary = summarize_paper(question)

        if summary:

            st.subheader("Paper Summary")
            st.write(summary)

        else:

            st.warning("Paper not found.")


    # ---------------------------------
    # Concept Explanation
    # ---------------------------------

    elif chat_mode == "Concept Explanation":

        explanation = explain_concept(question)

        if explanation:

            st.subheader("Concept Explanation")
            st.write(explanation)

        else:

            st.warning("Concept not found.")


    # ---------------------------------
    # General Chat
    # ---------------------------------

    else:

        with st.spinner("Searching..."):

            # ---------------------------------
            # Detect User Language
            # ---------------------------------

            user_language = detect_language(question)


            # ---------------------------------
            # Translate User Question to English
            # ---------------------------------

            english_question = translate_to_english(
                question,
                user_language
            )


            # ---------------------------------
            # Normalize Question
            # ---------------------------------

            english_question = re.sub(
                r'[^\w\s]',
                '',
                english_question
            ).strip().lower()


            # ---------------------------------
            # Sentiment Analysis
            # ---------------------------------

            sentiment, emoji, prefix = analyze_sentiment(
                question
            )


            # =================================================
            # CHECK WHETHER USER IS ASKING A FOLLOW-UP
            # =================================================

            followup_words = [
                "this",
                "that",
                "it",
                "explain this",
                "translate this",
                "summarize this",
                "explain it",
                "translate it",
                "summarize it",
                "explain that",
                "translate that",
                "summarize that"
            ]


            followup = (
                len(st.session_state.chat_history) > 0
                and any(
                    word in english_question
                    for word in followup_words
                )
            )


            # =================================================
            # DETECT REQUESTED OUTPUT LANGUAGE
            # =================================================

            requested_language = None

            language_patterns = {
                "hindi": "hi",
                "spanish": "es",
                "french": "fr",
                "english": "en"
            }


            for language_name, language_code in language_patterns.items():

                if language_name in english_question:

                    requested_language = language_code
                    break


            # =================================================
            # FOLLOW-UP QUESTION
            # =================================================

            if followup:

                # Get previous conversation
                last_question, last_answer = (
                    st.session_state.chat_history[-1]
                )


                # ---------------------------------------------
                # If user specifically requested a language
                # ---------------------------------------------

                if requested_language:

                    english_answer = last_answer

                    answer = translate_from_english(
                        english_answer,
                        requested_language
                    )


                    # Save follow-up in history
                    st.session_state.chat_history.append(
                        (
                            english_question,
                            english_answer
                        )
                    )


                else:

                    # User didn't specify a target language.
                    # Use their detected language.

                    english_answer = last_answer

                    answer = translate_from_english(
                        english_answer,
                        user_language
                    )


                    st.session_state.chat_history.append(
                        (
                            english_question,
                            english_answer
                        )
                    )


                # Keep only latest 10 exchanges

                if len(st.session_state.chat_history) > 10:

                    st.session_state.chat_history.pop(0)


                st.subheader("Detected Language")
                st.success(
                    user_language.upper()
                )

                st.subheader("Detected Sentiment")
                st.success(
                    f"{emoji} {sentiment}"
                )

                st.subheader("Answer")
                st.write(
                    prefix + answer
                )


            # =================================================
            # NORMAL / NEW QUESTION
            # =================================================

            else:

                # ---------------------------------------------
                # FIRST: Check Customer Service Dataset
                # ---------------------------------------------

                dataset_answer = get_dataset_answer(
                    english_question
                )


                if dataset_answer:

                    # Direct dataset answer
                    english_answer = dataset_answer


                else:

                    # -----------------------------------------
                    # Use FAISS / Medical Dataset / Knowledge
                    # -----------------------------------------

                    chain = get_qa_chain()


                    response = chain.invoke(
                        {
                            "input": english_question
                        }
                    )


                    answer = response["answer"].strip()


                    # -----------------------------------------
                    # Web Search if answer is unknown
                    # -----------------------------------------

                    normalized_question = (
                        english_question
                        .strip()
                        .lower()
                    )


                    if "don't know" in answer.lower():

                        if normalized_question not in [
                            "what is your name",
                            "who are you",
                            "who made you",
                            "hello",
                            "hi",
                            "hey"
                        ]:

                            st.info(
                                "Searching the web..."
                            )


                            web_answer = search_web(
                                question
                            )


                            if web_answer:

                                update_knowledge_base(
                                    english_question,
                                    web_answer
                                )


                                answer = web_answer


                                st.success(
                                    "Knowledge Base Updated Successfully!"
                                )


                            else:

                                answer = (
                                    "Sorry, I couldn't find an answer."
                                )


                    english_answer = answer


                # ---------------------------------------------
                # Translate Answer
                # ---------------------------------------------

                answer = translate_from_english(
                    english_answer,
                    user_language
                )


                # ---------------------------------------------
                # Save Conversation History
                # ---------------------------------------------

                st.session_state.chat_history.append(
                    (
                        english_question,
                        english_answer
                    )
                )


                # Keep only latest 10 exchanges

                if len(st.session_state.chat_history) > 10:

                    st.session_state.chat_history.pop(0)


                # ---------------------------------------------
                # Display Results
                # ---------------------------------------------

                st.subheader("Detected Language")

                st.success(
                    user_language.upper()
                )


                st.subheader("Detected Sentiment")

                st.success(
                    f"{emoji} {sentiment}"
                )


                st.subheader("Answer")

                st.write(
                    prefix + answer
                )


# ---------------------------------
# Research Statistics
# ---------------------------------

if chat_mode == "Research Statistics":

    st.subheader("Research Statistics")


    categories, years = get_research_statistics()


    st.write(
        "### Top Research Categories"
    )


    cat_names = [
        x[0]
        for x in categories
    ]

    cat_counts = [
        x[1]
        for x in categories
    ]


    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    ax.bar(
        cat_names,
        cat_counts
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    st.pyplot(fig)


    st.write(
        "### Papers by Year"
    )


    fig2, ax2 = plt.subplots(
        figsize=(8, 4)
    )

    ax2.plot(
        years.index,
        years.values,
        marker="o"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    st.pyplot(fig2)