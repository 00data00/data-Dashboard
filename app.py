import streamlit as st

# Set the title of the app
st.title("🏦 Bank Customer Churn Prediction")

# Display a team photo (make sure to replace 'team_photo.png' with your image file)
st.image("team_photo.png", caption="Our Amazing Team", use_column_width=True)

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
