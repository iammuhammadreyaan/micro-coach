# app.py

import streamlit as st
from coach_engine import get_advice

st.set_page_config(page_title="🧠 Micro-Coach", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧠 Micro-Coach</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Your daily dose of human-like habit wisdom — in one clean sentence.</p>", unsafe_allow_html=True)
st.divider()

user_input = st.text_area("💬 What's something you're trying to fix, build, or improve?", height=100)

if user_input:
    advice = get_advice(user_input)

    st.markdown(
        f"""
        <div style='background-color:#f0f0f0; padding: 15px; border-radius: 10px;'>
            <h4 style='color:#333;'>💡 {advice}</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🔁 Give me another take"):
     new_advice = get_advice(user_input)
    st.markdown(
        f"""
        <div style='background-color:#e8f0fe; padding: 15px; border-radius: 10px; margin-top: 15px;'>
            <h4 style='color:#222;'>🗣️ Another take:</h4>
            <p style='font-style: italic; color:#333;'>{new_advice}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("<hr style='margin-top: 30px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 13px;'>Made with ❤️ by Muhammad Reyaan</p>", unsafe_allow_html=True)
