import time
from csv_writer import Csv_Writer
from fir_filter import Fir_Filter
from serial_interface import Serial_Interface
from voltage_function import Voltage_Function


class Motor_Testing:
    def __init__(self):
        self.digital_filter = Fir_Filter()
        self.csv_writer = Csv_Writer('data.csv', ['time', 'rpm', 'filtered_rpm', 'voltage'])
        self.voltage_function = Voltage_Function()
        self.serial_interface = Serial_Interface()
        self.serial_interface.flush()
        self.prev_measurement = 0
        self.start_time = time.time()

    def run(self):
        while True:
            try:
                measurement = self.serial_interface.recv()
                measurement = float(measurement)
                prev_measurement = measurement

            except (UnicodeDecodeError, ValueError):
                measurement = prev_measurement
            voltage = self.voltage_function.give_current_voltage()
            self.serial_interface.send(voltage)

            filtered_measruement = self.digital_filter.give_filtered(measurement)
            self.csv_writer.add_line_of_data(
                    [time.time() - self.start_time, measurement,
                     filtered_measruement, voltage * 500 / 255]
                    )
            time.sleep(0.005)

    def reset(self):
        self.serial_interface.send(0)
        self.serial_interface.reset()


if __name__ == '__main__':
    try:
        motor_testing = Motor_Testing()
        motor_testing.run()
    except Exception as e:
        motor_testing.reset()
        print(e)
