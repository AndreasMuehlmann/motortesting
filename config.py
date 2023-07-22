import os
import math

from voltage_schedulers.trapezoid_function_scheduler import Trapezoid_Function_Scheduler
from voltage_schedulers.csv_scheduler import Csv_Scheduler
from voltage_schedulers.custom_function_scheduler import Custom_Function_Scheduler

path_to_motortesting = os.path.dirname(__file__)
path_to_measurements = os.path.join(path_to_motortesting, "measurements")
csv_scheduler_path = os.path.join(path_to_measurements, "voltage_schedule.csv")

# x: time in seconds
def function(x):
    return 50 * (-math.cos(x) + 1.5)

def calibration_function(x):
    return 128


repetitions = 5
period_duration_in_s = 5
# voltage_scheduler = Trapezoid_Function_Scheduler(45, 128, 0.5, 0.5)
voltage_scheduler = Csv_Scheduler(csv_scheduler_path)
# voltage_scheduler = Custom_Function_Scheduler(function)
# voltage_scheduler = Custom_Function_Scheduler(calibration_function)
