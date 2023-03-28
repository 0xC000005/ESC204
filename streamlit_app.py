import streamlit as st
import pandas as pd
from streamlit_leaflet import stleaflet

def process_csv_data(csv_string):
    df = pd.read_csv(pd.StringIO(csv_string), parse_dates=['timestamp'])
    return df

def plot_movement(df, point_size):
    center = [df['latitude'].mean(), df['longitude'].mean()]
    zoom = 10

    map_data = df[['latitude', 'longitude']].copy()
    map_data['size'] = point_size

    stleaflet.map(
        center=center,
        zoom=zoom,
        data=map_data.to_dict(orient='records'),
        draggable_circles=True,
        radius_multiplier=1.0,
    )

def main():
    st.set_page_config(page_title="GNSS Module Visualization", layout="wide")
    st.title("GNSS Module Visualization")
    st.markdown("""
    Welcome to the GNSS Module Visualization app!
    Please paste your CSV formatted text below, and press "Display" to show the animated movement.
    """)

    csv_input = st.text_area("Paste your CSV formatted text here:")
    display_button = st.button("Display")
    point_size = st.slider("Point size", min_value=1, max_value=50, value=10, step=1)

    if display_button and csv_input:
        st.markdown("### Map Visualization")
        df = process_csv_data(csv_input)
        plot_movement(df, point_size)

if __name__ == "__main__":
    main()
