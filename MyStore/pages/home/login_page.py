from base.selenium_driver import SeleniumDriver
import utilities.Custom_logger as cl
import logging
import time


class LoginPage(SeleniumDriver):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# locators
    _login_link = "//a[contains(text(),'Sign in')]"
    _email_field = "email"
    _password_field = "passwd"
    _login_btn = "SubmitLogin"

# find and get locators
#     def get_login_link(self):
#         return self.driver.find_element(By.LINK_TEXT, self._login_link)
#
#     def get_email_field(self):
#         return self.driver.find_element(By.ID, self._email_field)
#
#     def get_password_field(self):
#         return self.driver.find_element(By.ID, self._password_field)
#
#     def get_login_button(self):
#         return self.driver.find_element(By.NAME, self._login_btn)

# Operation on locators
    def click_on_login_link(self):
        self.elementClick(self._login_link, locatorType= "xpath")

    def enter_email(self, email):
        self.sendKeys(email, self._email_field)

    def enter_password(self, password):
        self.sendKeys(password, self._password_field)

    def click_login_button(self):
        self.elementClick(self._login_btn)

    def login_test(self, email="", password=""):
        self.click_on_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(2)

    def valid_login(self):
        result = self.isElementPresent("//span[contains(text(),'Mushtaq Hussain')]", locatorType= "xpath")
        return result

    def empty_login(self):
        result = self.isElementPresent("//li[contains(text(),'An email address required.')]",locatorType="xpath")
        return result

    def invalid_email_login(self):
        result = self.isElementPresent("//li[contains(text(),'Invalid email address.')]", locatorType= "xpath")
        return result

    def invalid_password_login(self):
        result = self.isElementPresent("//li[contains(text(),'Authentication failed.')]", locatorType= "xpath")
        return result

    def verify_title(self):
        if "My Store" in self.get_title():
            return True
        else:
            return False