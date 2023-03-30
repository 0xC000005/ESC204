% Load sample garbage and case geometry data
garbage_data = load('garbage.mat'); % Replace this with your garbage geometry
case_data = load('case.mat'); % Replace this with your case geometry

% Call the function with the loaded data
plotSignalStrengthSimulationWithSlider(garbage_data.garbage_geometry, case_data.case_geometry);
