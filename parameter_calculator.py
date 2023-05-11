import time

from csv_writer import Csv_Writer


class Parameter_Calculator:
    def __init__(self):
        self.csv_writer = Csv_Writer('parameters.csv', ['iteration',
                                                        'max_rpm',
                                                        'total_rotations'])
        self.last_calculation = time.time()
        self.iterations = 0
        self.max_rpm = 0
        self.total_rotations = 0

    def calculate_parameters(self, rpm):
        self.max_rpm = max(self.max_rpm, rpm)
        self.total_rotations += rpm * (time.time() - self.last_calculation) / 60
        self.last_calculation = time.time()

    def reset(self):
        self.iterations += 1
        self.csv_writer.add_line_of_data([
            self.iterations,
            self.max_rpm,
            self.total_rotations
            ])
        self.max_rpm = 0
        self.total_rotations = 0
