from rides import Ride


class Vehicle:
    def __init__(self, position=(0,0), current_step=0, current_ride=None):
        self.row_position, self.col_position = position
        self.current_ride = current_ride
        self.current_step = current_step

    def get_ride(self):
        return self.current_ride

    def set_ride(self, ride: Ride):
        self.current_ride = ride

    def set_position(self, position: tuple):
        self.row_position, self.col_position = position

    def get_position(self):
        return self.row_position, self.col_position

