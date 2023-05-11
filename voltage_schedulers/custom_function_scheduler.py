import time

import config as conf


class Custom_Function_Scheduler:
    def __init__(self, custom_function):
        self.start_time = time.time()
        self.custom_function = custom_function
        self.was_reset = False

    def give_current_voltage(self):
        if time.time() - self.start_time >= conf.period_duration_in_s:
            self.start_time = time.time()
            self.was_reset = True
        return self.custom_function(time.time() - self.start_time)
