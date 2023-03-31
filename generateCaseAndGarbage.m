% Create a simple case geometry using an ellipsoid
[X_case, Y_case, Z_case] = ellipsoid(0, 0, 0, 5, 5, 2, 30);
case_geometry = struct('X', X_case, 'Y', Y_case, 'Z', Z_case);

% Save the case geometry to a .mat file
save('case.mat', 'case_geometry');

% Create a sphere of radius 1.8 meters
[X_garbage, Y_garbage, Z_garbage] = sphere(30);
X_garbage = 1.8 * X_garbage;
Y_garbage = 1.8 * Y_garbage;
Z_garbage = 1.8 * Z_garbage;

garbage_geometry = struct('X', X_garbage, 'Y', Y_garbage, 'Z', Z_garbage);

% Save the garbage geometry to a .mat file
save('garbage.mat', 'garbage_geometry');
