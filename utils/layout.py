import streamlit as st

def add_sidebar():
    st.sidebar.header("Navigation")
    sections = {
        " About": "#about",
        " Projects": "#projects",
        " Skills": "#skills",
        " Experience": "#experience",
        " Contact": "#contact"
    }
    for label, anchor in sections.items():
        st.sidebar.markdown(f"[{label}]({anchor})", unsafe_allow_html=True)

