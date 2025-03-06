import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Chart 1: Uber Data Analysis")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("../data/uber-data.zip")  # Modify to correct CSV path
    return df

df = load_data()

# Example chart
fig = px.histogram(df, x="pickup_hour", title="Rides Per Hour")
st.plotly_chart(fig)