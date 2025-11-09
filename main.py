import os
print("Current working directory:", os.getcwd())
print("File exists:", os.path.exists("assets/lisbon_bg.JPG"))

import streamlit as st
from sections.hero import show_hero
from sections.about import show_about
from sections.projects import show_projects
from sections.skills import show_skills
from sections.experience import show_experience
from sections.contact import show_contact
from utils.styling import apply_custom_css
from utils.layout import add_sidebar

# --- Streamlit page setup ---
st.set_page_config(
    page_title="Nina Żórawska | Portfolio",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Apply custom CSS ---
apply_custom_css()

# --- Sidebar ---
add_sidebar()

# --- Display all sections ---
def main():
    show_hero()
    st.markdown("---")
    show_about()
    st.markdown("---")
    show_projects()
    st.markdown("---")
    show_skills()
    st.markdown("---")
    show_experience()
    st.markdown("---")
    show_contact()

if __name__ == "__main__":
    main()
