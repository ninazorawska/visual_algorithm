import streamlit as st
import base64
import os

def hero_background(image_path):
    with open(image_path, "rb") as file:
        data = base64.b64encode(file.read()).decode()
    return f"data:image/jpeg;base64,{data}"

def apply_custom_css():
    bg_path = os.path.join("assets", "lisbon_bg.JPG")
    bg_image = hero_background(bg_path)

    st.markdown(f"""
    <style>
    html, body, [data-testid="stAppViewContainer"] {{
        overflow-x: hidden !important;
        width: 100% !important;
        max-width: 100% !important;
    }}
    body {{
        font-family: 'Segoe UI', sans-serif;
        scroll-behavior: smooth;
    }}
    .hero {{
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background:
            linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)),
            url({bg_image});
        background-size: cover;
        background-position: center;
        color: white;
        text-align: center;
    }}
    </style>
    """, unsafe_allow_html=True)
