import streamlit as st
from PIL import Image
import os

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
# custom CSS styling
# -----------------------------
st.markdown("""
<style>
    /* Smaller name and larger text overall */
    .main-title {
        font-size: 40px !important;
        font-weight: 700;
        margin-bottom: 0.2em;
    }
    .subtitle {
        font-size: 20px !important;
        color: #555;
        margin-top: 0;
        margin-bottom: 1em;
    }

    /* Larger default text everywhere */
    .stMarkdown, .stText, p, li {
        font-size: 17px !important;
        line-height: 1.6em;
    }

    /* Reduce Streamlit default padding */
    .block-container {
        padding-top: 1rem;
    }

    /* Smooth scrolling between anchor links */
    html {
        scroll-behavior: smooth;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# header section (name + photo)
# -----------------------------
col1, col2 = st.columns([1, 3], vertical_alignment="center")

with col1:
    img_path = "IMG_1133.jpg"
    if os.path.exists(img_path):
        image = Image.open(img_path)
        st.image(image, width=180)
    else:
        st.warning("Profile photo not found — please place 'IMG_1133.jpg' in the project folder.")

with col2:
    st.markdown('<h1 class="main-title">🌸 Nina Żórawska</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle"><b>Data Science & AI Student</b> | Maastricht University → NOVA IMS Exchange</p>', unsafe_allow_html=True)
    st.write("📍 Lisbon, Portugal")
    st.markdown(
        "[💻 GitHub](https://github.com/ninazorawska) | "
        "[🔗 LinkedIn](https://linkedin.com/in/ninazorawska) | "
        "[📧 Email](mailto:nina.zorawska@email.com)"
    )

st.markdown("---")

# -----------------------------
# sidebar navigation
# -----------------------------
st.sidebar.header("Navigation")
sections = {
    "🏠 About": "#about",
    "💻 Projects": "#projects",
    "🧠 Skills": "#skills",
    "🎓 Experience": "#experience",
    "📫 Contact": "#contact"
}
for label, anchor in sections.items():
    st.sidebar.markdown(f"[{label}]({anchor})", unsafe_allow_html=True)

# -----------------------------
# about section
# -----------------------------
st.markdown('<a name="about"></a>', unsafe_allow_html=True)
st.header("About Me")
st.write("""
I'm Nina, a **Data Science & AI student at Maastricht University**, currently spending a semester abroad at **NOVA IMS, Lisbon**.  
I love building real-world AI applications — from web crawlers and chatbots to neural networks and data visualizations.  
Beyond tech, I'm passionate about **running, surfing, and photography**, which keeps my creative side alive 🌊📸
""")

# -----------------------------
# projects section
# -----------------------------
st.markdown('<a name="projects"></a>', unsafe_allow_html=True)
st.header("Highlighted Projects")

projects = [
    {
        "title": "🕸️ FastAPI + Playwright Web Crawler",
        "desc": "Built a multi-threaded crawler saving websites as PDFs using Playwright, Redis & BeautifulSoup. Handles document detection and tree-structured saving.",
        "tech": "FastAPI · Redis · Playwright · BeautifulSoup · PDFKit",
        "link": "https://gitlab.com/ninazorawska/webcrawler"
    },
    {
        "title": "🧠 Skin Lesion Classification CNN",
        "desc": "Custom Convolutional Neural Network trained on HAM10000 dataset with data augmentation and metadata integration. Benchmarked against VGG-16.",
        "tech": "TensorFlow · Keras · NumPy · Matplotlib",
        "link": "https://github.com/ninazorawska/skin-lesion-cnn"
    },
    {
        "title": "💬 Langfuse-Traced Streamlit Chat App",
        "desc": "Built an interactive chat app integrated with Gemini API and Langfuse tracing tools, including custom calculator and bill-splitting tools.",
        "tech": "Streamlit · Gemini API · Langfuse",
        "link": "https://github.com/ninazorawska/streamlit-chat-app"
    }
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
st.markdown('<a name="skills"></a>', unsafe_allow_html=True)
st.header("Technical Skills")
st.write("""
- **Programming:** Python, SQL, JavaScript (basic), HTML/CSS  
- **AI / ML:** TensorFlow, scikit-learn, Keras, Pandas, NumPy  
- **Data Engineering:** FastAPI, Redis, Hadoop, Spark  
- **Visualization:** Streamlit, Matplotlib, Seaborn, Plotly  
- **Tools:** Git, GitLab, Jupyter, VS Code, Docker
""")

# -----------------------------
# experience
# -----------------------------
st.markdown('<a name="experience"></a>', unsafe_allow_html=True)
st.header("Experience & Volunteering")
st.write("""
- **Web Summit 2025 (Lisbon)** — *Data Analysis Volunteer*  
  Collected, cleaned, and organized attendee data for post-event analytics.

- **Women in Business Organisation** — *Event Assistant*  
  Managed guest check-in and conference logistics.

- **University Projects** — *AI & Software Development*  
  Participated in multiple academic and independent ML & web projects.
""")

# -----------------------------
# contact
# -----------------------------
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
st.header("Contact")
st.write("📍 Currently in Lisbon, Portugal")
st.write("📧 [nina.zorawska@email.com](mailto:nina.zorawska@email.com)")
st.write("🔗 [LinkedIn](https://linkedin.com/in/ninazorawska)")
st.write("💻 [GitLab](https://gitlab.com/ninazorawska) | [GitHub](https://github.com/ninazorawska)")
st.write("🏃‍♀️ [Strava](https://www.strava.com/athletes/...) (optional 😉)")
