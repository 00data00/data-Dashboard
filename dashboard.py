import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('Bank Customer Churn Prediction - Bank Customer Churn Prediction.csv')

# Sidebar for filters
st.sidebar.title("Filter Options")

# Country Filter
selected_country = st.sidebar.multiselect("Select Country", options=data['country'].unique(), default=data['country'].unique())

# Gender Filter
selected_gender = st.sidebar.multiselect("Select Gender", options=data['gender'].unique(), default=data['gender'].unique())

# Churn Filter
selected_churn = st.sidebar.radio("Churn Status", options=[0, 1], index=0, format_func=lambda x: "No" if x == 0 else "Yes")

# Age Filter
min_age, max_age = int(data['age'].min()), int(data['age'].max())
age_range = st.sidebar.slider("Select Age Range", min_age, max_age, (min_age, max_age))

# Credit Score Filter
min_credit, max_credit = int(data['credit_score'].min()), int(data['credit_score'].max())
credit_score_range = st.sidebar.slider("Select Credit Score Range", min_credit, max_credit, (min_credit, max_credit))

# Balance Filter
min_balance, max_balance = float(data['balance'].min()), float(data['balance'].max())
balance_range = st.sidebar.slider("Select Balance Range", min_balance, max_balance, (min_balance, max_balance))

# Tenure Filter
min_tenure, max_tenure = int(data['tenure'].min()), int(data['tenure'].max())
tenure_range = st.sidebar.slider("Select Tenure Range", min_tenure, max_tenure, (min_tenure, max_tenure))

# Filter the data based on the sidebar selections
filtered_data = data[(data['country'].isin(selected_country)) &
                     (data['gender'].isin(selected_gender)) &
                     (data['churn'] == selected_churn) &
                     (data['age'].between(age_range[0], age_range[1])) &
                     (data['credit_score'].between(credit_score_range[0], credit_score_range[1])) &
                     (data['balance'].between(balance_range[0], balance_range[1])) &
                     (data['tenure'].between(tenure_range[0], tenure_range[1]))]

# App Title
st.title("Enhanced Customer Churn Dashboard")

# Overview Section (Four Columns for Key Metrics)
st.header("Overview")
col1, col2, col3, col4 = st.columns(4)

total_customers = filtered_data.shape[0]
churn_rate = filtered_data['churn'].mean() * 100
average_credit_score = filtered_data['credit_score'].mean()
average_salary = filtered_data['estimated_salary'].mean()

# Display key metrics in four columns
col1.metric(label="Total Filtered Customers", value=f"{total_customers}")
col2.metric(label="Churn Rate", value=f"{churn_rate:.2f}%")
col3.metric(label="Average Credit Score", value=f"{average_credit_score:.2f}")
col4.metric(label="Average Estimated Salary", value=f"${average_salary:,.2f}")

# Responsive Gender Distribution Pie Chart (Half Page Width)
st.subheader("Gender Distribution")
gender_counts = filtered_data['gender'].value_counts()
col5, col6 = st.columns(2)

with col5:
    fig1, ax1 = plt.subplots(figsize=(5, 5))  # Adjust size for responsiveness
    ax1.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

# Churn by Country Bar Chart
st.subheader("Churn by Country")
country_churn = filtered_data.groupby('country')['churn'].mean() * 100
st.bar_chart(country_churn)

# Churn by Age Group
st.subheader("Churn by Age Group")
filtered_data['age_group'] = pd.cut(filtered_data['age'], bins=[18, 30, 40, 50, 60, 100], labels=['18-30', '30-40', '40-50', '50-60', '60+'])
age_churn = filtered_data.groupby('age_group')['churn'].mean() * 100
st.bar_chart(age_churn)

# Churn by Tenure Line Chart
st.subheader("Churn by Tenure")
tenure_churn = filtered_data.groupby('tenure')['churn'].mean() * 100
st.line_chart(tenure_churn)

# Customer Profile Breakdown Section
st.header("Customer Profile Breakdown")

# Distribution of Credit Scores
st.subheader("Distribution of Credit Scores")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_data['credit_score'], kde=True, ax=ax2, color='blue')
st.pyplot(fig2)

# Active vs Non-Active Members
st.subheader("Active vs Non-Active Members")
active_counts = filtered_data['active_member'].value_counts()
fig3, ax3 = plt.subplots()
ax3.pie(active_counts, labels=["Active", "Non-Active"], autopct='%1.1f%%', startangle=90, colors=['#99ff99','#ffcc99'])
ax3.axis('equal')
st.pyplot(fig3)

# Products Owned by Customers
st.subheader("Products Owned by Customers")
products_count = filtered_data['products_number'].value_counts()
st.bar_chart(products_count)

# Balance Distribution
st.subheader("Balance Distribution")
fig4, ax4 = plt.subplots()
sns.histplot(filtered_data['balance'], kde=True, ax=ax4, color='green')
st.pyplot(fig4)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
# Select only numerical features for correlation calculation
numerical_features = filtered_data.select_dtypes(include=['number']) 
corr = numerical_features.corr()  # Calculate correlation on numerical columns only
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax5)
st.pyplot(fig5)
