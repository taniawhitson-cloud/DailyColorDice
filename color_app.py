import streamlit as st
import random

st.set_page_config(
    page_title="Daily Color Dice",
    page_icon="🎨"
)

colors = [
    ("❤️", "Red"),
    ("💙", "Blue"),
    ("💚", "Green"),
    ("💛", "Yellow"),
    ("💜", "Purple"),
    ("🧡", "Orange"),
    ("🩷", "Pink"),
    ("🤎", "Brown"),
    ("🖤", "Black"),
    ("🤍", "White"),
    ("🩵", "Sky Blue"),
    ("🩶", "Grey")
]

st.title("🎨 Daily Color Dice")
st.write("No bias. No cheating. One random color for everyone!")

if st.button("🎲 ROLL TODAY'S COLOR"):
    emoji, color = random.choice(colors)

    st.markdown(
        f"""
        <div style="
            background-color: #eeeeee;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
        ">
            <div style="font-size: 70px;">{emoji}</div>
            <h1>{color}</h1>
            <p>Today's outfit color!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(f"Everyone wears {color} today! 🎉")