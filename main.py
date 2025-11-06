import streamlit as st
from PIL import Image
import os
import base64

# -----------------------------
# page config
# -----------------------------
st.set_page_config(
    page_title="Nina Żórawska | Portfolio",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# helper: background loader
# -----------------------------
def hero_background(image_path):
    with open(image_path, "rb") as file:
        data = base64.b64encode(file.read()).decode()
    return f"data:image/jpeg;base64,{data}"

bg_image = hero_background("/Users/ninazorawska/Desktop/visual_algorithm/lisbon_bg.JPG")  # 👈 file must be in same folder


# -----------------------------
# custom CSS styling
# -----------------------------
st.markdown("""
<style>
/* Center content container */
.block-container {
    max-width: 1000px;
    margin: 0 auto;
    padding-top: 2rem;
}

/* Header title + subtitle */
.main-title {
    font-size: 38px !important;
    font-weight: 700;
    text-align: center;
    margin-bottom: 0.2em;
}

.subtitle {
    font-size: 22px !important;
    color: #555;
    text-align: center;
    margin-top: 0;
    margin-bottom: 1.5em;
}

/* Center all section headers */
h2, h3 {
    text-align: center !important;
}

/* Make all text slightly larger, left-aligned for readability */
.stMarkdown, .stText, p, li {
    font-size: 20px !important;
    line-height: 1.7em;
    text-align: center;
}

/* Links color */
a {
    color: #b84c8b !important;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}

html {
    scroll-behavior: smooth;
    scroll-padding-top: 100px; /* prevents section titles from hiding under top edge */
}

body {
    scroll-behavior: smooth;
    transition: all 0.5s ease-in-out;
}
                      
/* Offset anchor targets so headers are visible after scroll */
.anchor {
    display: block;
    position: relative;
    top: -90px;   /* 👈 adjust offset to fit your header height */
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# hero section styling
# -----------------------------
st.markdown(f"""
<style>
.hero {{
    height: 100vh;
    width: 100vw; /* full width of screen */
    margin: 0;
    padding: 0;
    position: relative;
    top: 0;
    left: 0;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;

    color: white;
    background:
        linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)),
        url({bg_image});
    background-size: cover; /* fully fills viewport */
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed; /* parallax */
    overflow: hidden;
    z-index: 0;
}}

/* Remove Streamlit default padding and frame */
.block-container {{
    padding: 0 !important;
    margin: 0 auto !important;
    max-width: 100% !important;
}}

section[data-testid="stSidebar"] {{
    z-index: 10;
}}

.hero img {{
    border-radius: 50%;
    width: 220px;
    height: 220px;
    object-fit: cover;
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    margin-bottom: 25px;
}}

.hero h1 {{
    font-size: 46px;
    font-weight: 700;
    margin-bottom: 0.2em;
}}

.hero p {{
    font-size: 20px;
    color: #f0f0f0;
    margin-bottom: 1em;
}}

.hero a {{
    text-decoration: none;
    margin: 0 12px;
    font-size: 18px;
    transition: color 0.3s ease;
    color: white;  /* all white by default */
}}

/* Subtle brand tints on hover */
.hero a[href*="github"]:hover {{
    color: #cccccc; /* light gray */
}}

.hero a[href*="linkedin"]:hover {{
    color: #7ec8f8; /* light blue */
}}

.hero a[href*="mailto"]:hover {{
    color: #ffcce5; /* light pink */
}}

.hero a:hover {{
    text-decoration: underline;
}}

.scroll-down {{
    position: absolute;
    bottom: 25px;
    font-size: 28px;
    color: #fff;
    animation: bounce 1.8s infinite;
}}

@keyframes bounce {{
    0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
    40% {{ transform: translateY(-10px); }}
    60% {{ transform: translateY(-5px); }}
}}
</style>

<div class="hero">
    <h1>🌸 Nina Żórawska</h1>
    <p><b>Data Science & AI Student</b> | Maastricht University → NOVA IMS Exchange</p>
    <p>📍 Lisbon, Portugal</p>
    <p>
        <a href="https://github.com/ninazorawska">💻 GitHub</a> |
        <a href="https://linkedin.com/in/ninazorawska">🔗 LinkedIn</a> |
        <a href="mailto:nina.zorawska@email.com">📧 Email</a>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# -----------------------------
