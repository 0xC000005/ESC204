% Function to calculate the maximum range the receiver can transmit a 40 kB csv file in 2 minutes
function maxRange = calculateMaxRange(transmitterPowerDbm, transmitterGain, receiverGain, attenuation)
    % Calculate required data rate (bits per second) for a 40 kB csv file in 2 minutes
    fileSizeBytes = 40 * 1024; % 40 kB
    transferTimeSeconds = 2 * 60; % 2 minutes
    requiredDataRateBps = (fileSizeBytes * 8) / transferTimeSeconds;

    % The required signal strength for a successful transmission (dBm) at 1 Mbps data rate
    requiredSignalStrengthDbm = -90;

    % Adjust the required signal strength for the actual data rate
    requiredSignalStrengthDbm = requiredSignalStrengthDbm - 10 * log10(1e6 / requiredDataRateBps);

    % Bluetooth frequency (Hz)
    frequency = 2.45e9; % 2.45 GHz

    % Path loss exponent
    n = 3;

    % Calculate the path loss using the link budget formula and path loss model
    pathLoss = transmitterPowerDbm + transmitterGain + receiverGain - requiredSignalStrengthDbm - attenuation;

    % Calculate the maximum range based on the path loss, frequency, and path loss exponent
    maxRange = 10^((pathLoss + 147.55 - 20 * log10(frequency) - 10 * n * log10(10)) / (20 + 10 * n));
end
