import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(page_title="EuPrime 3D-Model Lead Scorer", layout="wide")

# Title and Description
st.title("🧬 3D In-Vitro Model Lead Generation Agent")
st.markdown("""
This dashboard identifies, enriches, and ranks potential customers based on **Propensity to Buy** signals 
(Role, Funding, Technographics, Location, and Scientific Publications).
""")

# Load Data
try:
    df = pd.read_csv('leads_data_final.csv')
except FileNotFoundError:
    st.error("Data file not found. Please run the data generation script first.")
    st.stop()

# Sidebar Filters
st.sidebar.header("Filter Leads")
min_score = st.sidebar.slider("Minimum Propensity Score", 0, 100, 50)
location_filter = st.sidebar.text_input("Search Location (e.g., Boston)")

# Apply Filters
filtered_df = df[df['Propensity_Score'] >= min_score]
if location_filter:
    filtered_df = filtered_df[filtered_df['Location_Person'].str.contains(location_filter, case=False) | filtered_df['Location_HQ'].str.contains(location_filter, case=False)]

# Main Table
st.dataframe(filtered_df)


