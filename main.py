import streamlit as st
from PIL import Image

# -----------------------------
# page config
# -----------------------------
st.set_page_config(
    page_title="Nina Żórawska | Portfolio",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"  # starts with sidebar hidden
)

# -----------------------------
# header section (name + photo)
# -----------------------------
col1, col2 = st.columns([1, 3], vertical_alignment="center")

with col1:
    image = Image.open("nina.jpg")  # put nina.jpg in same folder
    st.image(image, width=180, use_container_width=False)

with col2:
    st.title("🌸 Nina Żórawska")
    st.markdown("""
    **Data Science & AI Student | Maastricht University → NOVA IMS Exchange**  
    Passionate about **AI, ML, and Software Engineering**
    """)
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
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to:", ["🏠 About", "💻 Projects", "🧠 Skills", "🎓 Experience", "📫 Contact"])

# -----------------------------
# about section
# -----------------------------
if page == "🏠 About":
    st.header("About Me")
    st.write("""
    I'm Nina, a **Data Science & AI student at Maastricht University**, currently spending a semester abroad at **NOVA IMS, Lisbon**.  
    I love building real-world AI applications — from web crawlers and chatbots to neural networks and data visualizations.  
    Beyond tech, I'm passionate about **running, surfing, and photography**, which keeps my creative side alive 🌊📸
    """)

# -----------------------------
# projects section
# -----------------------------
elif page == "💻 Projects":
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
elif page == "🧠 Skills":
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
elif page == "🎓 Experience":
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
else:
    st.header("Contact")
    st.write("📍 Currently in Lisbon, Portugal")
    st.write("📧 [nina.zorawska@email.com](mailto:nina.zorawska@email.com)")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/ninazorawska)")
    st.write("💻 [GitLab](https://gitlab.com/ninazorawska) | [GitHub](https://github.com/ninazorawska)")
    st.write("🏃‍♀️ [Strava](https://www.strava.com/athletes/...) (optional 😉)")
