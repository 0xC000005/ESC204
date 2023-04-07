# GNSS Visualizing Streamlit Website Engineering Handbook

## Purpose of the Prototype
1. To communicate to stakeholders how the data collected from our garbage tracker will look like
2. To provide a basic, flexible and open-sourced platform for the stakeholders to interact with the data interpolation, and to enable further customized data analysis by the stakeholders
3. To explore different ways to utilize the data collected from the garbage tracker to better understand the garbage problem in Accra, Ghana

## Requirement Considered
| Feature Name               | Requirement                                      | Consideration                                                                                   |
|----------------------------|--------------------------------------------------|-------------------------------------------------------------------------------------------------|
| GNSS Data Upload           | Allow users to upload GNSS log files             | Support multiple file formats (e.g., GPX, KML, CSV) and handle large datasets                   |
| Map-based Visualization    | Display GNSS data on an interactive map          | Utilize a high-quality map service (e.g., OpenStreetMap, Google Maps) for accurate representation|
| Data Filtering             | Provide filtering options for GNSS data          | Include options for filtering by time, satellite system, signal strength, etc.                  |
| Data Export                | Allow users to export filtered/processed data    | Support multiple export formats (e.g., CSV, JSON, KML) and enable selective data export          |
| Performance Optimization   | Ensure smooth performance for large datasets     | Implement efficient data processing and visualization techniques                                 |
| User Interface & Experience | Develop an intuitive and easy-to-use interface   | Prioritize a clean and modern design that is responsive and visually appealing                    |

Besides the above functionalities, helper scripts were also developed to help calibrate the raw GNSS data by allowing horizontal, vertical, and temporal offsets to be applied to the data. The scripts were written in Python and can be found in the [adjust_gps.py](https://github.com/0xC000005/ESC204/blob/main/adjust_gps.py)


## GNSS Visualizing Streamlit Website: Version 1

The main features included in this version are:

- CSV data input as a String
- No filtering options
- Displaying summary statistics
- Displaying filtered data
- Map visualization

In the first version of the prototype, the main goal was to create a simple web-based tool for uploading GNSS log files in CSV format, processing the data, and visualizing the movements on an interactive map. The uploaded CSV data was processed using the Pandas library, and map visualization was achieved using Streamlit's built-in map functionality and the Pydeck library.

The user interface provided a text area for pasting CSV-formatted data and two buttons: "Display" and "Replay Animation." The "Display" button generated a static map visualization, showing the entire movement track, and a table displaying the timestamp and Horizontal Dilution of Precision (HDOP) as a representation of signal strength. The "Replay Animation" button played an animation of the GNSS module's movement on the map, simulating the movement's progression.

Although the prototype offered basic functionality for GNSS data visualization, it served as a foundation for further improvements, such as additional data filtering, support for different file formats, and more advanced visualization techniques.

## GNSS Visualizing Streamlit Website: Version 2

Version 2 of the website introduced additional features to enhance the user experience and provide more detailed information. The main improvements and changes in this version are:

- Added a time slider for data filtering
- Fixed map disappearing issue after dragging the slider
- Improved input display and slider functionality
- Enhanced the overall user interface

## GNSS Visualizing Streamlit Website: Version 3

Version 3 of the website focused on refining the app and ensuring it functioned smoothly. The main changes and enhancements included in this version are:

- Switched from pydeck to folium for map visualization
- Removed redundant main() function
- Changed the example CSV position

Throughout the development process, smaller changes were also made to improve the app's performance, fix issues, and optimize the user experience.
