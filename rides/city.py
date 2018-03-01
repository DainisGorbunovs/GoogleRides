from rides import Ride, Vehicle


class City:
    def __init__(self, file: str):
        self.rides = []
        self.vehicles = []

        with open(file, 'rb') as f:
            self.row_count, self.col_count, self.vehicle_count, \
                self.ride_count, self.ride_bonus, self.step_count\
                = [int(i) for i in f.readline().split()]
            self.add_rides_from_file(f)

        self.add_vehicles()

    def get_row_count(self) -> int:
        return self.row_count

    def get_column_count(self) -> int:
        return self.col_count

    def get_vehicle_count(self) -> int:
        return self.vehicle_count

    def get_ride_count(self) -> int:
        return self.ride_count

    def get_ride_bonus(self) -> int:
        return self.ride_bonus

    def get_step_count(self) -> int:
        return self.step_count

    def add_rides_from_file(self, f):
        for line in f:
            self.rides.append(Ride(line.decode()))

    def get_rides(self) -> list:
        return self.rides

    def add_vehicles(self):
        for vehicle in range(self.get_vehicle_count()):
            self.vehicles.append(Vehicle())

    def next_ride(self):
        pass

    def find_score(self):
        pass
