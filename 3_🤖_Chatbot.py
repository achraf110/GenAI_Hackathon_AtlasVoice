import streamlit as st 
from openai import OpenAI
import numpy as np
import google.generativeai as gemi

# client = OpenAI(api_key=st.secrets['OPENAI_API_KEY']) # upload the openAI Api key from .env file, the default variable is "OPENAI_API_KEY"


# openai model
if "openai_model" not in st.session_state:
    st.session_state['openai_model'] = 'gpt-3.5-turbo'

# initializing a chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# for iterration in the chat history then display it 
# why ?
# why not !
# no bcs every time we enter an input all the session get's empty 
# so we store every little chat in the chat history 
# loop through it and display it 
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("Say something"): # asseign the user input to prompt var 
    with st.chat_message('user'): # user for the avatar
        st.markdown(prompt)
    st.session_state.messages.append({"role":'user',"content": prompt})
        

    with st.chat_message('assistant'):
        message_place = st.empty()
        full_response = ""

        for response in client.chat.completions.create(
            model= st.session_state['openai_model'],
            messages= [
                {"role":m["role"], "content":m['content']}
                for m in st.session_state.messages
            ],
            stream=True
        ):
            full_response += (response.choices[0].delta.content or "")
            message_place.markdown(full_response + " ")
        message_place.markdown(full_response)

    st.session_state.messages.append({"role":'assistant',"content":full_response})