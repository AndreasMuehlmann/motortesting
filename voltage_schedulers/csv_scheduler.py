import time

import pandas as pd

import config as conf


class Csv_Scheduler:
    def __init__(self, file_name):
        self.start_time = time.time()
        self.data = pd.read_csv(file_name)
        self.times = self.data['time']
        self.voltages = self.data['voltage']
        self.index = 0
        self.was_reset = False

    def give_current_voltage(self):
        if time.time() - self.start_time >= self.times[len(self.times) - 1] - self.times[0]:
            self.start_time = time.time()
            self.index = 0
            self.was_reset = True
        for i in range(self.index, len(self.times)):
            if self.times[i] - self.times[0] > time.time() - self.start_time:
                self.index = i
                return self.voltages[i] * 255 / 5
        return self.voltages[-1] * 255 / 5
