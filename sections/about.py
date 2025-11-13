import streamlit as st
import base64
import os

def show_about():
    st.markdown('<a name="about"></a>', unsafe_allow_html=True)
    st.header("About Me")
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])

    with col1:
        about_img_path = "assets/IMG_1133.jpg"
        if os.path.exists(about_img_path):
            st.markdown(
                f"""
                <div style="display:flex; justify-content:center; align-items:center; margin-left:60px;">
                    <img src="data:image/jpeg;base64,{base64.b64encode(open(about_img_path, "rb").read()).decode()}" 
                        alt="Profile photo" width="250" style="border-radius:15px; box-shadow:0 4px 20px rgba(0,0,0,0.3);">
                </div>
                <p style="text-align:center; margin-top:10px; </p>
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
                font-size:30px;
                line-height:1.6em;
                max-width:1200px;      /* 👈 limit how wide the text goes */
                margin-left: 40px;    /* 👈 move text slightly left for alignment */
            ">
            Hi! I'm Nina, a <b>Data Science & AI student at Maastricht University</b>, currently spending a semester abroad at <b>NOVA Information Management School, Lisbon</b>.<br><br>
            I love to learn and gain knowledge in different fields, such as machine learning, data science, and technology. I like to challenge myself — that's why I built this website from scratch.<br><br>
            Beyond the up-scaling and the major topic of today, which is AI, I'm passionate about all sorts of sports, music, and photography, which keeps my creative side alive!
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
    st.markdown("---")