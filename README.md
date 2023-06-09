# ESC204 Signal Strength Simulation Project

This project aims to simulate the signal strength of a Bluetooth Low Energy (BLE) device inside a garbage and case setup. The simulation takes into account the attenuation due to the case and garbage materials.

The project also includes a Streamlit app for visualizing the GNSS GPS log csv file.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://0xc000005-esc204-streamlit-app-kq3yff.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


![Simulation Screenshot](https://raw.githubusercontent.com/0xC000005/ESC204/main/screenshot.png)
![Website Screenshot](https://raw.githubusercontent.com/0xC000005/ESC204/main/screenshot2.png)
## File Structure

```angular2html
.
├── .idea
├── GNSS_data
├── handbook
├── venv
├── adjust_gps.py
├── calculateMaxRange.m
├── calculateStretchFactor.py
├── case.mat
├── convertL76xToStreamlitFormat.py
├── Engineering_Handbook_Signal_Simulation.md
├── Engineering_Handbook_Streamlit.md
├── example_input.csv
├── garbage.mat
├── generateCaseAndGarbage.m
├── main.m
├── plotSignalStrengthSimulationWithSlider.m
├── README.md
├── requirements.txt
├── screenshot.png
├── screenshot2.png
├── simulateSignalStrength.m
├── streamlit_app.py
└── updatePlot.m
```



## Files and Path Description

- `adjust_gps.py`: Python script for shifting and stretching the GNSS GPS path log.
- `calculateMaxRange.m`: MATLAB function to calculate the maximum range the receiver can transmit a 40 kB csv file within a specified time constraint.
- `calculateStretchFactor.py`: Python script to calculate the stretch factor between GNSS GPS path log and the true path.
- `case.mat`: MATLAB binary file containing the geometry of the case.
- `convertL76xToStreamlitFormat.py`: Python script for converting the L76x format GNSS GPS path log to a Streamlit compatible format.
- `Engineering_Handbook_Signal_Simulation.md`: Markdown file for the Engineering Handbook for Signal Simulation.
- `Engineering_Handbook_Streamlit.md`: Markdown file for the Engineering Handbook for Streamlit app.
- `example_input.csv`: Example input file with data for the simulation.
- `garbage.mat`: MATLAB binary file containing the geometry of the garbage.
- `generateCaseAndGarbage.m`: MATLAB script to generate case and garbage geometry.
- `main.m`: MATLAB script for running the signal strength simulation.
- `plotSignalStrengthSimulationWithSlider.m`: MATLAB function to plot the signal strength simulation with an interactive slider.
- `README.md`: This README file.
- `requirements.txt`: Python requirements for the Streamlit app.
- `screenshot.png`: Screenshot of the signal strength simulation.
- `screenshot2.png`: Screenshot of the Streamlit app.
- `simulateSignalStrength.m`: MATLAB function to simulate the signal strength based on the given parameters.
- `streamlit_app.py`: Python script for the Streamlit app visualization of the GNSS GPU log csv file.
- `updatePlot.m`: MATLAB function to update the plot of the signal strength simulation.
- `GNSS_data`: Folder containing the GNSS GPS log csv files.
- `handbook`: Folder containing the artifacts for the Engineering Handbooks.
1. Clone the repository.
2. Install Python dependencies using `pip install -r requirements.txt`.
3. Run the MATLAB scripts in the MATLAB environment.

## Usage

1. Run the `main.m` script in MATLAB to perform the signal strength simulation. This script uses the provided geometry files (`case.mat` and `garbage.mat`) and the signal strength simulation functions to generate a 3D plot of the signal strength within the garbage and case setup.

2. Run the Streamlit app using `streamlit run streamlit_app.py` to visualize the simulation results. The Streamlit app provides an interactive visualization of the tracker movement data. You can also directly access the GNSS tool here: https://0xc000005-esc204-streamlit-app-kq3yff.streamlit.app/

3. Run the `python adjust_gps.py input_file output_file correct_latitude correct_longitude factor` script to adjust the GNSS GPS path log. This script takes in the GNSS GPS path log csv file and the stretch factor as input and outputs a new csv file with the adjusted path.

4. Run the `convertL76xToStreamlitFormat.py` script to convert the L76x format GNSS GPS path log to a Streamlit compatible format. This script takes in the L76x format GNSS GPS path log csv file and outputs a new csv file with the adjusted path. 

5. Run the `calculateStretchFactor.py` script to calculate the stretch factor between GNSS GPS path log and the true path. This script takes in the GNSS GPS path log csv file and the true path csv file as input and outputs the stretch factor.


## Contributing

To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them to your branch.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

Please ensure that your code follows the project's coding standards and that you have tested your changes before submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
