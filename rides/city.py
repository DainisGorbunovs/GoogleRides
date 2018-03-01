from rides import Ride


class City:
    def __init__(self, line: str):
        self.row_count, self.col_count, self.vehicle_count,\
            self.ride_count, self.ride_bonus, self.step_count = [int(i) for i in line.split()]

        self.rides = []

    def get_row_count(self):
        return self.row_count

    def get_column_count(self):
        return self.col_count

    def get_vehicle_count(self):
        return self.vehicle_count

    def get_ride_count(self):
        return self.ride_count

    def get_ride_bonus(self):
        return self.ride_bonus

    def get_step_count(self):
        return self.step_count

    def add_rides_from_file(self, f):
        for line in f:
            self.rides.append(Ride(line.decode()))

    def get_rides(self):
        return self.rides

    def next_ride(self):
        pass

    def find_score(self):
        pass
