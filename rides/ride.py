class Ride:
    def __init__(self, line: str):
        int_line = [int(i) for i in line.split()]
        self.row_start, self.col_start, self.row_fin, self.col_fin, self.early_start, self.late_fin = int_line

    def get_row_start(self):
        return self.row_start

    def get_column_start(self):
        return self.col_start

    def get_row_finish(self):
        return self.row_fin

    def get_earliest_start(self):
        return self.early_start

    def get_latest_finish(self):
        return self.late_fin
