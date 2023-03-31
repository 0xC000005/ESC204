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
        title(ax, sprintf('Signal Strength (dBm) at Radius %.2f, Max Range: %.2f m', radius, maxRange));
        rotate3d(ax, 'on');

        % Plot the case and garbage objects (assuming they are mesh objects)
        hold(ax, 'on');
        case_mesh = mesh(ax, case_geometry.X, case_geometry.Y, case_geometry.Z); % Replace 'case' with the variable containing the case geometry
        case_mesh.FaceAlpha = 0.1; % Adjust transparency
        case_mesh.FaceColor = [0, 0, 1];
        case_mesh.EdgeColor = 'k';

        garbage_mesh = mesh(ax, garbage_geometry.X, garbage_geometry.Y, garbage_geometry.Z); % Replace 'garbage' with the variable containing the garbage geometry
        garbage_mesh.FaceAlpha = 0.1; % Adjust transparency
        garbage_mesh.FaceColor = [1, 0, 0];
        garbage_mesh.EdgeColor = 'k';

        % Create a dedicated legend
        legend(ax, [case_mesh, garbage_mesh], {'Case', 'Garbage'}, 'Location', 'best');

        hold(ax, 'off');
    end