import sys
import csv


def adjust_gps(input_file, output_file, correct_latitude, correct_longitude, factor):
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        data = [row for row in reader]
    original_latitude = float(data[0][1])
    original_longitude = float(data[0][2])

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for row in data:
            latitude = float(row[1])
            longitude = float(row[2])

            # Calculate the stretched latitude and longitude
            adjusted_latitude = correct_latitude + (latitude - original_latitude) * factor
            adjusted_longitude = correct_longitude + (longitude - original_longitude) * factor

            writer.writerow([row[0], adjusted_latitude, adjusted_longitude] + row[3:])


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python adjust_gps.py input_file output_file correct_latitude correct_longitude factor")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        correct_latitude = float(sys.argv[3])
        correct_longitude = float(sys.argv[4])
        factor = float(sys.argv[5])

        adjust_gps(input_file, output_file, correct_latitude, correct_longitude, factor)
