import random
import time
import os
import subprocess
from csv_writer import Csv_Writer


def main():
    csv_writer = Csv_Writer('data.csv', ['x', 'y'])

    x = 0
    y = 0
    while True:
        csv_writer.add_line_of_data([x, y])

        x += 1
        y += random.random()

        time.sleep(0.1)


if __name__ == '__main__':
    main()
