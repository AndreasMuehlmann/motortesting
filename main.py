import traceback
import time
from csv_writer import Csv_Writer
from iir_filter import Iir_Filter
from serial_interface import Serial_Interface
from voltage_function import Voltage_Function
from parameter_calculator import Parameter_Calculator


class Motor_Testing:
    def __init__(self):
        self.digital_filter = Iir_Filter(0.7, 5)
        self.csv_writer = Csv_Writer('data.csv', ['time',
                                                  'rpm',
                                                  'filtered_rpm',
                                                  'measured_voltage*10^-3',
                                                  'voltage*10^-3'])
        self.voltage_function = Voltage_Function()
        self.serial_interface = Serial_Interface()
        self.parameter_calculator = Parameter_Calculator()
        self.start_time = time.time()
        self.time = 0

    def run(self):
        while True:
            rpm, measured_voltage = self.serial_interface.give_measurements()
            voltage = self.voltage_function.give_current_voltage()
            self.serial_interface.send(voltage)
            filtered_rpm = self.digital_filter.give_filtered(rpm)
            self.time = time.time() - self.start_time
            self.csv_writer.add_line_of_data([
                self.time,
                rpm,
                filtered_rpm,
                measured_voltage * 5000 / 1023,
                voltage * 5000 / 255,
                ])
            self.parameter_calculator.calculate_parameters(rpm, self.voltage_function.mode)
            time.sleep(0.005)

    def reset(self):
        self.serial_interface.reset()


if __name__ == '__main__':
    try:
        motor_testing = Motor_Testing()
        motor_testing.run()
    except KeyboardInterrupt:
        motor_testing.reset()
    except Exception:
        motor_testing.reset()
        print(traceback.format_exc())
