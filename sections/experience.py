import streamlit as st

def show_experience():
    st.markdown('<a name="experience"></a>', unsafe_allow_html=True)
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