from rides import Ride


class Vehicle:
    def __init__(self, position=(0,0), current_step=0, current_ride=None):
        self.row_position, self.col_position = position
        self.current_ride = current_ride
        self.current_step = current_step
        self.ride_ids = []

    def get_ride(self) -> Ride:
        return self.current_ride

    def set_ride(self, ride: Ride):
        self.current_ride = ride
        self.ride_ids.append(ride.get_ride_id())

    def get_step(self) -> int:
        return self.current_step

    def set_step(self, step: int):
        self.current_step = step

    def set_position(self, position: tuple):
        self.row_position, self.col_position = position

    def get_position(self) -> tuple:
        return self.row_position, self.col_position

    def get_distance_to_ride_start(self, ride: Ride):
        return abs(ride.get_row_start() - self.row_position) + abs(ride.get_column_start() - self.col_position)
