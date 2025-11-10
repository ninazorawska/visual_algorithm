import streamlit as st
import os
import base64

def show_projects():
    st.markdown('<a class="anchor" id="projects"></a>', unsafe_allow_html=True)
    st.header("Highlighted Projects")

    # 💅 Minimalist expander styling
    st.markdown("""
    <style>
    div[data-testid="stExpander"] {
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
        margin: 0 !important;
        padding: 0.5rem 0 !important;
    }

    div[data-testid="stExpander"] > div:first-child {
        background: transparent !important;
        color: #b84c8b !important;
        font-weight: 600 !important;
        font-size: 18px !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        transition: color 0.2s ease-in-out;
    }

    div[data-testid="stExpander"] > div:first-child:hover {
        color: #8b2f66 !important;
        text-decoration: underline;
        cursor: pointer;
    }

    div[data-testid="stExpander"] > div:nth-child(2) {
        border: none !important;
        background: transparent !important;
        padding-top: 0.5rem !important;
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
        },

        {
            "title": "⛳ Golf Game AI Simulation </b>",
            "desc": "A physics-driven golf simulation integrating differential equations, numerical solvers, and AI bots for autonomous gameplay.",
            "tech": "Java · LibGDX · AI Optimization (Adam, A*) · Numerical Methods (Euler, RK4)",
            "abstract": (
                "Crazy Putting! Combines physics, numerical analysis, and artificial intelligence to simulate a realistic game of golf. "
                "We explored how differential equations can model a golf ball’s motion across uneven terrains, and how AI "
                "agents can adapt to obstacles and maze-like courses."
            ),
            "description": (
                "By implementing Newtonian physics, incorporating gravitational, normal, and "
                "frictional forces we simulated the movement of the golf ball. We implemented two numerical solvers: **Euler’s method** for computational speed and the **4th-order "
                "Runge-Kutta method (RK4)** for higher accuracy. Apart from the physics layer, we developed three bots: a **rule-based** bot, "
                "an **AI** bot leveraging the Adam optimizer for continuous learning, and an **A*** search-enhanced bot capable of navigating "
                "complex mazes. Each algorithm was tested on terrains of varying slopes and friction coefficients."
            ),
             "experiments": (
                "• Euler vs. RK4: computation time vs. precision trade-off tests.\n"
                "• AI vs. Rule-Based Bots: shot count and completion time across terrains.\n"
                "• A* Algorithm: pathfinding efficiency across maze configurations."
            ),
            "methods": (
                "Numerical modeling (Euler, RK4), Gradient Descent optimization, Adam momentum updates, heuristic pathfinding (A*), "
                "and experimental validation through RMSE and runtime analysis."
            ),
            "results": (
                "The RK4 method achieved the most accurate motion predictions but required more processing time. "
                "The AI bot consistently reached targets in fewer attempts and less time than the rule-based bot. "
                "The A* algorithm demonstrated adaptability to maze complexity, highlighting how heuristic optimization "
                "can enhance decision-making in autonomous systems."
            )

        }

    ]

    for p in projects:
        # --- HEADER + DESCRIPTION ---
        st.markdown(
            f"""
            <div style="text-align:center; font-size:40px;">{p['title']}</div>
            """, unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="text-align:center; font-size:18px; line-height:1.6; margin-top:0.5rem; margin-bottom:0.5rem;">
                {p["desc"]}
            </div>
            """, unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="text-align:center; font-size:18px; line-height:1.6; margin-top:0.5rem; margin-bottom:0.5rem; opacity:0.7;">
                {p["tech"]}
            </div>
            """, unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                text-align:left;
                max-width:1200px;
                margin-left:auto;
                margin-right:auto;
                font-size:25px;
                line-height:1.6em;
                margin-bottom:2.5rem;
            ">
                {p['abstract']}
            </div>
            """, unsafe_allow_html=True
        )

        # --- CONDITIONS ---
        has_poster = "poster_path" in p and os.path.exists(p["poster_path"])
        has_erd = "erd_path" in p and os.path.exists(p["erd_path"])

        # --- EXPANDER SECTION ---
        with st.expander("📖 Read more"):

            if has_poster or has_erd:
                col1, col2 = st.columns([1.2, 1.8], gap="medium")
            else:
                col2 = st.container()  # 👈 single full-width column

            # --- LEFT COLUMN (only if poster/erd exists) ---
            if has_poster or has_erd:
                with col1:
                    if has_poster:
                        st.image(p["poster_path"], caption="Project Poster", use_container_width=True)

                    if has_erd:
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

            # --- RIGHT COLUMN (textual details, or full width if no visuals) ---
            with col2:
                st.markdown("#### 🔍 Description")
                st.markdown(p.get("description", ""), unsafe_allow_html=True)

                if "planning" in p:
                    st.markdown("#### 🗓 Planning")
                    st.markdown(p["planning"], unsafe_allow_html=True)

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
