import requests
import streamlit as st
#from streamlit.components.v1 import html
#from pathlib import Path

st.set_page_config(page_title="Open AI Chat Assistant", layout="wide")
st.subheader("Open AI Chat Assistant: Life Enhancing with AI!")

css_file = "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def call_chatbot_api(query):
    url = 'https://binqiangliu-fastapi-in-docker.hf.space/api/chat'
    #url='https://hf-aichat-api.onrender.com/api/chat'
    json_data_for_api = {'user_question': query}
    response = requests.post(url, json=json_data_for_api) 
    result = response.json()
    return result['response']
    
user_query = st.text_input("Enter your query here:")
with st.spinner("AI Thinking...Please wait a while to Cheers!"):    
    if user_query !="" and not user_query.strip().isspace() and not user_query == "" and not user_query.strip() == "" and not user_query.isspace():
        response = call_chatbot_api(user_query)
        st.write("AI Response:")
        st.write(response)
        print(response)  # 打印Chatbot的响应
