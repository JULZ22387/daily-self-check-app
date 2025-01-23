import streamlit as st
import pandas as pd
from datetime import datetime

# Set page title
st.set_page_config(page_title="Daily Self-Check App")

# Create or load the Excel file
try:
    df = pd.read_excel("Daily_Self_Check_App_Data.xlsx")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Mood", "Sleep", "Exercise", "Notes"])

# App title
st.title("Daily Self-Check App")

# Get today's date
today = datetime.now().strftime("%Y-%m-%d")

# Input fields
mood = st.slider("How's your mood today?", 1, 10, 5)
sleep = st.number_input("Hours of sleep last night:", min_value=0.0, max_value=24.0, step=0.5)
exercise = st.checkbox("Did you exercise today?")
notes = st.text_area("Any notes for today?")

# Submit button
if st.button("Submit"):
    new_data = pd.DataFrame({
        "Date": [today],
        "Mood": [mood],
        "Sleep": [sleep],
        "Exercise": [exercise],
        "Notes": [notes]
    })
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel("Daily_Self_Check_App_Data.xlsx", index=False)
    st.success("Data submitted successfully!")

# Display existing data
st.subheader("Existing Data")
st.dataframe(df)