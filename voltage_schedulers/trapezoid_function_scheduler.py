import time

import config as conf


class Trapezoid_Function_Scheduler:
    def __init__(self, min, max, rise_time, fall_time):
        self.start_time = time.time()
        self.max = max
        self.min = min
        self.rise_time = rise_time
        self.fall_time = fall_time
        self.high_time = (conf.period_duration_in_s - rise_time - fall_time) / 2
        self.low_time = self.high_time
        self.was_reset = False

    def give_current_voltage(self):
        if time.time() - self.start_time >= conf.period_duration_in_s:
            self.start_time = time.time()
            self.was_reset = True
        return self._voltage_over_time(time.time() - self.start_time)

    # x: time in seconds
    def _voltage_over_time(self, x):
        if x >= self.low_time + self.rise_time + self.high_time:
            return self.max + -(self.max - self.min) / (self.fall_time) * \
                               (x - (self.low_time + self.rise_time + self.high_time))
        elif x >= self.low_time + self.rise_time:
            return self.max
        elif x >= self.low_time:
            return (self.max - self.min) / (self.rise_time) * \
                    (x - self.low_time) + self.min
        else:
            return self.min
