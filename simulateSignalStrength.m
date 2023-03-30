function receivedPowerDbm = simulateSignalStrength(transmitterPowerDbm, transmitterGain, receiverGain, distances, attenuationFactors)
    % Constants
    speedOfLight = 3e8; % Speed of light in meters/second
    frequency = 1575.42e6; % L1 GPS frequency in Hz
    wavelength = speedOfLight / frequency;

    % Convert transmitter power to watts
    transmitterPowerWatts = 10^((transmitterPowerDbm - 30) / 10);

    % Calculate the received power in watts using the free space path loss formula
    receivedPowerWattsFreeSpace = (transmitterPowerWatts * (10^(transmitterGain / 10)) * (10^(receiverGain / 10)) * (wavelength .^ 2)) ./ ((4 * pi * distances) .^ 2);

    % Apply attenuation factor
    receivedPowerWatts = receivedPowerWattsFreeSpace .* attenuationFactors;

    % Convert received power back to dBm
    receivedPowerDbm = 10 * log10(receivedPowerWatts) + 30;
end
