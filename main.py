import random
import time
from csv_writer import Csv_Writer
from fir_filter import Fir_Filter


def main():
    csv_writer = Csv_Writer('data.csv', ['x', 'y', 'yf'])

    x = 0
    y = 0
    fir_filter = Fir_Filter()
    while True:
        x += 100
        y += (random.random() - 0.5)
        yf = fir_filter.give_filtered(y)

        csv_writer.add_line_of_data([x, y, yf])
        time.sleep(0.002)


if __name__ == '__main__':
    main()
