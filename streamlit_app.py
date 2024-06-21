import streamlit as st
from response_agent.manager import Manager

manager = Manager()

st.title("Response Agent Dashboard")

request_type = st.selectbox("Select Request Type", ["reviews_intelligence", "estatistica", "storytelling"])
data_input = st.text_area("Input Data")

if st.button("Process"):
    result = manager.handle_request(request_type, data_input)
    st.write(result)
