@echo off
".\C:\Users\diete\motortesting\pyvenv\Scripts\activate"
"C:\Users\diete\AppData\Local\Programs\Python\Python311\python.exe" "C:\Users\diete\motortesting\live_plot.py" data.csv 200 &
"C:\Users\diete\AppData\Local\Programs\Python\Python311\python.exe" "C:\Users\diete\motortesting\live_plot.py" parameters.csv 2000 &
"C:\Users\diete\AppData\Local\Programs\Python\Python311\python.exe" "C:\Users\diete\motortesting\main.py"
pause
