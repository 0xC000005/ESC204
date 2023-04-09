import csv
from datetime import datetime, timedelta

# Input and output file paths
input_file = 'GNSS_data/calibration_processed.csv'
output_file = 'GNSS_data/calibration_processed_Streamlit.csv'

# Starting timestamp, change as needed
starting_timestamp = datetime.strptime("2023-04-09 09:00:00", "%Y-%m-%d %H:%M:%S")

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write header to the output file
    writer.writerow(['timestamp', 'latitude', 'longitude', 'fix_status', 'HDOP', 'satellites_in_use'])

    for index, row in enumerate(reader):
        # Extract the data from the input row
        timestamp, latitude, longitude, fix_status, hdop, satellites_in_use = row

        # Convert timestamp to the desired format
        converted_timestamp = starting_timestamp + timedelta(seconds=float(timestamp))

        # Write the converted row to the output file, excluding the index
        writer.writerow([converted_timestamp, latitude, longitude, fix_status, hdop, satellites_in_use])

if __name__ == '__main__':
    pass
