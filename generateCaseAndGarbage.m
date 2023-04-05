% Create a simple case geometry using a box (dimensions in meters)
x_length = 0.08;
y_length = 0.12; 
z_length = 0.04;

vertices = [-x_length/2, -y_length/2, -z_length/2;
             x_length/2, -y_length/2, -z_length/2;
             x_length/2,  y_length/2, -z_length/2;
            -x_length/2,  y_length/2, -z_length/2;
            -x_length/2, -y_length/2,  z_length/2;
             x_length/2, -y_length/2,  z_length/2;
             x_length/2,  y_length/2,  z_length/2;
            -x_length/2,  y_length/2,  z_length/2];
          
faces = [1, 2, 3, 4;
         5, 6, 7, 8;
         1, 2, 6, 5;
         3, 4, 8, 7;
         1, 4, 8, 5;
         2, 3, 7, 6];

case_geometry = struct('vertices', vertices, 'faces', faces);

% Save the case geometry to a .mat file
save('case.mat', 'case_geometry');

% Create a sphere of radius 1.0 meters
[X_garbage, Y_garbage, Z_garbage] = sphere(30);
X_garbage = 1.0 * X_garbage;
Y_garbage = 1.0 * Y_garbage;
Z_garbage = 1.0 * Z_garbage;

garbage_geometry = struct('X', X_garbage, 'Y', Y_garbage, 'Z', Z_garbage);

% Save the garbage geometry to a .mat file
save('garbage.mat', 'garbage_geometry');
