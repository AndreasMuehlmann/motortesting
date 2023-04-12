import serial
import time


class Serial_Interface:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)
        time.sleep(2)

    def recv_data(self):
        return self.ser.readline().decode().strip()

    def send(self, data):
        pass
    
    def reset(self):
        self.ser.close()
