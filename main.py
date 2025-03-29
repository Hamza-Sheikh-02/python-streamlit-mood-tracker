"""
This is the main file for the Mood Tracker application.
It handles the Streamlit page configuration, database connection,
and core functionality.
"""
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import database as db

# Load environment variables from .env file
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="Mood Tracker",
    page_icon="🙂",
    layout="wide"
)

# Establish database connection and ensure mood table exists
conn = db.connect_to_database()
db.create_mood_table(conn)

# Custom UI styling
st.markdown(
    """
    <style>
    #MainMenu, footer {visibility: hidden;}
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
    }
    .subtitle {font-size: 18px; color: #555; text-align: center;}
    .stButton>button {width: 100%;}
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and subtitle
st.markdown(
    """
    <h1 class="main-title">🙂 Mood Tracker</h1>
    <p class="subtitle">By Hamza Sheikh</p>
    """,
    unsafe_allow_html=True
)

# User name input
user_name = st.text_input("Enter your name", value="", key="username_input")

if user_name.strip() == "":
    st.warning("Please enter your name to continue.")
else:
    db_user_name = user_name.lower()

    # Display welcome message
    st.write(f"Welcome, {user_name}!")

    # Fetch last mood from database to set as default
    last_mood = db.load_last_mood(conn, db_user_name)
    default_mood = last_mood if last_mood else "Happy"

    # Mood selection
    st.subheader("How are you feeling today?")
    moods = ["Happy", "Sad", "Angry", "Stressed",
             "Anxious", "Neutral", "Excited"]
    default_index = moods.index(default_mood) if default_mood in moods else 0
    mood = st.selectbox("Select your mood", moods, index=default_index)

    # Save mood to database
    if st.button("Save Mood"):
        db.save_mood(conn, db_user_name, mood)
        st.success("Mood saved successfully!")

    # Display mood log
    st.subheader("Your Mood Log")
    mood_log = db.load_mood_log(conn, db_user_name)
    if mood_log:
        tab1, tab2 = st.tabs(["Data", "Graph"])
        # Convert mood log to a pandas DataFrame for display
        df = pd.DataFrame(mood_log)[["mood", "created_at"]]
        df["created_at"] = df["created_at"].dt.strftime("%Y-%m-%d %H:%M:%S")
        with tab1:
            st.dataframe(
                df.rename(columns={"mood": "Mood", "created_at": "Date"}),
                hide_index=True,
                use_container_width=True
            )
        with tab2:
            st.line_chart(df, x="created_at", y="mood")
    else:
        st.info("No mood logs found for you.")
