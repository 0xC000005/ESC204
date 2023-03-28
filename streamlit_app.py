import streamlit as st
import pandas as pd
import io
import time
import pydeck as pdk
import numpy as np

def process_csv_data(csv_string):
    df = pd.read_csv(io.StringIO(csv_string), parse_dates=['timestamp'])
    return df

def plot_movement(df):
    view_state = pdk.ViewState(
        latitude=df['latitude'].mean(),
        longitude=df['longitude'].mean(),
        zoom=15,
        pitch=0,
        bearing=0
    )

    layer = pdk.Layer(
        "ScatterplotLayer",
        df,
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        radius_scale=10,
        radius_min_pixels=5,
        radius_max_pixels=100,
        line_width_min_pixels=1,
        get_position=["longitude", "latitude"],
        get_radius=30,
        get_fill_color="[200, 30, 0, 160]",
        get_line_color=[255, 255, 255],
    )

    st.pydeck_chart(pdk.Deck(map_style="mapbox://styles/mapbox/light-v10", layers=[layer], initial_view_state=view_state, tooltip={"text": "HDOP: {HDOP}"}))

def play_animation(df):
    map_animation = st.empty()
    for idx, row in df.iterrows():
        current_location = pd.DataFrame([row], columns=df.columns)
        plot_movement(df.iloc[:idx+1])
        time.sleep(0.5)

def main():
    st.set_page_config(page_title="GNSS Module Visualization", layout="wide")
    st.title("GNSS Module Visualization")
    st.markdown("""
    Welcome to the GNSS Module Visualization app!
    Please paste your CSV formatted text below, and press "Display" to show the animated movement.
    """)

    st.markdown("### Example CSV format")
    st.markdown("""
    ```
    timestamp,latitude,longitude,fix_status,HDOP,satellites_in_use
    2023-03-28T09:00:00,43.662623,-79.397066,3,1.2,7
    2023-03-28T09:00:10,43.662718,-79.396846,3,1.1,8
    ...
    ```
    """)

    csv_input = st.text_area("Paste your CSV formatted text here:")
    display_button = st.button("Display")
    replay_button = st.button("Replay Animation")

    if display_button and csv_input:
        df = process_csv_data(csv_input)
        st.markdown("### Map Visualization")
        plot_movement(df)
        st.markdown("### Signal Strength")
        st.write("Signal strength is represented by the Horizontal Dilution of Precision (HDOP) in the table below.")
        st.write(df[['timestamp', 'HDOP']])

    if replay_button and df is not None:
        st.markdown("### Animated Movement")
        st.markdown("The animation below shows the gradual movement of the GNSS module.")
        play_animation(df)

if __name__ == "__main__":
    main()
