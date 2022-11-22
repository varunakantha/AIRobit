import datetime
import random
import threading
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plotdata():
    plt.style.use('fivethirtyeight')
    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}

    def animate(i):
        print("Animation is started.")

        lock = threading.Lock()
        lock.acquire()
        data = pd.read_excel('Data\graph.xlsx')
        lock.release()

        if len(data) > 0:
            x = data['time'].to_list()
            x1 = data['ftime'].to_list()
            y1 = data['count'].to_list()
            z = data['predicted_value'].to_list()

            y_counter = data['time'].iat[-1]
            current_a = data['a'].iat[-1]
            current_b = data['b'].iat[-1]
            current_c = data['c'].iat[-1]

            plt.cla()
            plt.scatter(x, y1, color='black')
            plt.plot(x, y1, label='Channel 1')
            plt.plot(x1, z, label='Channel 2')

            # plt.legend(loc='upper left')
            title = "y = (" + str(current_a) + ")x^2 + (" + str(current_b) + ")x + " + str(current_c)+"    |   "+str(datetime.datetime.now())
            plt.title(title)
            plt.tight_layout()
            plt.savefig("Data/graph-" + str(y_counter) + ".png")

    ani = FuncAnimation(plt.gcf(), animate, interval=10000)

    plt.tight_layout()
    plt.show()
