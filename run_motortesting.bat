@echo off
start "Data Plot" cmd /c "C:\Users\diete\motortesting\pyvenv\Scripts\activate && python C:\Users\diete\motortesting\live_plot.py C:\Users\diete\motortesting\data.csv 200"
start "Parameter Plot" cmd /c "C:\Users\diete\motortesting\pyvenv\Scripts\activate && python C:\Users\diete\motortesting\live_plot.py C:\Users\diete\motortesting\parameters.csv 2000"
start "Communication Arduino and Logic" cmd /c "C:\Users\diete\motortesting\pyvenv\Scripts\activate && python C:\Users\diete\motortesting\main.py"
pause
