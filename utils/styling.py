import streamlit as st
import os
import base64

def hero_background(image_path):
    """Encode image to base64 for use in CSS."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"🚨 Background image not found at: {image_path}")
    with open(image_path, "rb") as file:
        data = base64.b64encode(file.read()).decode()
    return f"data:image/jpeg;base64,{data}"

def apply_custom_css():
    """Inject global CSS and background image."""
    # --- Get absolute path dynamically ---
    current_dir = os.path.dirname(os.path.abspath(__file__))         # /visual_algorithm/utils
    project_root = os.path.abspath(os.path.join(current_dir, ".."))  # /visual_algorithm
    bg_path = os.path.join(project_root, "assets", "lisbon_bg.JPG")  # /visual_algorithm/assets/lisbon_bg.JPG

    print(f"🔍 Looking for background at: {bg_path}")
    print(f"📁 Exists: {os.path.exists(bg_path)}")

    bg_image = hero_background(bg_path)

    st.markdown(f"""
        <style>
        body {{
            background-image: url("{bg_image}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
        }}
        .hero {{
            text-align: center;
            padding: 4rem 1rem;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 20px;
            max-width: 700px;
            margin: 5rem auto;
            box-shadow: 0 4px 30px rgba(0,0,0,0.3);
        }}
        .hero h1 {{
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }}
        .hero p {{
            font-size: 1.2rem;
            margin: 0.3rem 0;
        }}
        .hero a {{
            color: #ffb6c1;
            text-decoration: none;
            font-weight: 500;
        }}
        .hero a:hover {{
            text-decoration: underline;
        }}
        </style>
    """, unsafe_allow_html=True)
