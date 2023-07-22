import traceback
import time
from datetime import datetime, timedelta, timezone
import os

import config as conf
from csv_writer import Csv_Writer
from serial_interface import Serial_Interface
from parameter_calculator import Parameter_Calculator
from csv_to_excel import csv_to_excel


class Motor_Testing:
    def __init__(self):
        self.csv_writer = Csv_Writer('data.csv', ['time_in_s',
                                                  'rpm',
                                                  'measured_voltage_in_V*10^3',
                                                  'voltage_in_V*10^3',
                                                  'current_in_A*10^4'])
        self.voltage_scheduler = conf.voltage_scheduler
        self.serial_interface = Serial_Interface()
        self.parameter_calculator = Parameter_Calculator()
        self.start_time = time.time()
        self.time = 0
        self.iterations = 0

    def run(self):
        while True:
            rpm, measured_voltage, measured_amps = self.serial_interface.give_measurements()
            voltage = self.voltage_scheduler.give_current_voltage()
            self.serial_interface.send(voltage)
            self.time = time.time() - self.start_time
            self.csv_writer.add_line_of_data([
                round(self.time, 2),
                int(rpm),
                int(measured_voltage * 5000 / 1023),
                int(voltage * 5000 / 255),
                int(measured_amps * 50000 / 1023),
                ])
            if self.voltage_scheduler.was_reset:
                self.voltage_scheduler.was_reset = False
                self.parameter_calculator.reset()
                self.iterations += 1
            self.parameter_calculator.calculate_parameters(rpm)
            if self.iterations >= conf.repetitions:
                self.reset()
                return
            time.sleep(0.05)

    def reset(self):
        self.serial_interface.reset()
        turn_off_serial_interface = Serial_Interface()
        turn_off_serial_interface.send(0)
        turn_off_serial_interface.reset()
        german_datetime = datetime.now()
        time_string = german_datetime.strftime("%Y%m%d-%H%M%S")
        csv_to_excel('data.csv', os.path.join('test_data', f'data{time_string}.xlsx'))
        csv_to_excel('parameters.csv', os.path.join('test_data', f'parameters{time_string}.xlsx'))


if __name__ == '__main__':
    try:
        motor_testing = Motor_Testing()
        motor_testing.run()
    except KeyboardInterrupt:
        motor_testing.reset()
    except Exception:
        motor_testing.reset()
        print(traceback.format_exc())
