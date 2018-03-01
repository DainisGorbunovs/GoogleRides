class Ride:
    def __init__(self, line: str):
        int_line = [int(i) for i in line.split()]
        self.row_start, self.col_start, self.row_fin, self.col_fin, self.early_start, self.late_fin = int_line

        # use Manhattan distance
        self.path_distance = abs(self.get_row_finish() - self.get_row_start()) \
            + abs(self.get_column_finish() - self.get_column_start())

    def get_row_start(self) -> int:
        return self.row_start

    def get_column_start(self) -> int:
        return self.col_start

    def get_row_finish(self) -> int:
        return self.row_fin

    def get_column_finish(self) -> int:
        return self.col_fin

    def get_earliest_start(self) -> int:
        return self.early_start

    def get_latest_finish(self) -> int:
        return self.late_fin

    def get_path_distance(self) -> int:
        return self.path_distance

    def get_ride_points(self) -> int:
        # an alias to get_path_distance
        return self.get_path_distance()

    def award_bonus(self, actual_start_time, actual_end_time) -> bool:
        # award bonus if picked up passenger on time (or before and waited)
        # AND arrived at the destination before or on time
        return actual_start_time <= self.get_earliest_start() and actual_end_time <= self.get_latest_finish()
