# MATLAB Signal Continuity Simulation Engineering Handbook

## Table of Contents
1. [Introduction](#introduction)
2. [Version 1: Initial Signal Strength Test](#version-1-initial-signal-strength-test)
3. [Version 2: Updated Signal Strength Calculation](#version-2-updated-signal-strength-calculation)
4. [Version 3: Changed Case Geometry](#version-3-changed-case-geometry)

## Requirements Considered

A requirement for the prototype is developed based on the purpose of the prototype. The requirement is then used to guide the development of the prototype.

| Feature Name                   | Requirement                                      | Consideration                                                                                                                                                                                                                                               |
|--------------------------------|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Easy to Use                    | Easy to use for technical and non-technical users | Although the simulation is technical by nature, proper instruction with easy input and output must be implemented to allow non-technical users to use the simulation even if they have no prior experience with the simulation and don't want to change the code. |
| Geometry Handling              | Handle different geometries                      | The simulation must take into account the different geometry on the signal path and calculate the signal loss accordingly.                                                                                                                                   |
| Material Composition Handling  | Handle different material compositions           | Different materials have different signal permittivity. When calculating the signal loss, the material composition must be considered.                                                                                                                       |
| Maximum Range Calculation      | Calculate the maximum range                      | The simulation must be able to calculate the maximum range the receiver can transmit a 40 kB csv file within a specified time constraint, in order to evaluate the performance of the tracker.                                                              |
| Visualization of Geometry & Loss | Visualize geometry and signal loss             | The simulation must be able to visualize the geometry and signal loss in each direction, providing users with a clear understanding of the signal path and the impact of the geometry on the signal strength.                                                 |



## Purpose of the Prototype

The purpose of the MATLAB Signal Continuity Simulation is to provide a simulation of the signal strength of the receiver. The simulation will be used to test the signal strength of the receiver and to determine the maximum range the receiver can transmit a 40 kB csv file within a specified time constraint.
Although the simulation is not a perfect representation of the actual signal strength due to the time constraint and the fact that our team does not have RF expertise, the simulation will provide a good starting point for the development of the signal strength test in the future. We feel confident that if the constraint is removed and the simulation is improved, the simulation will be able to provide a more accurate representation of the actual signal strength, which add understanding to the performance of the tracker. 


## File Description
- `calculateMaxRange.m`: MATLAB function to calculate the maximum range the receiver can transmit a 40 kB csv file within a specified time constraint.
- `case.mat`: MATLAB binary file containing the geometry of the case.
- `example_input.csv`: Example input file with data for the simulation.
- `garbage.mat`: MATLAB binary file containing the geometry of the garbage.
- `main.m`: MATLAB script for running the signal strength simulation.
- `plotSignalStrengthSimulationWithSlider.m`: MATLAB function to plot the signal strength simulation with an interactive slider.
- `README.md`: This README file.
- `requirements.txt`: Python requirements for the Streamlit app.
- `simulateSignalStrength.m`: MATLAB function to simulate the signal strength based on the given parameters.



## Version 1: Initial Signal Strength Test
Commit: `f39900444852ca495967672158d008a318f1d88c`

### Overview
This initial version of the MATLAB Signal Continuity Simulation sets the foundation for the signal strength test. The main goal of this version is to provide a starting point for the development of the simulation. Thus, this version is designed to be a minimum viable product (MVP) that can be improved in the future.
We use MATLAB for the simulation because MATLAB is a powerful tool for signal processing and signal strength calculation. Matlab also allows 3D rotation of the plot, which is important for studying the signal decay in different directions.
A design choice was made to only focus on the plotting and the making of geometry of the case and the garbage. The signal strength calculation is not included in this version because it is not the main focus of this version. The signal strength calculation will be improved in the future versions.

#### Main Function Achieved
- Establish a basic framework for signal strength testing.
- Created the initial files and structure for the project.
- Created the initial geometry files for the case and the garbage.
- Created the initial plotting function for the signal strength simulation.

## Version 2: Updated Signal Strength Calculation
Commit: `28f266b04f1f509384a4321ceef909410f7272fa`

### Overview
![](https://raw.githubusercontent.com/0xC000005/ESC204/main/screenshot.png)
In this version, the signal strength calculation has been updated to improve the accuracy of the simulation. The main goal of this version is to provide a more reliable signal strength test.
The signal calculation, however, doesn't take into account the material composition of the case and the garbage, nor the different geometry of the case. This is because the technical difficulty of the signal strength calculation is beyond the ability of the version 1 and 2 contributor. Instead, what we did is to calculate a uniform signal permittivity, which take into account the material composition and the geometry of the case and the garbage. This is a temporary solution to the problem, and the signal strength calculation will be improved in the future versions.

#### Main Function Achieved
- Improved the signal strength calculation for better accuracy.
- Plot the geometry of the case and the garbage using surface plot.
- Plot the signal strength in different directions using scatter plot.
- Uniforming the signal permittivity of the case and the garbage.
- Change the case and the garbage geometry to be surface to be more accurate, rather than just two spheres.

## Version 3: Changed Case Geometry
Commit: `ec7254278a8b2b3bb4af3f80805467edc599b981`

### Overview
![]()
In this version, we start to consider the geometry of the case and the garbage. The main goal of this version is to provide a more accurate signal strength test by taking into account the geometry of the case and the garbage. Note that the material composition of the case and the garbage is not considered in this version. We also improve the UI of the simulation by adding a slider to allow users to change how far radius the signal strength is to be calculated and plotted. 



#### Main Function Achieved
- Adapted the simulation to handle different case geometries.
- Added a slider to the simulation to allow users to change the angle of the case.
- Change the case and the garbage geometry to be mesh instead of surface so that user can see through the case and the garbage to see the signal strength in different directions.
- Added a function to calculate the maximum range the receiver can transmit a 40 kB csv file within a specified time constraint.



## Future Work
- Improve the signal strength calculation to take into account the material composition of the case and the garbage.
- Improve the signal strength calculation to take into account the different geometry of the case and the garbage.
- Improve the UI of the simulation by adding more features.
- Improve the simulation by adding more features.
