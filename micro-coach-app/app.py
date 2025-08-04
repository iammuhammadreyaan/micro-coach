# app.py

import streamlit as st
from coach_engine import get_advice

# Set page configuration
st.set_page_config(page_title="🧠 Micro-Coach", layout="centered")

# App title and subtitle
st.markdown("<h1 style='text-align: center;'>🧠 Micro-Coach</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>An AI-powered mini life coach for instant clarity and motivation.</p>", unsafe_allow_html=True)

# Divider
st.markdown("---")

# Button to get advice
if st.button("💡 Get Advice"):
    try:
        new_advice = get_advice()
        if new_advice:
            st.markdown(f"<p style='font-style: italic; color:#333;'>{new_advice}</p>", unsafe_allow_html=True)
        else:
            st.warning("No advice received. Please try again.")
    except Exception as e:
        st.error("Something went wrong while getting advice.")
        st.exception(e)
else:
    st.info("Click the button above to receive micro-coaching advice.")
