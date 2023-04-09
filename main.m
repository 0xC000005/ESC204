% Load sample garbage and case geometry data
garbage_data = load('garbage.mat'); % Replace this with your garbage geometry
case_data = load('case.mat'); % Replace this with your case geometry

% Transmitter characteristics
transmitterPowerDbm = 10; % 20 dBm transmission
transmitterGain = 2; % 2 dB antenna gain
receiverGain = 3; % 3 dB gain on reception

% Additional attenuation factors for case and garbage (unit-less)
attenuationPLA = 3; % Adjust based on the specific case material
attenuationCase = attenuationPLA * 0.01; % 1 cm case thickness
attenuationOrganic = 1;
attenuationPlastic = 2;
attenuationMetal = 10;
attenuationGlass = 5;
attenuationRandom = 3;

% Calculate overall garbage attenuation based on material percentages
attenuationGarbage = 0.69 * attenuationOrganic + 0.1 * attenuationPlastic + 0.02 * attenuationMetal + 0.02 * attenuationGlass + 0.17 * attenuationRandom;

% Create a grid of points in the 3D space
[X, Y, Z] = meshgrid(-10:1:10, -10:1:10, -10:1:10);

% Calculate the distance from the GPS tracker (located at the origin) to each point in the grid
distances = sqrt(X.^2 + Y.^2 + Z.^2);

% Calculate the signal strength at each point in the grid
signalStrength = simulateSignalStrength(transmitterPowerDbm, transmitterGain, receiverGain, distances, attenuationCase * attenuationGarbage);

% Calculate the maximum range the receiver can transmit a 40 kB csv file
maxRange = calculateMaxRange(transmitterPowerDbm, transmitterGain, receiverGain, attenuationCase * attenuationGarbage);


% Call the function with the loaded data
plotSignalStrengthSimulationWithSlider(garbage_data.garbage_geometry, case_data.case_geometry, signalStrength, maxRange);
