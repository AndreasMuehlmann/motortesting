import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd


plt.style.use('fivethirtyeight')
plt.tight_layout()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x']
    y = data['y']
    yf = data['yf']


    plt.cla()
    plt.plot(x, y, label='rpm')
    plt.plot(x, yf, label='filtered rpm')
    # plt.xlim([0, 1000])
    # plt.ylim([-20, 20])
    plt.legend(loc='upper left')
    plt.tight_layout()


animation = FuncAnimation(plt.gcf(), animate, interval=100,  cache_frame_data=False)
plt.show()
