import streamlit as st

# Set the title of the app
st.title("🏦 Bank Customer Churn Prediction")


# Team members with emojis
st.write("### Our Team: 👩‍💻👨‍💻")
team_members = [
    "Donya Samir 🎉",
    "Esraa Mosaad 🎉",
    "Mostafa Omar 🎉",
    "Nour Ehab 🎉",
    "Talal Ibrahim 🎉"
]
for member in team_members:
    st.write(f"- {member}")

# Problem section
st.subheader("🚩 Problem:")
st.write("High churn rates lead to loss of customers for banks. 😟")

# Objective section
st.subheader("🎯 Objective:")
st.write("Predict bank customer churn and build interactive dashboards. 📊")
