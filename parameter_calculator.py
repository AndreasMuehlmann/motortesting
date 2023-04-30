import time

from csv_writer import Csv_Writer
from voltage_function_modes import Voltage_Function_Modes


class Parameter_Calculator:
    def __init__(self):
        self.csv_writer = Csv_Writer('parameters.csv', ['iteration',
                                                        'max_rpm',
                                                        'total_rotations_in_Inc*(10^-1)'])
        self.iterations = 0
        self.last_calculation = time.time()
        self.first_mode = Voltage_Function_Modes.Low
        self.previous_voltage_function_mode = Voltage_Function_Modes.Low
        self._reset_values()

    def calculate_parameters(self, rpm, filtered_rpm, voltage_function_mode):
        if voltage_function_mode == Voltage_Function_Modes.Low and \
                self.previous_voltage_function_mode != Voltage_Function_Modes.Low:
            self.iterations += 1
            self.csv_writer.add_line_of_data([
                self.iterations,
                self.max_rpm,
                self.total_rotations * 10**-1,
                ])
            self._reset_values()
        self._calculate_tmp_values(rpm, filtered_rpm, voltage_function_mode)
        self.last_calculation = time.time()
        self.previous_voltage_function_mode = voltage_function_mode

    def _calculate_tmp_values(self, rpm, filtered_rpm, voltage_function_mode):
        self.max_rpm = max(self.max_rpm, filtered_rpm)
        if voltage_function_mode == Voltage_Function_Modes.Inc:
            self.total_rotations += rpm * (time.time() - self.last_calculation) * 60

    def _reset_values(self):
        self.max_rpm = 0
        self.total_rotations = 0
