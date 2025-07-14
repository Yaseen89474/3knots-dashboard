import streamlit as st
import pandas as pd

st.set_page_config(page_title="3Knots Digital CEO Dashboard", layout="wide")

# Branding Header
st.markdown("""
    <div style='background-color:#1E1E2F;padding:20px;border-radius:10px'>
        <h1 style='color:#ffffff;text-align:center;'>3Knots Digital - CEO Dashboard</h1>
        <p style='color:#bbbbbb;text-align:center;'>https://3knotshost.com/</p>
    </div>
""", unsafe_allow_html=True)

role = st.sidebar.selectbox("Select your role", ["CEO", "Marketing", "Sales", "Projects"])
st.sidebar.markdown("---")
st.sidebar.info("Welcome to your role-based view")

# Google Sheet links
marketing_sheet = "https://docs.google.com/spreadsheets/d/1Q-BZaKmka9-Y8RkUXduT7v9qwA6TF8rAaoyDWAZumY8/edit?usp=sharing"
sales_sheet = "https://docs.google.com/spreadsheets/d/1ZV8xgRVXR1PZTI7n9_KvSclv8MQEd4zAAGCUuW1L1f4/edit?usp=sharing"
projects_sheet = "https://docs.google.com/spreadsheets/d/1GiE4AUs3Qxyk6XQ1Tj6Pa1q44MzOizxfRBLs90CptXw/edit?usp=sharing"

if role == "CEO":
    st.subheader("Full Dashboard Overview")
    st.markdown("📈 Sales Overview [Live Google Sheet]({})".format(sales_sheet))
    st.markdown("📊 Marketing Overview [Live Google Sheet]({})".format(marketing_sheet))
    st.markdown("✅ Project Tasks [Live Google Sheet]({})".format(projects_sheet))
elif role == "Marketing":
    st.subheader("Marketing Dashboard")
    st.markdown("📊 [Open Marketing Sheet]({})".format(marketing_sheet))
elif role == "Sales":
    st.subheader("Sales Dashboard")
    st.markdown("📈 [Open Sales Sheet]({})".format(sales_sheet))
elif role == "Projects":
    st.subheader("Project Dashboard")
    st.markdown("✅ [Open Project Tasks Sheet]({})".format(projects_sheet))

# Footer branding
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center style='color:gray;'>© 2025 3Knots Digital — All Rights Reserved</center>", unsafe_allow_html=True)