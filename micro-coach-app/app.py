# app.py

import streamlit as st
from coach_engine import get_advice

# Page settings
st.set_page_config(page_title="🧠 Micro-Coach", layout="centered")

# App header
st.markdown("<h1 style='text-align: center;'>🧠 Micro-Coach</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your AI-powered mini life coach for quick advice.</p>", unsafe_allow_html=True)

# Button to get new advice
if st.button("💡 Get Advice"):
    new_advice = get_advice()
    st.markdown(f"<p style='font-style: italic; color:#333;'>{new_advice}</p>", unsafe_allow_html=True)
