from selenium import webdriver
from pages.home.login_page import LoginPage
from pages.home.order_page import ProductOrder
from pages.home.update_address_page import UpdateAddress
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.order = ProductOrder(self.driver)
        self.address = UpdateAddress(self.driver)

    @pytest.mark.run(order=1)
    def test_verify_title(self):
        result1 = self.lp.verify_title()
        assert result1 == True

    @pytest.mark.run(order=5)
    def test_valid_login(self):
        self.lp.login_test("test128@email.com", "0926302426")
        result = self.lp.valid_login()
        assert result == True

    @pytest.mark.run(order=2)
    def test_empty_login(self):
        self.lp.login_test("", "")
        result = self.lp.empty_login()
        assert result == True

    @pytest.mark.run(order=3)
    def test_invalid_email_login(self):
        self.lp.login_test("test1234", "0926302426")
        result = self.lp.invalid_email_login()
        assert  result == True

    @pytest.mark.run(order=4)
    def test_invalid_password_login(self):
        self.lp.login_test("test128@email.com", "12345")
        result = self.lp.invalid_password_login()
        assert result == True

    @pytest.mark.run(order=13)
    def test_order(self):
        self.order.order_complete_test("blouse")

    @pytest.mark.run(order=6)
    def test_verify_add_to_cart(self):
        self.order.addto_cart_page_test("blouse")

    @pytest.mark.run(order=7)
    def test_summary_page(self):
        self.order.sumaary_page_test("blouse")

    @pytest.mark.run(order=8)
    def test_address_page(self):
        self.order.address_page_test("blouse")

    @pytest.mark.run(order=9)
    def test_update_address(self):
        self.address.update_address_test("blouse", "Ali", "Hussain", "Islambad",
                                         "Islamabad", "46000", "0926302426", "03005050555", "Billing Address")

    @pytest.mark.run(order=10)
    def test_shipping_page(self):
        self.order.shipping_page_test("blouse")

    @pytest.mark.run(order=11)
    def test_term_condition_check(self):
        self.order.term_condition_check_test("blouse")

    @pytest.mark.run(order=12)
    def test_payment_page(self):
        self.order.payemet_page_test("blouse")

