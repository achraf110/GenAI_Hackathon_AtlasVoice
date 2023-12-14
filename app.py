import streamlit as st
from tempfile import NamedTemporaryFile
from openai import OpenAI
import assemblyai as aai
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI() # upload the openAI Api key from .env file, the default variable is "OPENAI_API_KEY"


def get_transcript(f):
    aai.settings.api_key = st.secrets['ASSAMBLY_API_KEY']
    config = aai.TranscriptionConfig(speaker_labels=True)

    transcriber = aai.Transcriber()   
    with st.spinner("Transcribing the File ..."):
        transcript = transcriber.transcribe(f,config)

    return transcript

# setting defaults  
f = None
entered = None

# Header 
st.header('This is the :orange[AtlasVoice], Doctor Helper!', divider="orange")

# -------------
# For Technical users 
# -------------
with st.expander('Technical requirements'):
    st.markdown('''
                ## Technical requirements: 
                ### speech-to-text1  
                - [x] the user must upload a audio/video   
                - [ ] the user must see the results transcription as a result
                ### embedding   
                - [ ] vectorizing text1
                ### chatbot: vect-to-text  
                - [ ] gpt-3.5 turbo must be finetuned with the output of the text1  
                - [ ] adding intuitive questions for the user to try
                ''')
st.divider()

# ----------------------------------------------------------------------------------------------
# store the uploaded file in a temporary file 
f = st.file_uploader("File")
st.audio(f)

if f :
    uploaded_file = f.name.split('.')[-1] # Ex: Eng_test.mp3 ==> split ===> ["Eng_test","mp3"] ==> take the last one 'mp3'
    print(uploaded_file)
    temp_fname = f"tmp.{uploaded_file}"
    with open(temp_fname, "wb") as fl:
        fl.write(f.read())
    f = temp_fname

    entered = st.button('Transcribe')

    if entered: 
        transcript = get_transcript(f)
        os.remove(f)
        with st.expander("See Your Transcript"):
            for utterance in transcript.utterances:
                st.write(f"Speaker {utterance.speaker}: {utterance.text}")
        

        with st.expander('Summary of the tanscript'):
            prompt = '''Provide a Brief summaryr of the transcript, with some key take aways about the personality of the patient,
                        the doctore is alwayse person_A and patient is always patient_B so distinguich between them.
                    '''
            result = transcript.lemur.task(prompt=prompt)

            st.write(result.response)
        

