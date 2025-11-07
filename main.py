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
# custom CSS styling (unified)
# -----------------------------
st.markdown("""
<style>

/* ========== GLOBAL LAYOUT FIXES ========== */

/* Prevent horizontal scrolling globally */
html, body, [data-testid="stAppViewContainer"], [data-testid="stVerticalBlock"] {
    overflow-x: hidden !important;
    width: 100% !important;
    max-width: 100% !important;
}

/* Smooth scrolling */
html {
    scroll-behavior: smooth;
    scroll-padding-top: 100px; /* prevents section titles from hiding under top edge */
}
body {
    scroll-behavior: smooth;
    transition: all 0.5s ease-in-out;
}

/* Sidebar animation fix */
section[data-testid="stSidebar"] {
    overflow-x: hidden !important;
    transition: all 0.3s ease-in-out !important;
}

/* Block container stays centered and responsive */
.block-container {
    max-width: 100%;
    overflow-x: hidden !important;
    padding: 0 2rem !important;
    margin: 0 auto !important;
    box-sizing: border-box !important;
}


/* ========== TYPOGRAPHY & TEXT ========== */

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

/* Make all text slightly larger, left-aligned for readability */
.stMarkdown, .stText, p, li {
    font-size: 20px !important;
    line-height: 1.7em;
    text-align: center;
}

/* Center all section headers */
h2, h3 {
    text-align: center !important;
}

/* Link color and hover behavior */
a {
    color: #b84c8b !important;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}

/* Anchor offset (so sections aren’t hidden under nav bar) */
.anchor {
    display: block;
    position: relative;
    top: -90px;
    visibility: hidden;
}


/* ========== EXPANDER POLISH ========== */

div[data-testid="stExpander"] {
    background-color: rgba(255,255,255,0.9);
    border-radius: 15px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    padding: 1rem;
}

[data-testid="column"] img {
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.25);
}


/* ========== HERO SECTION ========== */

.hero {
    height: 100vh;
    width: 100vw;
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
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    overflow: hidden;
    z-index: 0;
}

.hero img {
    border-radius: 50%;
    width: 220px;
    height: 220px;
    object-fit: cover;
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 46px;
    font-weight: 700;
    margin-bottom: 0.2em;
}

.hero p {
    font-size: 20px;
    color: #f0f0f0;
    margin-bottom: 1em;
}

.hero a {
    text-decoration: none;
    margin: 0 12px;
    font-size: 18px;
    transition: color 0.3s ease;
    color: white;
}

.hero a[href*="github"]:hover {
    color: #cccccc;
}
.hero a[href*="linkedin"]:hover {
    color: #7ec8f8;
}
.hero a[href*="mailto"]:hover {
    color: #ffcce5;
}
.hero a:hover {
    text-decoration: underline;
}

/* Animated scroll arrow */
.scroll-down {
    position: absolute;
    bottom: 25px;
    font-size: 28px;
    color: #fff;
    animation: bounce 1.8s infinite;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-10px); }
    60% { transform: translateY(-5px); }
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
    about_img_path = "/Users/ninazorawska/Desktop/visual_algorithm/IMG_1133.jpg"
    if os.path.exists(about_img_path):
        st.markdown(
            f"""
            <div style="display:flex; justify-content:center; align-items:center; margin-left:40px;">
                <img src="data:image/jpeg;base64,{base64.b64encode(open(about_img_path, "rb").read()).decode()}" 
                     alt="Profile photo" width="250" style="border-radius:15px; box-shadow:0 4px 20px rgba(0,0,0,0.3);">
            </div>
            <p style="text-align:center; margin-top:10px;">🌸 Hi, I'm Nina!</p>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Profile image not found. Please place 'IMG_1133.jpg' in the same folder.")
with col2:
    st.markdown(
        """
        <div style="
            text-align:left;
            font-size:22px;
            line-height:1.6em;
            max-width:900px;      /* 👈 limit how wide the text goes */
            margin-left: 40px;    /* 👈 move text slightly left for alignment */
        ">
        Hi! I'm Nina, a <b>Data Science & AI student at Maastricht University</b>, currently spending a semester abroad at <b>NOVA Information Management School, Lisbon</b>.<br><br>
        I love to learn and gain knowledge in different fields, such as machine learning, data science, and technology. I like to challenge myself — that's why I built this website from scratch 🙂.<br><br>
        Beyond the up-scaling and the major topic of today, which is AI, I'm passionate about all sorts of sports, music, and photography, which keeps my creative side alive!
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("---")


# -----------------------------
# projects section
# -----------------------------
st.markdown('<a class="anchor" id="projects"></a>', unsafe_allow_html=True)
st.header("Highlighted Projects")

projects = [
    {
        "title": "Skin Lesion Classification CNN</b>",
        "desc": "Custom Convolutional Neural Network trained on the HAM10000 dataset with data augmentation and metadata integration. Benchmarked against VGG-16.",
        "tech": "TensorFlow · Keras · NumPy · Matplotlib",
        "abstract": (
            "Skin cancer is one of the most common types of cancer worldwide, ranking 17th for melanoma (MSC) "
            "and 5th for non-melanoma (NMSC). Although its prevalence differs across continents, the global "
            "rate is steadily increasing. MSC is particularly dangerous due to its high metastatic potential; "
            "however, early detection can reduce mortality by up to 90%. This project focuses on the automated "
            "classification of dermoscopic images from the HAM10000 dataset using a custom CNN architecture "
            "leveraging transfer learning and advanced feature extraction techniques."
        ),
        "description": (
            "The core goal of this project was to develop an automated classifier for dermoscopic images from "
            "the HAM10000 dataset. The research aimed to answer the following questions: <br><br>"
            "• Which CNN architecture yields the best accuracy — a custom model or a transfer-learning-based VGG-16?<br>"
            "• How does incorporating patient-specific metadata influence model performance?<br>"
            "• What are the optimal oversampling and undersampling ratios for class imbalance?<br>"
            "• Which hyperparameters (learning rate, hidden layers) most affect CNN performance?"
        ),
        "getting_started": (
            "The HAM10000 (Human Against Machine with 10000 training images) dataset (Tschandl, 2018) is publicly "
            "available through the Harvard Dataverse. It contains 10,015 dermatoscopic images covering seven skin disease classes: "
            "Actinic keratoses (akiec), Basal cell carcinoma (bcc), Benign keratosis-like lesions (bkl), Dermatofibroma (df), "
            "Melanoma (mel), Nevus (nv), and Vascular lesions (vasc). The dataset is diverse and well-annotated, making it ideal "
            "for training deep learning models. Preprocessing included normalization (scaling pixel values) and resizing images to "
            "128×128 pixels for input consistency. <br><br>"
            "<b>Model validation</b> was a crucial step to ensure robustness. Validation procedures included "
            "<i>Train-Validation-Test splits</i>, <i>cross-validation</i>, and comprehensive <i>performance metrics</i>. "
            "An 80% training / 20% validation split was used to evaluate performance on unseen data, while the test set provided "
            "by HAM10000 was used for final evaluation."
        ),
        "implementation": (
            "The CNN was implemented using TensorFlow and Keras. The architecture featured multiple convolutional "
            "and pooling layers for hierarchical feature extraction, followed by fully connected layers with dropout "
            "regularization. Transfer learning was integrated via a pretrained VGG-16 backbone for comparison. "
            "The model employed ReLU activation, softmax output, and Adam optimizer. Data augmentation (rotation, "
            "horizontal flip, brightness adjustment) helped mitigate overfitting."
        ),
        "experiments": (
            "A series of experiments tested different architectures (custom CNN vs VGG-16), learning rates, batch sizes, "
            "and class-balancing techniques. SMOTE and undersampling were applied to address the dataset’s imbalance. "
            "Cross-validation assessed consistency across folds, and early stopping prevented overfitting."
        ),
        "methods": (
            "The workflow included preprocessing, model building, training with early stopping, and evaluation using "
            "accuracy, precision, recall, F1-score, and confusion matrix analysis. Visualizations (ROC curves, loss/accuracy plots) "
            "helped monitor training dynamics."
        ),
        "results": (
            "The custom CNN achieved a macro-F1 score of 0.84 and outperformed VGG-16 in terms of class-balance robustness. "
            "Adding metadata improved recall for rare lesion types by approximately 6%. The final model demonstrated "
            "strong generalization on the unseen HAM10000 test set, confirming its potential for real-world diagnostic support."
        ),
        "poster_path": "/Users/ninazorawska/Desktop/visual_algorithm-1/KEN10_Poster.jpg",
    }
]



for p in projects:
    st.markdown(p["title"], unsafe_allow_html=True)
    st.write(p["desc"])
    st.caption(p["tech"])

    st.markdown("### 📘 Abstract")
    st.markdown(
        f"""
        <div style="
            text-align: left;
            max-width: 900px;     /* 👈 limit how far right it goes */
            margin-left: auto;    /* 👈 center horizontally */
            margin-right: auto;   /* 👈 center horizontally */
            font-size: 18px;
            line-height: 1.6em;
        ">
            {p['abstract']}
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.expander("📖 Read more"):
        col1, col2 = st.columns([1, 1.5], gap="medium")

        with col1:
            if "poster_path" in p and os.path.exists(p["poster_path"]):
                st.image(
                    p["poster_path"],
                    caption="Project Poster – Skin Lesion Classification CNN",
                    use_container_width=True
                )
            else:
                st.markdown("*(Poster unavailable — file not found.)*")

        with col2:
            st.markdown("#### 🔍 Research Focus & Description")
            st.markdown(p["description"], unsafe_allow_html=True)

            st.markdown("#### 🧩 Dataset & Validation")
            st.markdown(p["getting_started"], unsafe_allow_html=True)

            st.markdown("#### ⚙️ Implementation")
            st.write(p["implementation"])

            st.markdown("#### 🧪 Experiments")
            st.write(p["experiments"])

            st.markdown("#### 📚 Methods")
            st.write(p["methods"])

            st.markdown("#### 📈 Results")
            st.write(p["results"])

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
