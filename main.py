# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import time

import executors
import test1

target_page = "https://gossip.hirufm.lk/81118/2022/11/tharindi-franando.html"
target_element = "/html/body/div[1]/div[6]/div[1]/div[2]/div/div[3]/div[3]/div/div[1]/font[1]/b"

# if __name__ == '__main__':
#     executor = executors.MainExecutor()
#
#     #if executor.login("varunakantha@gmail.com", "xxx"):
#
#     try:
#         executor.start_data_stream(target_page, target_element)
#
#     except Exception as e:
#             print("Oops! Exception in main method : " + str(e))
#             time.sleep(5)
#             executor.start_data_stream(target_page, target_element)
#
#         # else:
#         #     print("Ooops! Unable to login to account.")

target_page = "https://gossip.hirufm.lk/77234/2022/07/cctv-matara.html"
target_element = "/html/body/div[3]/div[5]/div[7]/div[1]/div[2]/div/div[3]/div[3]/div/div[1]/font[1]/b"

if __name__ == '__main__':
    test = test1.animation