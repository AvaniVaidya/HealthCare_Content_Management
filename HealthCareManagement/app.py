import streamlit as st

from extractive_summarizer import ExtractiveSummarizer;
from abstractive_summarizer import AbstractiveSummarizer;

# Streamlit interface
st.title("Healthcare Content Summarization Tool")

summarizerE = ExtractiveSummarizer()
summarizerA = AbstractiveSummarizer()

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

st.session_state.user_input = st.text_area("Enter the healthcare text here:", value=st.session_state.user_input)

if st.button("Summarize"):
    
    # Generate summary
    summary = summarizerE.generate_summary(st.session_state.user_input)
    
    st.write("----------------------------------------------------------------------------------------")
    st.write("Extractive Text Summary:")
    st.write("----------------------------------------------------------------------------------------")
    st.write(summary)

    summary = summarizerA.generate_summary(st.session_state.user_input)
    st.write("----------------------------------------------------------------------------------------")
    st.write("Abstractive Text Summary:")
    st.write("----------------------------------------------------------------------------------------")
    st.write(summary)
