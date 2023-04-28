# Import libraries
import streamlit as st
import torch
from transformers import pipeline

# Set page title
st.set_page_config(page_title='Energy Consumption Chatbot', page_icon=':zap:')

# Load chatbot model
model = pipeline('text2text-generation', model='GPT2')

# Set welcome message
st.write('Welcome to the Energy Consumption Chatbot! How can I assist you today?')

# Chatbot function
def run_chatbot():
    user_input = st.text_input('You: ')

    if user_input:
        chatbot_response = model(user_input)[0]['generated_text']
        st.write('Chatbot: ' + chatbot_response)

# Run chatbot
run_chatbot()
