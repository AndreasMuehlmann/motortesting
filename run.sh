#!/bin/bash
source pyvenv/bin/activate
python live_plot.py data.csv &
python main.py 
