# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import executors

target_page = "https://gossip.hirufm.lk/74181/2022/04/chamara-wijesooriya.html"
target_element = "/html/body/div[1]/div[5]/div[7]/div[1]/div[2]/div/div[3]/div[3]/div/div[1]/font[1]/b"

if __name__ == '__main__':
    executor = executors.MainExecutor()

    if executor.login("ajantha1311@gmail.com", "1qaz2wsx@"):

        executor.start_data_stream(target_page,target_element)

    else:
        print("Ooops! Unable to login to account.")
