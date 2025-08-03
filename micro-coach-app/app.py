# app.py

import streamlit as st
from coach_engine import get_advice

st.set_page_config(page_title="🧠 Micro-Coach", layout="centered")
st.title("🧠 Micro-Coach: One-Sentence Habit Trainer")
st.subheader("Enter your goal or struggle — get 1 sentence of smart advice.")

user_input = st.text_input("💬 What's your current goal or struggle?")

if user_input:
    advice = get_advice(user_input)
    st.markdown(f"### 🗣️ Advice:\n> {advice}")

    if st.button("🔁 Another Tip"):
        st.markdown(f"> {get_advice(user_input)}")