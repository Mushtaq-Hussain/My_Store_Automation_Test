"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
import os


class WebDriverFactory():
    def __init__(self, browser):
        """
                Inits WebDriverFactory class

                Returns:
                    None
                """
        self.browser = browser

    """
            Set chrome driver and iexplorer environment based on OS

            chromedriver = "C:/.../chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver = webdriver.Chrome(chromedriver)

            PREFERRED: Set the path on the machine where browser will be executed
        """
    def getWebDriverInstance(self):
        baseURL = "http://automationpractice.com/index.php"
        if self.browser == "iexplorer":
            driver = webdriver.Edge(executable_path=r"C:\Users\mushtaq.hussain\PycharmProjects\letskodeit\drivers\msedgedriver.exe")
        elif self.browser == "firefox":
            firefoxdriver = r"C:\Users\mushtaq.hussain\PycharmProjects\letskodeit\drivers\geckodriver.exe"
            driver = webdriver.Firefox(executable_path=firefoxdriver)
        elif self.browser == "chrome":
            driver = webdriver.Chrome(executable_path=r"C:\Users\mushtaq.hussain\PycharmProjects\letskodeit\drivers\chromedriver.exe")
        else:
            driver = webdriver.Chrome(
                executable_path=r"C:\Users\mushtaq.hussain\PycharmProjects\letskodeit\drivers\chromedriver.exe")

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
