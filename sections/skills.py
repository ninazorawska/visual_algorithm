import streamlit as st
import os
import base64

def show_skills():
    st.markdown('<a name="skills"></a>', unsafe_allow_html=True)
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
    