import streamlit as st
import pandas as pd
import time
import folium
from streamlit_folium import folium_static


def process_csv_data(csv_string):
    df = pd.read_csv(pd.StringIO(csv_string), parse_dates=['timestamp'])
    return df


def plot_movement(df, point_radius):
    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=12)
    for index, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=point_radius,
            color='red',
            fill=True,
            fill_color='red'
        ).add_to(m)
    folium_static(m)


def main():
    st.set_page_config(page_title="GNSS Module Visualization", layout="wide")
    st.title("GNSS Module Visualization")
    st.markdown("""
    Welcome to the GNSS Module Visualization app!
    Please paste your CSV formatted text below, and press "Display" to show the animated movement.
    """)

    csv_input = st.text_area("Paste your CSV formatted text here:")
    display_button = st.button("Display")

    if display_button and csv_input:
        st.markdown("### Map Visualization")
        df = process_csv_data(csv_input)
        point_radius = st.slider("Point size", min_value=1, max_value=50, value=5, step=1)
        plot_movement(df, point_radius)


if __name__ == "__main__":
    main()
