from rides import Ride, Vehicle


class City:
    def __init__(self, file: str):
        self.score = 0
        self.rides = []
        self.vehicles = []

        with open(file, 'rb') as f:
            self.row_count, self.col_count, self.vehicle_count, \
                self.ride_count, self.ride_bonus, self.step_count\
                = [int(i) for i in f.readline().split()]
            self.add_rides_from_file(f)

        self.add_vehicles()
        self.output = ''

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
            self.rides.append(Ride(line.decode(), len(self.rides)))

    def get_rides(self) -> list:
        return self.rides

    def add_vehicles(self):
        for vehicle in range(self.get_vehicle_count()):
            self.vehicles.append(Vehicle())

    def get_score(self) -> int:
        return self.score

    def assign_rides_to_vehicles(self):
        while len(self.rides) > 0:
            for vehicle in self.vehicles:
                self.assign_nearest_ride_to_vehicle(vehicle)
                ride = vehicle.get_ride()

                # if arrives early, then need to wait
                if vehicle.get_step() < ride.get_earliest_start():
                    vehicle.set_step(ride.get_earliest_start())

                ride_score = self.get_ride_score(vehicle.get_ride(), 0, ride.get_path_distance())
                vehicle.set_position((ride.get_row_finish(), ride.get_column_finish()))
                vehicle.set_step(vehicle.get_step() + ride.get_path_distance())

                if vehicle.get_step() >= self.get_step_count():
                    self.output += str(len(vehicle.ride_ids)) + ' ' + ' '.join([str(i) for i in vehicle.ride_ids]) + '\n'
                    self.vehicles.remove(vehicle)
                self.score += ride_score

                if len(self.rides) <= 0:
                    for vehicle in self.vehicles:
                        self.output += str(len(vehicle.ride_ids)) + ' ' + ' '.join([str(i) for i in vehicle.ride_ids]) + '\n'
                    return

    def assign_nearest_ride_to_vehicle(self, vehicle: Vehicle):
        nearest_ride = None
        shortest_distance = None
        for ride in self.rides:
            distance_to_ride = vehicle.get_distance_to_ride_start(ride)
            if shortest_distance is None or distance_to_ride < shortest_distance:
                shortest_distance = distance_to_ride
                nearest_ride = ride

        vehicle.set_ride(nearest_ride)
        self.rides.remove(nearest_ride)

    def get_ride_score(self, ride: Ride, actual_start_time: int, actual_finish_time: int):
        bonus = self.get_ride_bonus() if ride.award_bonus(actual_start_time, actual_finish_time) else 0
        ride_score = ride.get_ride_points() + bonus
        return ride_score

    def get_output(self):
        return self.output