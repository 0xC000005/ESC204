import sys
import csv

def adjust_gps(input_file, output_file, correct_latitude, correct_longitude):
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        data = [row for row in reader]

    original_latitude = float(data[0][1]) # Change this to 1
    original_longitude = float(data[0][2]) # Change this to 2

    lat_diff = correct_latitude - original_latitude
    lon_diff = correct_longitude - original_longitude

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for row in data:
            adjusted_latitude = float(row[1]) + lat_diff # Change this to 1
            adjusted_longitude = float(row[2]) + lon_diff # Change this to 2
            writer.writerow([row[0], adjusted_latitude, adjusted_longitude] + row[3:])

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python adjust_gps.py input_file output_file correct_latitude correct_longitude")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        correct_latitude = float(sys.argv[3])
        correct_longitude = float(sys.argv[4])

        adjust_gps(input_file, output_file, correct_latitude, correct_longitude)
