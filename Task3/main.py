import streamlit as st
from langchain_helper import (
    create_vector_db,
    get_qa_chain,
    search_web,
    update_knowledge_base,
    analyze_image,
    get_saved_answer
)

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Customer Service Chatbot",
    page_icon="🤖"
)

st.title("🤖AI Knowledge Chatbot")
st.write("""
This chatbot can answer questions from:

• Customer Service Dataset

• Medical Dataset (MedQuAD)

• Uploaded Images

If information is unavailable, it searches the web and updates its knowledge base automatically.
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
question = st.text_input("Ask your question")

if question:
  if uploaded_image:

        with st.spinner("Analyzing Image..."):

            answer = analyze_image(
                uploaded_image,
                question
            )

        st.subheader("Image Analysis")

        st.write(answer)

        st.stop()
  with st.spinner("Searching..."):

     chain = get_qa_chain()

     response = chain.invoke({"input": question})

     answer = response["answer"].strip()
    
    

    # ---------------------------------
    # If answer not found in FAISS
    # ---------------------------------
     if "don't know" in answer.lower():
        saved_answer = get_saved_answer(question)
        if saved_answer:
            answer = saved_answer
            st.success("Answer found in knowledge updates")
        else:
            st.info("Searching the web...")
            web_answer = search_web(question)
            if web_answer:
            # Save in knowledge_updates.csv
                update_knowledge_base(question, web_answer)
                answer = web_answer
                st.success("Knowledge Base Updated Successfully!")
            else:
                answer = "Sorry, I couldn't find an answer."

    # ---------------------------------
    # Display Final Answer
    # ---------------------------------
     st.subheader("Answer")

     st.write(answer)