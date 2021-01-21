from base.selenium_driver import SeleniumDriver
import utilities.Custom_logger as cl
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import logging
import time


class UpdateAddress(SeleniumDriver):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# loctors

    _search_btn = "submit_search"   #name
    _search_field = "search_query_top" #id
    _mouse_hover = "right-block" #class
    _Addto_cart = "//span[contains(text(),'Add to cart')]"
    _proceed_check = "//header/div[3]/div[1]/div[1]/div[4]/div[1]/div[2]/div[4]/a[1]/span[1]"
    _proceed_check1 = "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/p[2]/a[1]/span[1]"
    _check_box = "addressesAreEquals" #id
    _update_btn = "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[2]/div[2]/ul[1]/li[9]/a[1]/span[1]"
    _address = "address1" # id
    _city = "//input[@id='city']"
    _state = "id_state" #id
    _postal_code = "postcode" # id
    _country = "id_country" # id
    _phone = "phone" # id
    _mobile_phone = "phone_mobile" # id
    _address_title = "alias" #id
    _save_btn = "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/p[2]/button[1]/span[1]"
    _first_name = "firstname" # id
    _last_name = "lastname" #id
    _home_btn = "//body/div[@id='page']/div[2]/div[1]/div[1]/a[1]/i[1]"

    def enter_search_product(self, name):
        text_field = self.driver.find_element_by_id(self._search_field)
        text_field.clear()
        self.sendKeys(name, self._search_field)

    def click_on_search(self):
        self.elementClick(self._search_btn, locatorType= "name")
        self.driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)

    def mouse_hover(self):
        action = ActionChains(self.driver)
        find = self.driver.find_element_by_class_name(self._mouse_hover)
        action.move_to_element(find).perform()
        time.sleep(2)
        add_cart = self.driver.find_element_by_xpath(self._Addto_cart)
        action.move_to_element(add_cart).click().perform()

    def click_on_proceed(self):
        self.elementClick(self._proceed_check, locatorType= "xpath")

    def click_on_proceed1(self):
        self.elementClick(self._proceed_check1, locatorType= "xpath")

    def click_on_check_box(self):
        self.elementClick(self._check_box)

    def click_on_update_btn(self):
        self.elementClick(self._update_btn, locatorType="xpath")

    def enter_first_name(self, first_name):
        text_field = self.driver.find_element_by_id(self._first_name)
        text_field.clear()
        self.sendKeys(first_name, self._first_name)
        time.sleep(2)

    def enter_last_name(self, last_name):
        text_field = self.driver.find_element_by_id(self._last_name)
        text_field.clear()
        self.sendKeys(last_name, self._last_name)
        time.sleep(2)

    def enter_adress(self, address):
        text_field = self.driver.find_element_by_id(self._address)
        text_field.clear()
        self.sendKeys(address, self._address)
        time.sleep(2)

    def enter_city(self, city):
        text_field = self.driver.find_element_by_xpath(self._city)
        text_field.clear()
        self.sendKeys(city, self._city, locatorType="xpath")
        time.sleep(2)

    def select_state(self):
        drop_down = self.driver.find_element_by_id(self._state)
        drop_down_list = Select(drop_down)
        drop_down_list.select_by_visible_text("Georgia")


    def enetr_postal_code(self, code):
        text_field = self.driver.find_element_by_id(self._postal_code)
        text_field.clear()
        self.sendKeys(code, self._postal_code)
        time.sleep(2)

    def enter_phone_number(self, phone_number):
        text_field = self.driver.find_element_by_id(self._phone)
        text_field.clear()
        self.sendKeys(phone_number, self._phone)
        time.sleep(2)

    def enter_mobile_number(self, mobile_number):
        text_field = self.driver.find_element_by_id(self._mobile_phone)
        text_field.clear()
        self.sendKeys(mobile_number, self._mobile_phone)
        time.sleep(2)

    def enter_address_title(self, title):
        text_field = self.driver.find_element_by_id(self._address_title)
        text_field.clear()
        self.sendKeys(title, self._address_title)
        time.sleep(2)

    def click_on_save_btn(self):
        self.elementClick(self._save_btn, locatorType= "xpath")
        time.sleep(2)

    def click_on_home_btn(self):
        self.elementClick(self._home_btn, locatorType= "xpath")

    def update_address_test(self, name, first_name, last_name, address, city, code, phone_number, mobile_number, title):
        self.enter_search_product(name)
        self.click_on_search()
        self.mouse_hover()
        self.click_on_proceed()
        self.click_on_proceed1()
        self.click_on_check_box()
        self.click_on_update_btn()
        time.sleep(2)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_adress(address)
        self.enter_city(city)
        self.select_state()
        time.sleep(4)
        self.enetr_postal_code(code)
        self.enter_phone_number(phone_number)
        self.enter_mobile_number(mobile_number)
        self.enter_address_title(title)
        self.click_on_save_btn()
        result = self.isElementPresent("//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[2]/div[2]/ul[1]/li[2]",
            locatorType="xpath")
        assert result == True
        time.sleep(2)
        self.click_on_home_btn()
        time.sleep(2)





