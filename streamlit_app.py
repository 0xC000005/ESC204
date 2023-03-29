import streamlit as st
import pandas as pd
import time
import folium
from streamlit_folium import folium_static
from folium.plugins import TimestampedGeoJson


def process_csv_data(csv_string):
    df = pd.read_csv(pd.StringIO(csv_string), parse_dates=['timestamp'])
    return df


# Rest of the code remains unchanged.


def plot_movement(df, point_radius):
    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=13)

    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['longitude'], row['latitude']]
            },
            'properties': {
                'times': [row['timestamp'].strftime('%Y-%m-%dT%H:%M:%SZ')],
                'style': {'radius': point_radius, 'color': 'blue'}
            }
        }
        for _, row in df.iterrows()
    ]

    TimestampedGeoJson(
        {'type': 'FeatureCollection', 'features': features},
        period='PT1M',
        add_last_point=True,
        auto_play=False,
        loop=False,
        max_speed=1,
        loop_button=True,
        date_options='YYYY-MM-DD HH:mm:ss',
        time_slider_drag_update=True,
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
        point_radius = st.slider("Point size", min_value=1, max_value=50, value=10)
        plot_movement(df, point_radius)


if __name__ == "__main__":
    main()
