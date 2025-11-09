import os
import base64
import streamlit as st

def hero_background(image_path):
    with open(image_path, "rb") as file:
        data = base64.b64encode(file.read()).decode()
    return f"data:image/jpeg;base64,{data}"

def apply_custom_css():
    """Full-screen hero background + white content below"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, ".."))
    bg_path = os.path.join(project_root, "assets", "lisbon_bg.JPG")
    bg_image = hero_background(bg_path)

    st.markdown(f"""
        <style>
        /* === IMPORT GOOGLE FONTS === */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Poppins:wght@600;700&display=swap');

        /* === BASE FONT STYLES === */
        html, body, [data-testid="stAppViewContainer"], .main {{
            font-family: 'Inter', sans-serif !important;
        }}

        h1, h2, h3, .hero h1, .page-content h2 {{
            font-family: 'Poppins', sans-serif !important;
            letter-spacing: 0.5px;
        }}

        /* ---------- HERO SECTION (full screen) ---------- */
        .hero-section {{
            position: relative;
            height: 100vh;
            width: 100%;
            background: url("{bg_image}") no-repeat center center fixed;
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            text-align: center;
        }}

        .hero-overlay {{
            background: rgba(0, 0, 0, 0.45);
            padding: 5rem 2rem;
            border-radius: 20px;
            backdrop-filter: blur(4px);
            box-shadow: 0 4px 30px rgba(0,0,0,0.4);
        }}

        .hero-overlay h1 {{
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }}

        .hero-overlay p {{
            font-size: 1.2rem;
            margin: 0.3rem 0;
        }}

        .hero-overlay a {{
            color: #ffb6c1;
            text-decoration: none;
            font-weight: 500;
        }}

        .hero-overlay a:hover {{
            text-decoration: underline;
        }}

        /* ---------- PAGE CONTENT BELOW ---------- */
        .page-content {{
            background-color: white;
            color: #333;
            padding: 8rem 2rem 10rem 2rem;
            min-height: 100vh;
        }}

        .page-content h2 {{
            text-align: center;
            margin-bottom: 2.5rem;
            font-size: 4rem;               /* 👈 beautiful large titles */
            font-weight: 700;
            letter-spacing: 1px;
            color: #111;
            position: relative;
            display: inline-block;
            padding-bottom: 0.5rem;
            font-family: 'Poppins', sans-serif;
        }}

        /* underline accent */
        .page-content h2::after {{
            content: "";
            position: absolute;
            left: 50%;
            bottom: 0;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background-color: #ffb6c1;
            border-radius: 2px;
        }}

        .page-content p {{
            font-size: 1.1rem;
            line-height: 1.7;
            max-width: 900px;
            margin: 0 auto;
            text-align: justify;
        }}

        /* ---------- FUNNY DIVIDER ---------- */
        .wave-divider {{
            line-height: 0;
            overflow: hidden;
        }}

        .wave-divider svg {{
            display: block;
            width: 100%;
            height: 100px;
        }}

        /* Hide Streamlit chrome */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        </style>
    """, unsafe_allow_html=True)
