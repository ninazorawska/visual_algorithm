import streamlit as st
import os
import base64


# -----------------------------
# hero component
# -----------------------------
def show_hero():
    st.markdown("""
        <div class="hero">
            <h1>🌸 Nina Żórawska</h1>
            <p><b>Data Science & AI Student</b> | Maastricht University → NOVA IMS Exchange</p>
            <p>📍 Lisbon, Portugal</p>
            <p>
                <a href="https://github.com/ninazorawska" target="_blank">💻 GitHub</a> |
                <a href="https://linkedin.com/in/ninazorawska" target="_blank">🔗 LinkedIn</a> |
                <a href="mailto:nina.zorawska@gmail.com">📧 Email</a>
            </p>
        </div>
    """, unsafe_allow_html=True)
