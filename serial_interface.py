import serial
import time


class Serial_Interface:
    def __init__(self):
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 9600)
        except serial.serialutil.SerialException:
            self.ser = serial.Serial('COM3', 9600)

        self.prev_measurements = [0, 0]
        time.sleep(1)

    def give_measurements(self):
        try:
            measurements = self._recv()
            measurements = [float(measurement) for measurement in measurements]
            self.prev_measurements = measurements
        except (UnicodeDecodeError, ValueError):
            measurements = self.prev_measurements
        return measurements

    def _recv(self):
        return self.ser.readline().decode().strip().split(',')

    def send(self, data):
        self.ser.write(str(data).encode() + b'\n')

    def reset(self):
        self.ser.close()
