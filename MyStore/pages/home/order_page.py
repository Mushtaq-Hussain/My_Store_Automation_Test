from base.selenium_driver import SeleniumDriver
import utilities.Custom_logger as cl
from selenium.webdriver import ActionChains
import logging
import time


class ProductOrder(SeleniumDriver):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #loctors:
    _search_btn = "submit_search"   #name
    _search_field = "search_query_top" #id
    _mouse_hover = "right-block" #class
    _Addto_cart = "//span[contains(text(),'Add to cart')]"
    _proceed_check = "//header/div[3]/div[1]/div[1]/div[4]/div[1]/div[2]/div[4]/a[1]/span[1]"
    _proceed_check1 = "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/p[2]/a[1]/span[1]"
    _proceed_check2 = "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/form[1]/p[1]/button[1]/span[1]"
    _proceed_check3 = "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/p[1]/button[1]/span[1]"
    _Check_box = "cgv"
    _payby_bank = "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/p[1]/a[1]"
    _payby_cheque = "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/p[1]/a[1]/span[1]"
    _confirm_order = "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/form[1]/p[1]/button[1]/span[1]"
    _order_complete = "//strong[contains(text(),'Your order on My Store is complete.')]"
    _cross = "cross"
    _home_btn = "//body/div[@id='page']/div[2]/div[1]/div[1]/a[1]/i[1]"
    _term_condition_close = "//a[@class='fancybox-item fancybox-close']" # class

    def click_cross(self):
        self.elementClick(self._cross, locatorType= "class")

    def click_on_home_btn(self):
        self.elementClick(self._home_btn, locatorType="xpath")

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

    def click_on_proceed2(self):
        self.elementClick(self._proceed_check2, locatorType= "xpath")

    def click_on_proceed3(self):
        self.elementClick(self._proceed_check3, locatorType= "xpath")

    def click_on_checkbox(self):
        self.elementClick(self._Check_box)

    def click_on_paybank(self):
        self.elementClick(self._payby_bank, locatorType= "xpath")

    def click_on_confirm_order(self):
        self.elementClick(self._confirm_order, locatorType= "xpath")

    def click_on_close_term_condition(self):
        self.elementClick(self._term_condition_close, locatorType="xpath")

    def order_complete_test(self, name):
        self.enter_search_product(name)
        self.click_on_search()
        self.mouse_hover()
        time.sleep(2)
        self.click_on_proceed()
        self.click_on_proceed1()
        self.click_on_proceed2()
        self.click_on_checkbox()
        self.click_on_proceed3()
        self.click_on_paybank()
        self.click_on_confirm_order()
        result = self.isElementPresent("//strong[contains(text(),'Your order on My Store is complete.')]", locatorType= "xpath")
        assert result == True

    def addto_cart_page_test(self, name):
        self.enter_search_product(name)
        self.click_on_search()
        self.mouse_hover()
        result = self.isElementPresent("//header/div[3]/div[1]/div[1]/div[4]/div[1]/div[1]/h2[1]", locatorType= "xpath")
        assert result == True
        self.click_cross()
        time.sleep(2)

    def sumaary_page_test(self, name):
        self.enter_search_product(name)
        self.click_on_search()
        self.mouse_hover()
        self.click_on_proceed()
        result = self.isElementPresent("//tbody/tr[@id='product_2_7_0_430147']/td[1]/a[1]/img[1]", locatorType="xpath")
        assert result == True
        self.click_on_home_btn()
        time.sleep(2)

    def address_page_test(self, name):
        self.enter_search_product(name)
        self.click_on_search()
        self.mouse_hover()
        self.click_on_proceed()
        self.click_on_proceed1()
        result = self.isElementPresent("//h3[contains(text(),'Your delivery address')]", locatorType="xpath")
        assert result == True
        self.click_on_home_btn()
        time.sleep(2)
        
    def shipping_page_test(self, name):
        self.enter_search_product(name)
        self.click_on_search()
        self.mouse_hover()
        self.click_on_proceed()
        self.click_on_proceed1()
        self.click_on_proceed2()
        result = self.isElementPresent("//strong[contains(text(),'My carrier')]", locatorType="xpath")
        assert result == True
        self.click_on_home_btn()
        time.sleep(2)

    def payemet_page_test(self, name):
        self.enter_search_product(name)
        self.click_on_search()
        self.mouse_hover()
        self.click_on_proceed()
        self.click_on_proceed1()
        self.click_on_proceed2()
        self.click_on_checkbox()
        self.click_on_proceed3()
        self.click_on_paybank()
        result = self.isElementPresent("//h3[contains(text(),'Bank-wire payment.')]", locatorType="xpath")
        assert result == True
        self.click_on_home_btn()
        time.sleep(2)

    def term_condition_check_test(self,name):
        self.enter_search_product(name)
        self.click_on_search()
        self.mouse_hover()
        self.click_on_proceed()
        self.click_on_proceed1()
        self.click_on_proceed2()
        self.click_on_proceed3()
        result = self.isElementPresent("//p[contains(text(),'You must agree to the terms of service before cont')]", locatorType="xpath")
        assert result == True
        time.sleep(2)
        self.click_on_close_term_condition()
        time.sleep(2)
        self.click_on_home_btn()
        time.sleep(2)
        