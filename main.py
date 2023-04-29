import traceback
import time
from csv_writer import Csv_Writer
from fir_filter import Fir_Filter
from iir_filter import Iir_Filter
from serial_interface import Serial_Interface
from voltage_function import Voltage_Function


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
        self.serial_interface.flush()
        self.prev_measurements = [0, 0]
        self.start_time = time.time()

    def run(self):
        while True:
            try:
                measurements = self.serial_interface.recv()
                measurements = [float(measurement) for measurement in measurements]
                self.prev_measurements = measurements

            except (UnicodeDecodeError, ValueError):
                measurements = self.prev_measurements
            rpm, measured_voltage = measurements
            voltage = self.voltage_function.give_current_voltage()
            self.serial_interface.send(voltage)

            filtered_rpm = self.digital_filter.give_filtered(rpm)
            self.csv_writer.add_line_of_data(
                    [time.time() - self.start_time,
                     rpm,
                     filtered_rpm,
                     measured_voltage * 5000 / 1023,
                     voltage * 5000 / 255]
                    )
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
