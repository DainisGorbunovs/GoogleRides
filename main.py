import sys
from rides import City, Vehicle, Ride


if len(sys.argv) < 2:
    exit("Missing data input file.")

city = City(sys.argv[1])
print("Parsed {} rides from {} input file.".format(city.get_ride_count(), sys.argv[1]))
rides = city.get_rides()


print("Done")
