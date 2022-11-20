import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plotdata():
    plt.style.use('fivethirtyeight')
    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}

    # x_vals = []
    # y_vals = []

    # index = count()


    def animate(i):
        data = pd.read_excel('Data\graph.xlsx')
        if len(data)>0:
            x = data['time'].to_list()
            y1 = data['count'].to_list()
            y_counter = data['time'].iat[-1]
            # a = data['a'].iat[-1]
            # b = data['b'].iat[-1]
            # c = data['c'].iat[-1]
            plt.cla()
            plt.scatter(x, y1, color='red')
            plt.plot(x, y1, label='Channel 1')

            # plt.legend(loc='upper left')
            title  = open('title.txt','r').read()
            plt.title(title)
            plt.tight_layout()
            plt.savefig("Data/graph-" + str(y_counter) + ".png")

    ani = FuncAnimation(plt.gcf(), animate, interval=10000)

    plt.tight_layout()
    plt.show()