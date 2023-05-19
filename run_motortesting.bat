@echo off
start /B "Data Plot" cmd /c "C:\Users\diete\motortesting\pyvenv\Scripts\activate && python C:\Users\diete\motortesting\live_plot.py C:\Users\diete\motortesting\data.csv 200"
start /B "Parameter Plot" cmd /c "C:\Users\diete\motortesting\pyvenv\Scripts\activate && python C:\Users\diete\motortesting\live_plot.py C:\Users\diete\motortesting\parameters.csv 2000"
call "C:\Users\diete\motortesting\pyvenv\Scripts\activate"
python "C:\Users\diete\motortesting\main.py"
pause
