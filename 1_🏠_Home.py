import streamlit as st
# from streamlit_extras.app_logo import add_logo



with st.sidebar:
    st.image("./assets/images/MoroccoAI_Logo.png")
    

st.header(":orange[AtlasVoice] Assistant",
          divider="orange")
#st.title(":orange[AtlasVoice] Assistant ")

st.markdown("""
            <style>
            .medium-font {
                font-size:20px !important;
            }
            </style>
            """, unsafe_allow_html=True)

st.markdown(
    '''
    <p class="medium-font"> 
        Welcome to AtlasVoice – where breakthroughs in technology meet the heart of psychotherapy.
        Driven by a vision to revolutionize the way therapists connect with their patients.  
    </p>
   
    <H2> How to use the App </H2> 
    <ol>
        <li class="medium-font">Submit the audio file to the 📜 <kbd>transcript</kbd> section to receive a transcription.</li>
        <li class="medium-font">Explore 🤖 <kbd>Geminibot</kbd> for assistance with any inquiries about your transcript.</li>
    </ol>
    '''
, unsafe_allow_html=True)
