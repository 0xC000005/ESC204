import streamlit as st
import pandas as pd
import io
import pydeck as pdk


def process_csv_data(csv_string):
    df = pd.read_csv(io.StringIO(csv_string), parse_dates=['timestamp'])
    return df


def plot_movement(df, slider_value, node_size):
    view_state = pdk.ViewState(
        latitude=df['latitude'].mean(),
        longitude=df['longitude'].mean(),
        zoom=15,
        pitch=0,
        bearing=0
    )

    layer = pdk.Layer(
        "ScatterplotLayer",
        df.iloc[:slider_value],
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        radius_scale=node_size,
        radius_min_pixels=3,
        radius_max_pixels=50,
        line_width_min_pixels=1,
        get_position=["longitude", "latitude"],
        get_radius=20,
        get_fill_color="[200, 30, 0, 160]",
        get_line_color=[255, 255, 255],
    )

    st.pydeck_chart(
        pdk.Deck(map_style="mapbox://styles/mapbox/light-v10", layers=[layer], initial_view_state=view_state,
                 tooltip={"text": "HDOP: {HDOP}"}))


def main():
    st.set_page_config(page_title="GNSS Module Visualization", layout="wide")
    st.title("GNSS Module Visualization")
    st.markdown("""
    Welcome to the GNSS Module Visualization app!
    Please paste your CSV formatted text below, and press "Display" to show the movement with a slider.
    """)

    st.markdown("### Example CSV format")
    st.markdown("""
    ```
    timestamp,latitude,longitude,fix_status,HDOP,satellites_in_use
    2023-03-28T09:00:00,43.662623,-79.397066,3,1.2,7
    2023-03-28T09:00:10,43.662718,-79.396846,3,1.1,8
    2023-03-28T09:00:20,43.662820,-79.396640,3,1.0,9
    2023-03-28T09:00:30,43.662917,-79.396458,2,1.1,8
    2023-03-28T09:00:40,43.663011,-79.396249,2,1.2,7
    2023-03-28T09:00:50,43.663076,-79.396079,1,1.3,6
    2023-03-28T09:01:00,43.663192,-79.395890,3,1.2,7
    2023-03-28T09:01:10,43.663284,-79.395698,2,1.3,6
    2023-03-28T09:01:20,43.663376,-79.395495,3,1.1,8
    2023-03-28T09:01:30,43.663474,-79.395321,2,1.2,7
    ```
    """)

    csv_input = st.text_area("Paste your CSV formatted text here:")
    display_button = st.button("Display")

    if display_button and csv_input:
        df = process_csv_data(csv_input)
        st.markdown("### Map Visualization")

        slider_value = st.slider("Move the slider to see the movement", min_value=1, max_value=len(df), value=len(df),
                                 step=1, key="slider_movement")
        node_size = st.slider("Adjust the size of the nodes", min_value=1, max_value=20, value=6, step=1,
                              key="slider_node_size")

        plot_movement(df, slider_value, node_size)
        st.markdown("### Signal Strength")
        st.write("Signal strength is represented by the Horizontal Dilution of Precision (HDOP) in the table below.")
        st.write(df[['timestamp', 'HDOP']])

        while True:
            slider_value = st.slider("Move the slider to see the movement", min_value=1, max_value=len(df),
                                     value=slider_value, step=1, key="slider_movement_update")
            node_size = st.slider("Adjust the size of the nodes", min_value=1, max_value=20, value=node_size, step=1,
                                  key="slider_node_size_update")
            plot_movement(df, slider_value, node_size)
            if not st.button("Update"):
                break


if __name__ == "__main__":
    main()
