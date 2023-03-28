import streamlit as st
import pandas as pd
import io
import time

def process_csv_data(csv_string):
    df = pd.read_csv(io.StringIO(csv_string), parse_dates=['timestamp'])
    return df

def plot_movement(df):
    st.map(df)

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
        plot_movement(df)
        st.markdown("### Signal Strength")
        st.write("Signal strength is represented by the Horizontal Dilution of Precision (HDOP) in the table below.")
        st.write(df[['timestamp', 'HDOP']])

        st.markdown("### Animated Movement")
        st.markdown("The animation below shows the gradual movement of the GNSS module.")
        map_animation = st.empty()
        for idx, row in df.iterrows():
            current_location = pd.DataFrame([row], columns=df.columns)
            map_animation.map(current_location)
            time.sleep(0.5)

if __name__ == "__main__":
    main()
