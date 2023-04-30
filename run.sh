#!/bin/bash
source pyvenv/bin/activate
python live_plot.py data.csv 50 &
python live_plot.py parameters.csv 1000 &
python main.py 
