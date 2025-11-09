import streamlit as st

def show_hero():
    st.markdown("""
        <section class="hero-section">
            <div class="hero-overlay">
                <h1>🌸 Nina Żórawska</h1>
                <p><b>Data Science & AI Student</b> | Maastricht University → NOVA IMS Exchange</p>
                <p>📍 Lisbon, Portugal</p>
                <p>
                    <a href="https://github.com/ninazorawska" target="_blank">💻 GitHub</a> |
                    <a href="https://linkedin.com/in/ninazorawska" target="_blank">🔗 LinkedIn</a> |
                    <a href="mailto:nina.zorawska@gmail.com">📧 Email</a>
                </p>
            </div>
        </section>
                
          <!-- Funny Wave Divider -->
        <div class="wave-divider">
            <svg viewBox="0 0 1440 320" xmlns="http://www.w3.org/2000/svg">
                <path fill="#ffffff" fill-opacity="1"
                    d="M0,224L60,218.7C120,213,240,203,360,181.3C480,160,600,128,720,133.3C840,139,960,181,1080,181.3C1200,181,1320,139,1380,117.3L1440,96L1440,320L1380,320C1320,320,1200,320,1080,320C960,320,840,320,720,320C600,320,480,320,360,320C240,320,120,320,60,320L0,320Z">
                </path>
            </svg>
        </div>
    """, unsafe_allow_html=True)

