import streamlit as st

from agent import run_agent

st.title("AI DevOps Agent")

query = st.chat_input(
    "Enter command"
)

if query:

    st.chat_message("user").write(query)

    result = run_agent(query)

    st.chat_message("assistant").write(result)