import serial
import time


class Serial_Interface:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)
        time.sleep(2)

    def recv(self):
        return self.ser.readline().decode().strip()

    def send(self, data):
        self.ser.write(str(data).encode() + b'\n')

    def flush(self):
        self.ser.flush()

    def reset(self):
        self.ser.close()
