import streamlit as st

def add_sidebar():
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


def render_navbar():
    st.markdown("""
        <style>
            .top-navbar {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                background: rgba(255,255,255,0.85);
                backdrop-filter: blur(8px);
                padding: 0.7rem 1rem;
                display: flex;
                justify-content: center;
                gap: 2.2rem;
                z-index: 999999 !important;
                border-bottom: 1px solid rgba(0,0,0,0.1);
                font-family: 'Plus Jakarta Sans', sans-serif;
            }

            .nav-item { position: relative; }

            .nav-link {
                color: #333 !important;
                text-decoration: none;
                font-weight: 500;
                font-size: 1rem;
                padding: 6px 12px;
            }

            .nav-link:hover { color: #ff6fa8 !important; }

            .dropdown {
                position: absolute;
                top: 36px;
                left: 0;
                background: white;
                border-radius: 8px;
                box-shadow: 0 6px 18px rgba(0,0,0,0.15);
                min-width: 160px;
                display: none;
                flex-direction: column;
                padding: 0.5rem 0;
                z-index: 9999999 !important;
            }

            .dropdown a {
                padding: 8px 16px;
                text-decoration: none;
                display: block;
                font-size: 0.95rem;
                color: #333;
                white-space: nowrap;
            }

            .dropdown a:hover {
                background: #ffe2ec;
                color: #ff4f93 !important;
            }

            .nav-item:hover .dropdown { display: flex; }

            .navbar-space { height: 65px; }
        </style>

        <div class="top-navbar">

            <div class="nav-item">
                <a href="#about" class="nav-link">About</a>
            </div>

            <div class="nav-item">
                <a class="nav-link">Projects ▾</a>
                <div class="dropdown">
                    <a href="#projects">All Projects</a>
                    <a href="#project-alien">Alien Grades Prediction</a>
                    <a href="#project-streamlit">Streamlit Portfolio</a>
                    <a href="#project-crawler">Web Crawler</a>
                </div>
            </div>

            <div class="nav-item">
                <a href="#skills" class="nav-link">Skills</a>
            </div>

            <div class="nav-item">
                <a href="#experience" class="nav-link">Experience</a>
            </div>

            <div class="nav-item">
                <a href="#contact" class="nav-link">Contact</a>
            </div>

        </div>

        <div class="navbar-space"></div>
        """, unsafe_allow_html=True)
