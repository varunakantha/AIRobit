# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import time
import threading
from graph_generator import plotdata
import pandas as pd

import executors


target_page = "https://gossip.hirufm.lk/81445/2022/11/fifa-world-cup-qatar-2022.html"
target_element = "/html/body/div[1]/div[6]/div[1]/div[2]/div/div[3]/div[3]/div/div[1]/font[1]/b"

def exe_func():
    executor = executors.MainExecutor()

    #if executor.login("varunakantha@gmail.com", "xxx"):

    try:
        executor.start_data_stream(target_page, target_element)
    
    except Exception as e:
            print("Oops! Exception in main method : " + str(e))
            time.sleep(5)
            executor.start_data_stream(target_page, target_element)



if __name__ == '__main__':
    pd.DataFrame(columns=['time','count','a','b','c']).to_excel('Data\graph.xlsx')
    t1 = threading.Thread(target= exe_func)
    t2 = threading.Thread(target = plotdata)

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