# sidebar navigation
# -----------------------------
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

# -----------------------------
# about section
# -----------------------------
st.markdown('<a class="anchor" id="about"></a>', unsafe_allow_html=True)
st.header("About Me")

col1, col2 = st.columns([1, 2])

with col1:
    about_img_path = "/Users/ninazorawska/Desktop/visual_algorithm/IMG_1133.jpg"  # 👈 use your actual photo path
    if os.path.exists(about_img_path):
        st.image(about_img_path, width=250, caption="🌸 Hi, I'm Nina!", use_container_width=False)
    else:
        st.warning("Profile image not found. Please place 'IMG_1133.jpg' in the same folder.")

with col2:
    st.write("""
    I'm Nina, a **Data Science & AI student at Maastricht University**, currently spending a semester abroad at **NOVA IMS, Lisbon**.  
    I love building real-world AI applications — from **web crawlers** and **chatbots** to **neural networks** and **data visualizations**.  
    Beyond tech, I'm passionate about **running**, **surfing**, and **photography**, which keeps my creative side alive 🌊📸  
    """)

st.markdown("---")


# -----------------------------
# projects section
# -----------------------------
st.markdown('<a class="anchor" id="projects"></a>', unsafe_allow_html=True)
st.header("Highlighted Projects")

projects = [
  
    {
        "title": "🧠 Skin Lesion Classification CNN",
        "desc": "Custom Convolutional Neural Network trained on HAM10000 dataset with data augmentation and metadata integration. Benchmarked against VGG-16.",
        "tech": "TensorFlow · Keras · NumPy · Matplotlib",
        "link": "https://github.com/ninazorawska/skin-lesion-cnn"
    },

]

for p in projects:
    st.subheader(p["title"])
    st.write(p["desc"])
    st.caption(p["tech"])
    st.markdown(f"[🔗 View project]({p['link']})")
    st.markdown("---")

# -----------------------------
# skills
# -----------------------------
st.markdown('<a class="anchor" id="skills"></a>', unsafe_allow_html=True)
st.header("Technical Skills")

st.markdown("""
<div style='text-align:center; font-size:18px;'>
<b>Programming:</b> Python, SQL, JavaScript (basic), HTML/CSS  <br>
<b>AI / ML:</b> TensorFlow, scikit-learn, Keras, Pandas, NumPy  <br>
<b>Data Engineering:</b> Hadoop, Spark  <br>
<b>Visualization:</b> Streamlit, Matplotlib, Seaborn  <br>
<b>Tools:</b> Git, GitLab, Jupyter, VS Code  
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# experience
# -----------------------------
st.markdown('<a class="anchor" id="experience"></a>', unsafe_allow_html=True)
st.header("Experience & Volunteering")

st.markdown("""
<div style='text-align:center; font-size:18px; line-height:1.8em;'>
<b>Web Summit 2025 (Lisbon)</b> — <i>Data Analysis Volunteer</i> <br>
Collected, cleaned, and organized attendee data for post-event analytics. <br><br>

<b>Women in Business Organisation</b> — <i>Event Assistant</i> <br>
Managed guest check-in and conference logistics. <br><br>

<b>University Projects</b> — <i>AI & Software Development</i> <br>
Participated in multiple academic and independent ML & web projects.
</div>
""", unsafe_allow_html=True)

st.markdown("---")
# -----------------------------
# contact
# -----------------------------
st.markdown('<a class="anchor" id="contact"></a>', unsafe_allow_html=True)
st.header("Contact")
st.write("📍 Currently in Lisbon, Portugal")
st.write("📧 [nina.zorawska@email.com](mailto:nina.zorawska@email.com)")
st.write("🔗 [LinkedIn](https://linkedin.com/in/ninazorawska)")
st.write("💻 [GitLab](https://gitlab.com/ninazorawska) | [GitHub](https://github.com/ninazorawska)")
st.write("🏃‍♀️ [Strava](https://www.strava.com/athletes/...) (optional 😉)")
