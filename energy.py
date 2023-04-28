
import streamlit as st

from transformers import pipeline


st.set_page_config(page_title='Energy Consumption Chatbot', page_icon=':zap:')


model = pipeline('text2text-generation', model='GPT2')

st.write('Welcome to the Energy Consumption Chatbot! How can I assist you today?')


def run_chatbot():
    user_input = st.text_input('You: ')

    if user_input:
        chatbot_response = model(user_input)[0]['generated_text']
        st.write('Chatbot: ' + chatbot_response)


run_chatbot()
