import streamlit as st
from langchain_helper import (
    create_vector_db,
    get_qa_chain,
    search_web,
    update_knowledge_base,
)

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Customer Service Chatbot",
    page_icon="🤖"
)

st.title("🤖 CUSTOMER SERVICE CHATBOT")

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
  with st.spinner("Searching..."):

     chain = get_qa_chain()

     response = chain.invoke({"input": question})

     answer = response["answer"].strip()
    
    

    # ---------------------------------
    # If answer not found in FAISS
    # ---------------------------------
     if "don't know" in answer.lower():

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