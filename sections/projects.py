import streamlit as st
import os
import base64

def show_projects():
    st.markdown('<a class="anchor" id="projects"></a>', unsafe_allow_html=True)
    st.header("Highlighted Projects")

    st.markdown("""
    <style>
    /* --- Expander (Read More) Custom Styling --- */
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.6) !important; /* soft transparent background */
        border: none !important;        /* removes the grey frame */
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);  /* subtle floating effect */
        border-radius: 16px !important; /* smooth rounded corners */
        padding: 1.2rem 1rem 1rem 1rem !important;
        margin-top: 1rem;
        margin-bottom: 2rem;
        transition: all 0.3s ease-in-out;
    }

    /* Hover glow for a tactile feel */
    div[data-testid="stExpander"]:hover {
        box-shadow: 0 6px 22px rgba(0, 0, 0, 0.12);
        background-color: rgba(255, 255, 255, 0.75);
    }

    /* Header styling */
    div[data-testid="stExpander"] > div:first-child {
        background-color: transparent !important;
        border: none !important;
        color: #b84c8b !important; /* your accent pink */
        font-weight: 600 !important;
        font-size: 20px !important;
    }

    /* Remove default divider line */
    div[data-testid="stExpander"] > div:first-child::after {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
    projects = [
        {
            "title": "🧠 Skin Lesion Classification CNN</b>",
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
                "available through the Harvard Dataverse. It contains 10,015 dermatoscopic images covering seven skin disease classes. "
                "<br><br><b>Model validation</b> included train/validation/test splits, cross-validation, and performance metrics."
            ),
            "implementation": "Implemented in TensorFlow/Keras with ReLU, dropout, and transfer learning via VGG-16.",
            "experiments": "Compared architectures, tuned hyperparameters, and addressed class imbalance with SMOTE.",
            "methods": "Evaluated using F1-score, ROC, accuracy, recall, and confusion matrix visualizations.",
            "results": "Achieved macro-F1 score of 0.84, outperforming VGG-16 in class-balance robustness.",
            "poster_path": "assets/KEN10_Poster.jpg",
        },

        {
            "title": "🍕 Pizza Restaurant Ordering System</b>",
            "desc": "Developed a GUI-based ordering and delivery management system in Python integrated with a relational SQL database.",
            "tech": "Tkinter · SQL · Python · ER Diagrams",
            "abstract": (
                "In response to EU regulations banning centralized take-away services, each restaurant must now operate "
                "its own independent ordering system. This project implements a modular pizza ordering and delivery platform "
                "featuring menu management, order processing, delivery assignment, and earnings reporting."
            ),
            "description": (
                "The project required implementing all requested functionality using an appropriate database system. "
                "We provided a simple GUI (Tkinter) to interact with a relational database (MySQL), storing data such as customers, "
                "orders, pizzas, and deliveries. Functionality included placing and managing orders, applying discounts, and "
                "tracking delivery statuses."
            ),
            "planning": (
                "Week 1–2: ERD and schema design. <br>"
                "Week 3: Database implementation and GUI integration. <br>"
                "Week 4: Earnings report and testing. <br>"
                "Week 5–6: Documentation, debugging, and submission."
            ),
            "poster_path": "/Users/ninazorawska/Desktop/visual_algorithm-2/pizza_project_poster.jpg",
            "erd_path": "assets/ERD.jpg",  # 👈 add your ERD image here
            "video_link": "https://drive.google.com/file/d/13CNlT7Wx0IbaPad4eJ91hmXZ4B_jOefx/view?usp=sharing",
        }
    ]




    for p in projects:
        st.markdown(f"### {p['title']}", unsafe_allow_html=True)
        st.write(p["desc"])
        st.caption(p["tech"])

        st.markdown("### 📘 Abstract")
        st.markdown(
            f"""
            <div style="
                text-align: left;
                max-width: 1000px;
                margin-left: auto;
                margin-right: auto;
                font-size: 25px;
                line-height: 1.6em;
            ">
                {p['abstract']}
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.expander("📖 Read more"):
            col1, col2 = st.columns([1.2, 1.8], gap="medium")  # 👈 Left: images | Right: text

            # --- LEFT COLUMN: Poster + ERD + Video link ---
            with col1:
                # Project Poster
                if "poster_path" in p and os.path.exists(p["poster_path"]):
                    st.image(
                        p["poster_path"],
                        caption="Project Poster",
                        use_container_width=True
                    )

                # ER Diagram (a bit smaller, below poster)
                if "erd_path" in p and os.path.exists(p["erd_path"]):
                    st.markdown(
                        f"""
                        <div style="text-align:center; margin-top:15px;">
                            <img src="data:image/jpeg;base64,{base64.b64encode(open(p['erd_path'], 'rb').read()).decode()}"
                                alt="ER Diagram"
                                style="max-width:1000px; border-radius:12px; box-shadow:0 2px 10px rgba(0,0,0,0.25);">
                            <p style="font-size:14px; color:gray;">Entity-Relationship Diagram</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


            # --- RIGHT COLUMN: Textual details ---
            with col2:
                st.markdown("#### 🔍 Description")
                st.markdown(p.get("description", ""), unsafe_allow_html=True)

                if "planning" in p:
                    st.markdown("#### 🗓 Planning")
                    st.markdown(p["planning"], unsafe_allow_html=True)

                # Video Link
                if "video_link" in p:
                    st.markdown(
                        f"""
                        <div style="text-align:center; margin-top:10px;">
                            <a href="{p['video_link']}" target="_blank" 
                            style="font-size:17px; color:#b84c8b; text-decoration:none; font-weight:600;">
                            🎬 Watch Project Presentation
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                if "getting_started" in p:
                    st.markdown("#### 🧩 Dataset & Validation")
                    st.markdown(p["getting_started"], unsafe_allow_html=True)

                if "implementation" in p:
                    st.markdown("#### ⚙️ Implementation")
                    st.write(p["implementation"])

                if "experiments" in p:
                    st.markdown("#### 🧪 Experiments")
                    st.write(p["experiments"])

                if "methods" in p:
                    st.markdown("#### 📚 Methods")
                    st.write(p["methods"])

                if "results" in p:
                    st.markdown("#### 📈 Results")
                    st.write(p["results"])




        st.markdown("---")