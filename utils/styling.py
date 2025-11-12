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
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600&family=Space+Grotesk:wght@500;700&display=swap');


        /* === BASE FONT STYLES === */
        html, body, [data-testid="stAppViewContainer"] {{
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            background-color: #f0f0f0 !important;
            color: #111 !important;
        }}

        /* HEADINGS */
        h1, h2, h3 {{
            font-family: 'Space Grotesk', sans-serif !important;
            letter-spacing: 0.5px;
            color: #111 !important;
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
        }}##

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

        /* PAGE CONTENT BLOCK */
        .block-container {{
            padding-top: 2rem;
        }}

        /* ACCENT TITLES */
        .page-content h2 {{
                text-align: center;
                font-size: 3.2rem;
                color: #ffffff;
                position: relative;
                display: inline-block;
                padding-bottom: 0.4rem;
        }}

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

            /* PARAGRAPHS */
        .page-content p {{
                font-size: 1.1rem;
                line-height: 1.7;
                max-width: 900px;
                margin: 0 auto;
                color: #e8e8e8;
        }}


        /* Hide Streamlit chrome */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        </style>
    """, unsafe_allow_html=True)
