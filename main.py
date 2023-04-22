import time
from csv_writer import Csv_Writer
from fir_filter import Fir_Filter
from serial_interface import Serial_Interface
from voltage_function import Voltage_Function


def main():
    fir_filter = Fir_Filter()
    csv_writer = Csv_Writer('data.csv', ['time', 'rpm', 'filtered_rpm', 'voltage'])
    voltage_function = Voltage_Function()
    prev_measurement = 0
    start_time = time.time()
    while True:
        try:
            measurement = serial_interface.recv()
            measurement = float(measurement)
            prev_measurement = measurement

        except (UnicodeDecodeError, ValueError):
            measurement = prev_measurement
        voltage = voltage_function.give_current_voltage()
        serial_interface.send(voltage)

        filtered_measruement = fir_filter.give_filtered(measurement)
        csv_writer.add_line_of_data(
                [time.time() - start_time, measurement,
                 filtered_measruement, voltage * 500 / 255]
                )
        time.sleep(0.005)


if __name__ == '__main__':
    try:
        serial_interface = Serial_Interface()
        serial_interface.flush()
        main()
    except KeyboardInterrupt:
        serial_interface.reset()
