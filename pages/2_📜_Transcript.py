import streamlit as st
from tempfile import NamedTemporaryFile
import assemblyai as aai

import os



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


# initialize hestory for summary and transcription 

if "transcription" not in st.session_state:
    st.session_state['transcription'] = []

if "summary" not in st.session_state:
    st.session_state['summary'] = []

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
 
    transcript = get_transcript(f)
    os.remove(f)

    with st.expander("See Your Transcript"):
        for utterance in transcript.utterances:
            transcption = f"Speaker {utterance.speaker}: {utterance.text}"
            st.session_state['transcription'].append({"content":transcption})
    
    with st.expander('Summary of the tanscript'):
        prompt = '''Provide a Brief summary of the transcript, Always make sure that the person_A is the doctor and person_B is 
                    the patient.'''
        result = transcript.lemur.task(prompt=prompt)
        summaries = result.response    
        st.session_state["summary"].append({"content": summaries})

# store the Transcript + Summary to the session_state
with st.expander("See Your Transcript"):
    for transc in st.session_state['transcription']:
        st.markdown(transc['content'])

with st.expander('Summary of the tanscript'):
    for sam in st.session_state['summary']:        
        st.markdown(sam['content'])
    

    
