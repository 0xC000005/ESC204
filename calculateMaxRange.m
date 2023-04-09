% Function to calculate the maximum range the receiver can transmit a 40 kB csv file in 2 minutes
function maxRange = calculateMaxRange(transmitterPowerDbm, transmitterGain, receiverGain, attenuation)
    pSens = -100;
    pNoise = 10;

    % Bluetooth frequency (Hz)
    frequency = 2.45e9; % 2.45 GHz
    c = 2.998e8;

    %Pathloss
    numFactors = transmitterGain + receiverGain - attenutation - pSens - pNoise;
    
    denumFactors = (4*pi*frequency/c)^2;
    
    k = (10^(numFactors/10))/denumFactors;

    % Calculate the maximum range based on the path loss and attenutation
    maxRange = sqrt(k*pT);
end
