function receivedPowerDbm = simulateSignalStrength(transmitterPowerDbm, transmitterGain, receiverGain, distances, attenuationFactors)
    % Constants
    speedOfLight = 2.998e8; % Speed of light in meters/second
    frequency = 2.45e9; % L1 GPS frequency in Hz
    wavelength = speedOfLight / frequency;

    % Convert transmitter power to milliwatts
    transmitterPowerMWatts = 10^(transmitterPowerDbm / 10);

    % Calculate the received power in watts using the free space path loss formula
    receivedPowerMWattsFreeSpace = (transmitterPowerWatts * (10^(transmitterGain / 10)) * (10^(receiverGain / 10)) * (wavelength .^ 2)) ./ ((4 * pi * distances) .^ 2);

    % Apply attenuation factor
    receivedPowerWatts = receivedPowerWattsFreeSpace .* attenuationFactors;

    % Convert received power back to dBm
    receivedPowerDbm = 10 * log10(receivedPowerWatts);
end
