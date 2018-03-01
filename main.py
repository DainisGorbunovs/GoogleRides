import sys
from rides import City, Vehicle, Ride


if len(sys.argv) < 2:
    exit("Missing data input file.")

city = City(sys.argv[1])
print("Parsed {} rides from {} input file.".format(city.get_ride_count(), sys.argv[1]))
city.assign_rides_to_vehicles()
print("Basic simulation has a score of {}.".format(city.get_score()))

print(city.get_output())
city.save_output(sys.argv[1])

print("Done")
