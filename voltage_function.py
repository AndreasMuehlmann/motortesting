import time


class Voltage_Function:
    def __init__(self):
        self.seconds_to_repetition = 8
        self.start_time = time.time()
        self.max = 255
        self.min = 20
        self.time_to_max = 0.5
        self.time_to_min = self.time_to_max
        self.cool_down_time = 3

    def give_current_voltage(self):
        if time.time() - self.start_time >= self.seconds_to_repetition:
            self.start_time = time.time()
        return self._voltage_over_time(time.time() - self.start_time)

    # x: time in seconds
    def _voltage_over_time(self, x):
        if x >= self.seconds_to_repetition - self.time_to_min:
            return self.max + -(self.max - self.min) / (self.time_to_min) * \
                               (x - (self.seconds_to_repetition - self.time_to_min))
        elif x >= self.time_to_max + self.cool_down_time:
            return 255
        elif x <= self.cool_down_time:
            return self.min
        else:
            return (self.max - self.min) / (self.time_to_max) * \
                    (x - self.cool_down_time) + self.min

