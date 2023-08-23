# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import time
import threading
from graph_generator import plotdata
import pandas as pd

import executors

target_page = "https://gossip.hirufm.lk/89263/2023/08/ruwanweli-saya.html"
target_element = "/html/body/div[1]/div[5]/div[11]/div[1]/div[2]/div/div[3]/div[3]/div/div/font[1]/b"


def exe_func():
    executor = executors.MainExecutor()

    # if executor.login("varunakantha@gmail.com", "xxx"):

    executor.start_data_stream(target_page, target_element)


if __name__ == '__main__':
    pd.DataFrame(columns=['time', 'count', 'a', 'b', 'c']).to_excel('Data\graph.xlsx')
    t1 = threading.Thread(target=exe_func)
    t2 = threading.Thread(target=plotdata, daemon=True)
    t1.start()
    t2.start()

