import time
import datetime

import re
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import regression_models


class MainExecutor:
    path_chrome = "C:\\Users\\varunakanthak\\Automation\\drivers\\chromedriver"
    path_firefox = "C:\\Users\\varunakanthak\\Automation\\drivers\\geckodriver"
    selenium_driver = None
    data_frame = None

    # Initialize webdriver and disable chrome notifications
    def __init__(self):

        # For Chrome Browser
        # chrome_options = webdriver.ChromeOptions()
        # prefs = {"profile.default_content_setting_values.notifications": 2}
        # chrome_options.add_experimental_option("prefs", prefs)
        # MainExecutor.selenium_driver = webdriver.Chrome(MainExecutor.path, chrome_options=chrome_options)

        # For Firefox Browser
        options = webdriver.FirefoxOptions()

        # Make Headless
        print("Starting  with Headless-Mode...")
        options.headless = True
        options.binary_location = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        print("Opening Browser...")
        MainExecutor.selenium_driver = webdriver.Firefox(executable_path=MainExecutor.path_firefox, options=options)
        print("Maximizing Browser...")
        MainExecutor.selenium_driver.maximize_window()

        self.data_frame = pd.DataFrame(columns=['time', 'count'])

    def login(self, email, key):

        # Go to login page
        print("Redirecting to Facebook...")
        MainExecutor.selenium_driver.get("http://www.facebook.com")

        # Enter username
        print("Entering Username...")
        user_name = self.locate_element(
            "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
        user_name.clear()
        user_name.send_keys(email)

        # Enter password
        print("Entering Password...")
        password = self.locate_element(
            "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
        password.clear()
        password.send_keys(key)

        # Click login button
        print("Clicking Login Button...")
        login_button = self.locate_element(
            "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
        login_button.click()

        time.sleep(1)

        # Check the login title
        if MainExecutor.selenium_driver.title == "Facebook":
            print("FB Login is Successful !")
            return True
        else:
            print(" Oops'' Login Fail !")
            return False

        # Identify the web element and return it

    def locate_element(self, xpath):

        try:
            element = WebDriverWait(MainExecutor.selenium_driver, 50).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            return element
        except:

            print("Oops ! Element cannot be detected.")

    def start_data_stream(self, url, xpath):

        for counter in range(1, 720):
            print("Redirecting to target page...")
            MainExecutor.selenium_driver.get(url)
            print("Locating  target Data piece...")
            target_element = self.locate_element(xpath)
            print("Printing data...")
            print("Data : " + self.extract_numbers(target_element.text) + " | " + str(
                datetime.datetime.now()) + " | " + str(counter))

            self.data_frame.loc[counter, 'time'] = float(counter)

            # This is for FB analysis
            self.data_frame.loc[counter, 'count'] = float(self.extract_numbers(target_element.text))

            # This is for Views analysis
            # self.data_frame.loc[counter, 'count'] = float(int(self.extract_numbers(target_element.text)) - 1)

            # loop is configured to be executed in every minute
            print("Waiting for 1 minute...")
            time.sleep(60)

            # regression_models.perform_liner_regression(self.data_frame)

            regression_models.perform_polynomial_regression(self.data_frame, counter)
            regression_models.perform_liner_regression(self.data_frame)

    def extract_numbers(self, text):

        data = re.sub("[^0-9.]", "", text)
        if str(text).find('K') != -1:
            return str(float(data) * 1000)
        else:
            return data
