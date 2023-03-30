% Load sample garbage and case geometry data
load('garbage.mat'); % Replace this with your garbage geometry
load('case.mat'); % Replace this with your case geometry

% Transmitter characteristics
transmitterPowerDbm = 4; % BLE transmitter power in dBm (typical value is 0 to 10 dBm)

% Additional attenuation factor for case or garbage (unit-less)
attenuationCase = 3; % Adjust based on the specific case material
attenuationGarbage = 5; % Adjust based on the specific garbage material

% Create a grid of points in the 3D space
[X, Y, Z] = meshgrid(-10:1:10, -10:1:10, -10:1:10);

% Calculate the distance from the GPS tracker (located at the origin) to each point in the grid
distances = sqrt(X.^2 + Y.^2 + Z.^2);

% Calculate the signal strength at each point in the grid
signalStrength = simulateSignalStrength(transmitterPowerDbm, distances, attenuationCase * attenuationGarbage);

% Plot the 3D signal strength
figure;
scatter3(X(:), Y(:), Z(:), 30, signalStrength(:), 'filled');
colorbar;
axis equal;
xlabel('X');
ylabel('Y');
zlabel('Z');
title('Signal Strength (dBm)');
rotate3d on;

% Plot the case and garbage objects (assuming they are surface objects)
hold on;
surf(case_geometry); % Replace 'case' with the variable containing the case geometry
surf(garbage_geometry); % Replace 'garbage' with the variable containing the garbage geometry
hold off;
