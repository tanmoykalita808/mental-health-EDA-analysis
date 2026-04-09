import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🧠 Mental Health Dashboard")

# Load data
df = pd.read_csv("survey.csv")

st.subheader("Dataset Preview")
st.write(df.head())


col1, col2 = st.columns(2)

with col1:
    st.subheader("Benefits vs Treatment")
    fig, ax = plt.subplots()
    sns.countplot(x='benefits', hue='treatment', data=df, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Seek Help")
    fig, ax = plt.subplots()
    sns.countplot(x='seek_help', data=df, ax=ax)
    st.pyplot(fig)


col3, col4 = st.columns(2)

with col3:
    st.subheader("Work Interference")
    fig, ax = plt.subplots()
    sns.countplot(x='work_interfere', data=df, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col4:
    st.subheader("Supervisor Communication")
    fig, ax = plt.subplots()
    sns.countplot(x='supervisor', data=df, ax=ax)
    st.pyplot(fig)



st.markdown("## 🔍 Key Insights")

st.success("Employees with benefits are more likely to seek treatment.")

st.warning("Many employees hesitate to seek help due to stigma.")

st.info("Mental health significantly impacts work productivity.")