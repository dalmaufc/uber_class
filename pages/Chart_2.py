import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Chart 2: Uber Data Trends")

df = pd.read_csv("../data/uber-data.zip")

# Example chart
fig = px.scatter(df, x="pickup_hour", y="ride_count", title="Scatter of Rides")
st.plotly_chart(fig)