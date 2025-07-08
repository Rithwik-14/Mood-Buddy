import streamlit as st
from mood_logic import get_mood_response
import random
from datetime import datetime
import os
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1518837695005-2083093ee35b");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
    h1, h2, h3, p, div, span, label {
        color: #ffffff !important;
        text-shadow: 1px 1px 2px #000000;
    }
    </style>
""", unsafe_allow_html=True)



JOURNAL_PASSWORD = "Letsgoo"

def format_fancy_timestamp():
    now = datetime.now()
    day = int(now.strftime("%d"))
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    date_str = now.strftime(f"%B {day}{suffix} %Y, %I:%M %p")
    return date_str.lower().replace("am", "a.m.").replace("pm", "p.m.")


st.set_page_config(
    page_title="AI Mood Buddy",
    page_icon="🧠",
    layout="centered"
)
st.set_page_config(
    page_title="AI Mood Buddy",
    page_icon="🧠",
    layout="centered"
)
if "show_history" not in st.session_state:
    st.session_state.show_history = False

if "password_correct" not in st.session_state:
    st.session_state.password_correct = False

affirmations = [
    "You are doing your best and that’s enough.",
    "Every struggle is making you stronger.",
    "You are worthy of peace and progress.",
    "Your journey is uniquely beautiful.",
    "You’ve got what it takes to get through this.",
    "Progress, not perfection."
]


st.set_page_config(page_title="AI Mood Buddy", page_icon="💙", layout="centered")

st.title("💙 AI Mood Buddy")
st.subheader("Hey! How are you feeling today ? 💙")


mood = st.selectbox(
    "How are you feeling today?",
    [
        "😔Sad", "😣Stressed", "😠Angry", "😴Tired",
        "😄Happy", "😕Lost", "😰Anxious", "🙏Grateful"
    ]
)


if st.button("Give me support 💬"):
        st.session_state["show_support"] = True
if "show_support" in st.session_state and st.session_state["show_support"]:

        response = get_mood_response(mood)
        st.markdown(f"**🧠 Quote:** {response['quote']}")
        st.markdown(f"**🎵 Music Suggestion:** [{response['music']}]({response['music']})")
        st.markdown(f"**✨ Action Tip:** {response['action']}")
        st.markdown(f"**💖 Affirmation:** _{random.choice(affirmations)}_")


        st.markdown("---")
        st.subheader("📝 Want to reflect more?")
        journal = st.text_area("Write your thoughts here...")
        if st.button("Save Journal"):
            with open("journal.txt", "a", encoding="utf-8") as file:
                timestamp = format_fancy_timestamp()
                file.write(f"[{timestamp}] {mood} - {journal}\n")
            st.success("Journal entry saved!")
        

        if st.button("Show History"):
            st.session_state.show_history = True
            st.session_state.password_correct = False


        if st.session_state.show_history and not st.session_state.password_correct:
            password = st.text_input("🔐 Enter your journal password", type="password")
            if password:
                if password == JOURNAL_PASSWORD:
                    st.session_state.password_correct = True
                else:
                    st.error("❌ Incorrect password.")


        if st.session_state.show_history and st.session_state.password_correct:
            try:
                with open("journal.txt", "r", encoding="utf-8") as file:
                    history = file.read()

                if history.strip():
                    st.markdown("### 📚 Your Past Journal Entries")
                    for line in history.splitlines():
                        st.markdown(f"- {line}")

                else:
                    st.info("Your journal is currently empty.")

        
                if st.button("🧹 Clear Journal History"):
                    open("journal.txt", "w", encoding="utf-8").close()
                    st.success("Journal history cleared successfully.")
                    st.session_state.show_history = False
                    st.session_state.password_correct = False
                    st.rerun()

            except FileNotFoundError:
                    st.warning("No journal history found yet.")


try:
    emoji_font = fm.FontProperties(fname="C:/Windows/Fonts/seguiemj.ttf")
except:
    emoji_font = None

MOOD_COLORS = {
    "😄Happy": "#FFD700",   
    "😔Sad": "#87CEFA",     
    "😠Angry": "#FF6347",     
    "😫Stressed": "#FFA500",  
    "🙏Grateful": "#90EE90",  
    "😕Lost": "#D8BFD8",      
    "😴Tired": "#C0C0C0",     
    "😰Anxious": "#FFB6C1"    
}


if st.button("📊 Show Average Mood"):
    try:
        with open("journal.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        moods = []
        for line in lines:
            if "]" in line:
                mood_section = line.split("]")[1].split(" - ")[0].strip()
                moods.append(mood_section)

        if moods:
            mood_counts = Counter(moods)
            most_common_mood, count = mood_counts.most_common(1)[0]

            st.markdown("### 🧠 Your Most Frequent Mood")
            st.markdown(f"#### {most_common_mood} — {count} times")

            # Pie Chart
            labels = list(mood_counts.keys())
            sizes = list(mood_counts.values())

            fig, ax = plt.subplots()
            wedges, texts, autotexts = ax.pie(
                sizes, labels=labels, autopct="%1.1f%%", startangle=90
            )

            if emoji_font:
                for text in texts + autotexts:
                    text.set_fontproperties(emoji_font)

            ax.axis("equal")
            st.pyplot(fig)

        else:
            st.info("No mood entries found.")

    except FileNotFoundError:
        st.warning("journal.txt not found.")


MOOD_SCORES = {
    "😠Angry": 1,
    "😕Lost": 2,
    "😟Anxious": 3,
    "😫Stressed": 4,
    "😔Sad": 5,
    "😴Tired": 6,
    "🙏Grateful": 7,
    "😄Happy": 8
}


if st.button("📅 Show Mood Timeline"):
    try:
        with open("journal.txt", "r") as file:
            lines = file.readlines()

        mood_dates = []
        mood_values = []

        for line in lines:
            if "]" in line:
                timestamp_part = line.split("]")[0].strip("[")
                try:
                    timestamp = datetime.strptime(timestamp_part, "%B %dth %Y, %I:%M %p")
                except ValueError:
                    continue  # Skip badly formatted lines

                mood_part = line.split("]")[1].split(" - ")[0].strip()
                if mood_part in MOOD_SCORES:
                    mood_dates.append(timestamp)
                    mood_values.append(MOOD_SCORES[mood_part])

        if mood_dates:
            fig, ax = plt.subplots()
            ax.plot(mood_dates, mood_values, marker="o", linestyle="-")
            ax.set_title("🧠 Mood Over Time")
            ax.set_xlabel("Date")
            ax.set_ylabel("Mood Level")
            ax.set_yticks(list(MOOD_SCORES.values()))
            ax.set_yticklabels([mood for mood, score in sorted(MOOD_SCORES.items(), key=lambda x: x[1])])
            plt.xticks(rotation=30)
            st.pyplot(fig)
        else:
            st.info("Not enough mood entries to plot a timeline.")

    except FileNotFoundError:
        st.warning("Journal file not found.")




