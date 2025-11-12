import os
import streamlit as st
from sections.hero import show_hero
from sections.about import show_about
from sections.projects import show_projects
from sections.skills import show_skills
from sections.experience import show_experience
from sections.contact import show_contact
from utils.styling import apply_custom_css
from utils.layout import add_sidebar

st.set_page_config(
    page_title="🌸 Nina Żórawska | Portfolio",
    layout="wide",
    page_icon="🌸",
    initial_sidebar_state="collapsed"
)

from utils.styling import apply_custom_css
from sections.hero import show_hero
add_sidebar()
apply_custom_css()
# show_hero()

# --- Add spacing between hero and about ---
# st.markdown("<br><br><br>", unsafe_allow_html=True)
# --- Display all sections ---
def main():
    show_about()
    st.markdown("<br>", unsafe_allow_html=True)
    show_projects()
    st.markdown("---")
    show_skills()
    st.markdown("---")
    show_experience()
    st.markdown("---")
    show_contact()

if __name__ == "__main__":
    main()
