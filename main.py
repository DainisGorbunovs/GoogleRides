import sys
from rides import *


if len(sys.argv) < 2:
    exit("Missing data input file.")

with open(sys.argv[1], 'rb') as f:
    city = City(f.readline().decode())
    city.add_rides_from_file(f)

print("Parsed {} rides from {} input file.".format(city.get_ride_count(), sys.argv[1]))
