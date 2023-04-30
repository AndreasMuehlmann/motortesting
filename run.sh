#!/bin/bash
source pyvenv/bin/activate
python live_plot.py data.csv 200 &
python live_plot.py parameters.csv 2000 &
python main.py 
