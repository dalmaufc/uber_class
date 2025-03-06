import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Chart 3: Geographic Visualization")

df = pd.read_csv("data/uber-data.zip")

# Example chart
fig = px.scatter_mapbox(df, lat="lat", lon="lon", zoom=10)
fig.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig)