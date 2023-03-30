% Create a simple case geometry using an ellipsoid
[X_case, Y_case, Z_case] = ellipsoid(0, 0, 0, 5, 5, 2, 30);
case_geometry = struct('X', X_case, 'Y', Y_case, 'Z', Z_case);

% Save the case geometry to a .mat file
save('case.mat', 'case_geometry');

% Create simple garbage geometry using spheres
[X_garbage1, Y_garbage1, Z_garbage1] = sphere(30);
X_garbage1 = 3 * X_garbage1 + 3;
Y_garbage1 = 3 * Y_garbage1 + 3;
Z_garbage1 = 3 * Z_garbage1;

[X_garbage2, Y_garbage2, Z_garbage2] = sphere(30);
X_garbage2 = 3 * X_garbage2 - 3;
Y_garbage2 = 3 * Y_garbage2 - 3;
Z_garbage2 = 3 * Z_garbage2;

garbage_geometry = struct('X1', X_garbage1, 'Y1', Y_garbage1, 'Z1', Z_garbage1, ...
                          'X2', X_garbage2, 'Y2', Y_garbage2, 'Z2', Z_garbage2);

% Save the garbage geometry to a .mat file
save('garbage.mat', 'garbage_geometry');
