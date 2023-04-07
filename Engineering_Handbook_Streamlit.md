# GNSS Visualizing Streamlit Website Engineering Handbook

Access the Streamlit app here: https://0xc000005-esc204-streamlit-app-kq3yff.streamlit.app/
Access the repository here: https://github.com/0xC000005/ESC204

## Table of Contents
1. [Introduction](#introduction)
2. [Purpose of the Prototype](#purpose-of-the-prototype)
3. [Requirement Considered](#requirement-considered)
4. [Version 1: Initial MVP Prototype](#Version-1)
5. [Version 2: Updated Prototype](#Version-2)
6. [Version 3: Final Prototype](#Version-3)
7. [Future Work](#future-work)

## Purpose of the Prototype
1. To communicate to stakeholders how the data collected from our garbage tracker will look like
2. To provide a basic, flexible and open-sourced platform for the stakeholders to interact with the data interpolation, and to enable further customized data analysis by the stakeholders
3. To explore different ways to utilize the data collected from the garbage tracker to better understand the garbage problem in Accra, Ghana

The prototype also provide us an opportunity to gain more understanding on the performance of the tracker. We successfully used prototype to spot issues with the tracker, such as its inaccuracy.

## Requirement Considered

A requirement for the prototype is developed based on the purpose of the prototype. The requirement is then used to guide the development of the prototype.

## Version 1
Commit: `25ab82ec3fd18da672e6050514ef96e07ee9c433`
![](https://raw.githubusercontent.com/0xC000005/ESC204/main/handbook/img_1.png)

The main features included in this version are:

- CSV data input as a String
- No filtering options
- Visualizing the movement both in a static map and an animation

The first design is simply a minimum viable product (MVP) that allows users to input a CSV string and visualize the movement of the garbage tracker. The main purpose of this version is to demonstrate the basic functionality of the app and to provide a starting point for further development. 
The idea is that this version will serve as a framework for the future development of the app. The app will be further developed to include more features and functionalities, and to improve the user experience, by simply adding more function calls to the main() function.

Since this is an MVP, we made several intentional design choice to reduce the complexity of the app. For example, we only allow users to input a CSV string, and we don't provide any filtering options. The reason is that we want to focus on the core functionality of the app, which is to visualize the movement of the garbage tracker. One of which is how to take the input csv. We decided to take the input as a string, instead of a file, because it is easier to implement. The reason is that we can simply use the st.text_input() function to take the input, so that we don't need to worry about the technical complexity of file uploading, caching, etc.

## Version 2
Commit: `25b585b293b5553ba5112f53547bb4c97e4b9c4b`
![](https://raw.githubusercontent.com/0xC000005/ESC204/main/handbook/img_2.png)

Version 2 of the website introduced additional features to enhance the user experience and provide more detailed information. The main improvements and changes in this version are:

- Added a time slider for data filtering, and live updating of the map as the slider is dragged (Failed)
- Enhanced the overall user interface by providing helper information 

In this version, we try to add more features to the app to reach the initial design requirement. The main feature added in this version is the time slider. The time slider allows users to filter the data by time, and to visualize the movement of the garbage tracker at a specific time.

The problem is that the map disappears after dragging the slider. This is because the map is rendered using pydeck, which is a Python library for creating interactive maps. The map is rendered as a static image, and the slider is implemented using Streamlit's slider widget. When the slider is dragged, the map is re-rendered, which causes the map to disappear. 
To fix this issue, the map is now rendered using folium, which require major refactoring of the code. This basically means that the version 1 of the app is no longer useful, and the app is rewritten from scratch to make version 3. 

## Version 3
Commit: `d2ffaeec5c47dad08acf694af7aa11689c34dc87`
![](https://raw.githubusercontent.com/0xC000005/ESC204/main/handbook/img_3.PNG)


Version 3 of the website focused on refining the app and ensuring it functioned smoothly. The main changes and enhancements included in this version are:

- Refactor the code to switch from pydeck to folium for map visualization, also making the code more modular and readable
- Removed the using timeslider function and live updating of the map
- Added a sidebar for uploading CSV and filtering data
  - ![](https://raw.githubusercontent.com/0xC000005/ESC204/main/handbook/img_4.PNG)
- Added a display bottom for rendering the filtered location on the map
- Added a button for downloading the example CSV file
- Calculate the statistics such as distance and velocity of the tracker
  - ![](https://raw.githubusercontent.com/0xC000005/ESC204/main/handbook/img_5.PNG)
- Changed the example CSV position

In this version, the major change is to fix the map disappearing issue by switching from pydeck to folium. We removed the using timeslider function and live updating of the map. After consideration, we think that the live updating of the map is not necessary, as it doesn't provide any additional information. Instead, we used a static update button instead. The update button allows users to update the map with the new filtering options. After user filtered the data, we simply re-render the map with the new data, which is technically way easier than live updating the map. Although visually speaking, the live updating of the map is more appealing, the technical difficulty of implementing doesn't justify it.

![Inaccurate location logged from the tracker](https://raw.githubusercontent.com/0xC000005/ESC204/main/handbook/img_6.PNG)
During our testing visualization of the GNSS data from our tracker prototype, we found that the data is not ver accurate in the sense that it is both shifted and scaled. 
We believe that this is due to the GNSS module we used, as ESC204 students from last year also reported similar issues according to a TA. To address this issue, a helper script were also developed to help calibrate the raw GNSS data by allowing horizontal, vertical, and temporal offsets to be applied to the data. The scripts were written in Python and can be found in the [adjust_gps.py](https://github.com/0xC000005/ESC204/blob/main/adjust_gps.py)

Note that this script is not part of the Streamlit app, and it is only used to calibrate the raw GNSS data. The calibrated data is then used to generate the CSV file that is uploaded to the Streamlit app. The design philosophy is that the Streamlit app should only be responsible for visualizing the data, and it should not be responsible for offsetting the data, as otherwise we created a responsibility overlap between the app and the tracker, as acquire accurate GNSS data is the responsibility of the tracker.
After using the script to manually calibrate the data, we found that the data is now accurate enough to be visualized on the map. 
![calibrated location, note that the path matches the shape of Queen's Park](https://raw.githubusercontent.com/0xC000005/ESC204/main/handbook/img_7.PNG)

## Future Work

Although after version 3, all initial design requirements are met, there are still many features that can be added to the app to further enhance the user experience. Some of the features that can be added in the future are:
- Add more filtering options, such as filtering every nth data point
- Add more visualization options, such as visualizing the signal strength and using heatmaps to visualize the density of the garbage routes
- To allow user to export the map as an image
- To allow user to export filtered data as a CSV file


