# ESC204 Signal Strength Simulation Project

This project aims to simulate the signal strength of a Bluetooth Low Energy (BLE) device inside a garbage and case setup. The simulation takes into account the attenuation due to the case and garbage materials.



## File Structure

```angular2html
.
├── .idea
├── venv
├── calculateMaxRange.m
├── case.mat
├── example_input.csv
├── garbage.mat
├── main.m
├── plotSignalStrengthSimulationWithSlider.m
├── README.md
├── requirements.txt
├── simulateSignalStrength.m
└── streamlit_app.py
```


## Files Description

- `calculateMaxRange.m`: MATLAB function to calculate the maximum range the receiver can transmit a 40 kB csv file within a specified time constraint.
- `case.mat`: MATLAB binary file containing the geometry of the case.
- `example_input.csv`: Example input file with data for the simulation.
- `garbage.mat`: MATLAB binary file containing the geometry of the garbage.
- `main.m`: MATLAB script for running the signal strength simulation.
- `plotSignalStrengthSimulationWithSlider.m`: MATLAB function to plot the signal strength simulation with an interactive slider.
- `README.md`: This README file.
- `requirements.txt`: Python requirements for the Streamlit app.
- `simulateSignalStrength.m`: MATLAB function to simulate the signal strength based on the given parameters.
- `streamlit_app.py`: Python script for the Streamlit app visualization of the GNSS GPU log csv file .

## Installation

1. Clone the repository.
2. Install Python dependencies using `pip install -r requirements.txt`.
3. Run the MATLAB scripts in the MATLAB environment.

## Usage

1. Run the `main.m` script in MATLAB to perform the signal strength simulation. This script uses the provided geometry files (`case.mat` and `garbage.mat`) and the signal strength simulation functions to generate a 3D plot of the signal strength within the garbage and case setup.

2. Run the Streamlit app using `streamlit run streamlit_app.py` to visualize the simulation results. The Streamlit app provides an interactive visualization of the tracker movement data. You can also directly access the GNSS tool here: https://0xc000005-esc204-streamlit-app-kq3yff.streamlit.app/

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

