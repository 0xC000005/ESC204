import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from datetime import datetime

# Title and objective
st.title("GNSS Location Movement Logs Visualization")
st.write("Visualize GNSS location movement logs interactively with Streamlit")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload your GNSS log file in CSV format", type=["csv"])

if uploaded_file:
    # Read and parse CSV
    data = pd.read_csv(uploaded_file)
    data["timestamp"] = pd.to_datetime(data["timestamp"])

    # Filter options
    st.sidebar.header("Filter Options")
    start_date = st.sidebar.date_input("Start date", min_value=data["timestamp"].min().date())
    end_date = st.sidebar.date_input("End date", max_value=data["timestamp"].max().date(), value=data["timestamp"].max().date())
    fix_status_filter = st.sidebar.selectbox("Filter by fix status", options=sorted(data["fix_status"].unique()), index=0)
    min_satellites = st.sidebar.slider("Minimum number of satellites in use", min_value=data["satellites_in_use"].min(), max_value=data["satellites_in_use"].max(), value=data["satellites_in_use"].min())

    # Filter data
    filtered_data = data[(data["timestamp"].dt.date >= start_date) & (data["timestamp"].dt.date <= end_date) & (data["fix_status"] == fix_status_filter) & (data["satellites_in_use"] >= min_satellites)]

    # Display summary statistics
    st.header("Summary Statistics")
    st.write("Total distance traveled: TODO")
    st.write("Average speed: TODO")
    st.write("Duration of the trip: TODO")

    # Display table
    st.header("Filtered Data")
    st.write(filtered_data)

    # Display map
    st.header("Interactive Map Visualization")
    map_center = [filtered_data["latitude"].mean(), filtered_data["longitude"].mean()]
    m = folium.Map(location=map_center, zoom_start=14)

    # Plot tracker path
    path = filtered_data[["latitude", "longitude"]].values.tolist()
    folium.PolyLine(path, color="blue", weight=5, opacity=0.7).add_to(m)

    # Add markers for each point
    for lat, lon, time in zip(filtered_data["latitude"], filtered_data["longitude"], filtered_data["timestamp"]):
        folium.Marker(
            location=[lat, lon],
            icon=None,
            popup=f"Time: {time}"
        ).add_to(m)

    folium_static(m)
else:
    st.warning("Please upload a GNSS log file in CSV format")
    st.stop()
