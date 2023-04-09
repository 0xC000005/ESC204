import csv
import math


def read_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data = [row for row in reader]
    return data


def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def calculate_path_distance(data):
    total_distance = 0
    # find the first valid data point
    lat1, lon1 = float(data[0][1]), float(data[0][2])
    # find the last valid data point
    lat2, lon2 = float(data[-1][1]), float(data[-1][2])
    total_distance = haversine_distance(lat1, lon1, lat2, lon2)
    return total_distance


def calculate_stretch_factor(gnss_csv, true_csv):
    gnss_data = read_csv(gnss_csv)
    true_data = read_csv(true_csv)

    gnss_total_distance = calculate_path_distance(gnss_data)
    print("GNSS total distance:", gnss_total_distance)
    true_total_distance = calculate_path_distance(true_data)
    print("True total distance:", true_total_distance)

    stretch_factor = true_total_distance / gnss_total_distance
    return stretch_factor


if __name__ == "__main__":
    gnss_csv = 'GNSS_data/calibration_processed_Streamlit.csv'
    true_csv = 'GNSS_data/calibration_processed_test.csv'
    stretch_factor = calculate_stretch_factor(gnss_csv, true_csv)
    print("Stretch factor:", stretch_factor)
