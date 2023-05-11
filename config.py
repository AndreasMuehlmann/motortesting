import math

from voltage_schedulers.trapezoid_function_scheduler import Trapezoid_Function_Scheduler
from voltage_schedulers.csv_scheduler import Csv_Scheduler
from voltage_schedulers.custom_function_scheduler import Custom_Function_Scheduler


# x: time in seconds
def function(x):
    return 50 * (-math.cos(x) + 1.5)


repetitions = 5
period_duration_in_s = 15
# voltage_scheduler = Trapezoid_Function_Scheduler(20, 200, 0.5, 0.5)
voltage_scheduler = Csv_Scheduler('measurements/voltage_schedule.csv')
# voltage_scheduler = Custom_Function_Scheduler(function)
