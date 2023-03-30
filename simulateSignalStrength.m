function receivedPowerDbm = simulateSignalStrength(transmitterPowerDbm, distance, attenuation)
    % Constants
    frequency = 2.4e9; % BLE frequency: 2.4 GHz
    speedOfLight = 3e8;
    wavelength = speedOfLight / frequency;

    % Transmitter and receiver characteristics
    transmitterGain = 1;
    receiverGain = 1;

    % Convert transmitter power from dBm to Watts
    transmitterPowerWatts = 10 ^ (transmitterPowerDbm / 10) / 1000;

    % Friis Transmission Formula
    receivedPowerWattsFreeSpace = (transmitterPowerWatts * transmitterGain * receiverGain * (wavelength ^ 2)) / ((4 * pi * distance) ^ 2);

    % Apply attenuation
    receivedPowerWattsAttenuated = receivedPowerWattsFreeSpace / attenuation;

    % Convert received power from Watts to dBm
    receivedPowerDbm = 10 * log10(receivedPowerWattsAttenuated * 1000);
end
