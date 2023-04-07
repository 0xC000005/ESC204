import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from datetime import datetime
from geopy.distance import geodesic


def display_example_csv():
    st.markdown("### Example CSV format")
    st.markdown(
        """
        | timestamp          | latitude  | longitude  | fix_status | HDOP | satellites_in_use |
        |--------------------|-----------|------------|------------|------|-------------------|
        | 2023-03-28T09:00:00 | 43.662623 | -79.397066 |          3 |  1.2 |                 7 |
        | 2023-03-28T09:00:10 | 43.662718 | -79.396846 |          3 |  1.1 |                 8 |
        | 2023-03-28T09:00:20 | 43.662820 | -79.396640 |          3 |  1.0 |                 9 |
        | 2023-03-28T09:00:30 | 43.662917 | -79.396458 |          2 |  1.1 |                 8 |
        | 2023-03-28T09:00:40 | 43.663011 | -79.396249 |          2 |  1.2 |                 7 |
        | 2023-03-28T09:00:50 | 43.663076 | -79.396079 |          1 |  1.3 |                 6 |
        | 2023-03-28T09:01:00 | 43.663192 | -79.395890 |          3 |  1.2 |                 7 |
        | 2023-03-28T09:01:10 | 43.663284 | -79.395698 |          2 |  1.3 |                 6 |
        | 2023-03-28T09:01:20 | 43.663376 | -79.395495 |          3 |  1.1 |                 8 |
        | 2023-03-28T09:01:30 | 43.663474 | -79.395321 |          2 |  1.2 |                 7 |
        """
    )
    st.markdown(
        """
        **Fix status number representation:**
        - 1: No fix
        - 2: 2D fix
        - 3: 3D fix
        """
    )

# allow user to download example csv from a weblink by using st.download_button
def download_example_csv():
    csv = 'https://raw.githubusercontent.com/0xC000005/ESC204/main/example_input.csv'
    # st.markdown("### Download Example CSV")
    st.markdown("Click the button below to download the example CSV file.")
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='example_input.csv',
        mime='text/csv'
    )

def read_data(uploaded_file):
    data = pd.read_csv(uploaded_file)
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    # Convert latitude and longitude to float
    data["latitude"] = data["latitude"].astype(float)
    data["longitude"] = data["longitude"].astype(float)
    # Convert fix_status to int
    data["fix_status"] = data["fix_status"].astype(int)
    # Convert HDOP to float
    data["HDOP"] = data["HDOP"].astype(float)
    # Convert satellites_in_use to int, not numpy.int32
    data["satellites_in_use"] = data["satellites_in_use"].astype(int)

    # Filter out invalid data
    data = data[(data["latitude"] != 0) & (data["longitude"] != 0)]
    # Filter out data with NaN values
    data = data.dropna()
    return data


def display_filter_options(data):
    st.sidebar.header("Filter Options")
    start_date = st.sidebar.date_input("Start date", min_value=data["timestamp"].min().date(),
                                       value=data["timestamp"].min().date())
    start_time = st.sidebar.time_input("Start time", value=data["timestamp"].min().time())
    end_date = st.sidebar.date_input("End date", max_value=data["timestamp"].max().date(),
                                     value=data["timestamp"].max().date())
    end_time = st.sidebar.time_input("End time", value=data["timestamp"].max().time())

    start_datetime = pd.to_datetime(f"{start_date} {start_time}")
    end_datetime = pd.to_datetime(f"{end_date} {end_time}")

    fix_status_filter = st.sidebar.multiselect("Filter by fix status", options=sorted(data["fix_status"].unique()),
                                               default=sorted(data["fix_status"].unique()))

    min_satellites_value = int(data["satellites_in_use"].min())
    max_satellites_value = int(data["satellites_in_use"].max())

    if min_satellites_value == max_satellites_value:
        min_satellites = min_satellites_value
        st.sidebar.markdown(f"Minimum number of satellites in use: {min_satellites}")
    else:
        min_satellites = st.sidebar.slider("Minimum number of satellites in use",
                                           min_value=min_satellites_value,
                                           max_value=max_satellites_value,
                                           value=min_satellites_value)
    return start_datetime, end_datetime, fix_status_filter, min_satellites


def filter_data(data, start_datetime, end_datetime, fix_status_filter, min_satellites):
    return data[(data["timestamp"] >= start_datetime) & (data["timestamp"] <= end_datetime) & (
        data["fix_status"].isin(fix_status_filter)) & (data["satellites_in_use"] >= min_satellites)]


def calculate_total_distance(data):
    total_distance = 0
    for i in range(len(data) - 1):
        coords1 = (data.iloc[i]["latitude"], data.iloc[i]["longitude"])
        coords2 = (data.iloc[i + 1]["latitude"], data.iloc[i + 1]["longitude"])
        total_distance += geodesic(coords1, coords2).meters
    return total_distance


def calculate_duration(data):
    duration = data["timestamp"].max() - data["timestamp"].min()
    return duration


def calculate_average_speed(data, total_distance, duration):
    duration_seconds = duration.total_seconds()
    if duration_seconds > 0:
        average_speed = total_distance / duration_seconds
    else:
        average_speed = 0
    return average_speed


def display_summary_statistics(filtered_data):
    st.header("Summary Statistics")
    total_distance = calculate_total_distance(filtered_data)
    st.write(f"Total distance traveled: {total_distance:.2f} meters")

    duration = calculate_duration(filtered_data)
    st.write(f"Duration of the trip: {duration}")

    average_speed = calculate_average_speed(filtered_data, total_distance, duration)
    st.write(f"Average speed: {average_speed * 3.6:.2f} km/h")  # Convert m/s to km/h


def display_filtered_data(filtered_data):
    st.header("Filtered Data")
    st.write(filtered_data)


def display_map(filtered_data):
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


def display_image_with_caption(image_url, caption, width=None):
    if width is not None:
        st.image(image_url, caption=caption, width=width)
    else:
        st.image(image_url, caption=caption, use_column_width='auto')


def display_author_info():
    author_name = "Max Zhang"
    author_github_url = "https://github.com/0xC000005"
    st.markdown(f"**Author:** [{author_name}]({author_github_url}) 👈 Click to check out my GitHub page!")


def main():
    st.title("GNSS Location Movement Logs Visualization")
    st.write("Visualize GNSS location movement logs interactively with Streamlit")
    # Display author information and link to the author's GitHub page
    display_author_info()
    # Display the example CSV file
    display_example_csv()
    # Display download button for the example CSV file
    download_example_csv()

    uploaded_file = st.sidebar.file_uploader("Upload your GNSS log file in CSV format", type=["csv"])

    if uploaded_file:
        data = read_data(uploaded_file)
        start_date, end_date, fix_status_filter, min_satellites = display_filter_options(data)
        filtered_data = filter_data(data, start_date, end_date, fix_status_filter, min_satellites)

        if not filtered_data.empty:
            display_summary_statistics(filtered_data)  # Pass filtered_data as an argument
            display_filtered_data(filtered_data)
            display_map(filtered_data)
        else:
            st.warning("No filtered data to display")
    else:
        st.warning("Please upload a GNSS log file in CSV format")
        st.stop()



if __name__ == "__main__":
    main()
