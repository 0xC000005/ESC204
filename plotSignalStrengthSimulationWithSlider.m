function plotSignalStrengthSimulationWithSlider(garbage_geometry, case_geometry)
    % Load sample garbage and case geometry data
    load('garbage.mat'); % Replace this with your garbage geometry
    load('case.mat'); % Replace this with your case geometry

    % Transmitter characteristics
    transmitterPowerDbm = 20; % 20 dBm transmission
    transmitterGain = 10; % 10 dB antenna gain
    receiverGain = 20; % 20 dB gain on reception

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

    % Create a figure for the 3D signal strength plot
    fig = figure;
    ax = axes(fig);

    % Create a UI slider to control the radius
    slider = uicontrol('Style', 'slider', 'Min', 0, 'Max', 10, 'Value', 0, 'Position', [150 20 300 20], 'Callback', @updatePlot);

    % Initialize the plot
    updatePlot();

    % Function to update the plot based on the slider value
    function updatePlot(~, ~)
        radius = slider.Value;

        % Filter the signal strength data based on the current radius
        mask = distances >= radius & distances < (radius + 1);

        % Clear the current plot
        cla(ax);

        % Plot the filtered signal strength data
        scatter3(ax, X(mask), Y(mask), Z(mask), 30, signalStrength(mask), 'filled');
        colorbar;
        axis(ax, 'equal');
        xlabel(ax, 'X');
        ylabel(ax, 'Y');
        zlabel(ax, 'Z');
        title(ax, sprintf('Signal Strength (dBm) at Radius %.2f', radius));
        rotate3d(ax, 'on');

        % Plot the case and garbage objects (assuming they are surface objects)
        hold(ax, 'on');
        surf(ax, case_geometry.X, case_geometry.Y, case_geometry.Z); % Replace 'case' with the variable containing the case geometry
        surf(ax, garbage_geometry.X, garbage_geometry.Y, garbage_geometry.Z); % Replace 'garbage' with the variable containing the garbage geometry
        hold(ax, 'off');
    end
end
