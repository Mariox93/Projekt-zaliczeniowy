from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from test_utils import utils
import unittest
from ddt import ddt, data, unpack
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
invalid_email_data = os.path.join(THIS_DIR, '..', 'test_data/invalid_emails.csv')
correct_data = os.path.join(THIS_DIR, '..', 'test_data/correct_data.csv')
insecure_password = os.path.join(THIS_DIR, '..', 'test_data/insecure_password.csv')
invalid_postalCode = os.path.join(THIS_DIR, '..', 'test_data/invalid_postalCode.csv')

@ddt
class RegistrationTest(BaseTest):
    """
    Register page tests
    """

    @data(*utils.get_data(invalid_email_data))
    @unpack
    def test_incorrect_email(self, invalid_mail):
        """Attempt to register user with invalid email"""

        hp = HomePage(self.driver)
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.fill_email(invalid_mail)
        lp.click_create_btn()
        lp.check_error()

    @data(*utils.get_data(insecure_password))
    @unpack
    def test_insecure_password(self, gender, first_name, last_name, email, password, day, month, year, company,
                                  address, city, state, postal_code, add_info, home_phone, mobile_phone, alias):
        """Attempt to register user with insecure password"""
        hp = HomePage(self.driver)
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.click_create_btn()
        rp = RegisterPage(self.driver)
        rp.choose_gender(gender)
        rp.fill_name(first_name)
        rp.fill_surname(last_name)
        rp.fill_password(password)
        rp.choose_day(day)
        rp.choose_month(month)
        rp.choose_year(year)
        rp.accept_newsletter()
        rp.accept_specialOffers()
        rp.fill_company(company)
        rp.fill_address(address)
        rp.fill_city(city)
        rp.choose_state(state)
        rp.fill_postalCode(postal_code)
        rp.fill_addInfo(add_info)
        rp.fill_homePhone(home_phone)
        rp.fill_mobilePhone(mobile_phone)
        rp.fill_alias(alias)
        rp.click_registerButton()
        rp.check_password_error()

    @data(*utils.get_data(invalid_postalCode))
    @unpack
    def test_invalid_postalCode(self, gender, first_name, last_name, email, password, day, month, year, company,
                               address, city, state, postal_code, add_info, home_phone, mobile_phone, alias):
        """Attempt to register user with invalid postal code"""

        hp = HomePage(self.driver)
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.click_create_btn()
        rp = RegisterPage(self.driver)
        rp.choose_gender(gender)
        rp.fill_name(first_name)
        rp.fill_surname(last_name)
        rp.fill_password(password)
        rp.choose_day(day)
        rp.choose_month(month)
        rp.choose_year(year)
        rp.accept_newsletter()
        rp.accept_specialOffers()
        rp.fill_company(company)
        rp.fill_address(address)
        rp.fill_city(city)
        rp.choose_state(state)
        rp.fill_postalCode(postal_code)
        rp.fill_addInfo(add_info)
        rp.fill_homePhone(home_phone)
        rp.fill_mobilePhone(mobile_phone)
        rp.fill_alias(alias)
        rp.click_registerButton()
        rp.check_postalCode_error()

    @data(*utils.get_data(correct_data))
    @unpack
    def test_without_numberPhone(self, gender, first_name, last_name, email, password, day, month, year, company,
                                  address, city, state, postal_code, add_info, home_phone, mobile_phone, alias):
        """Attempt to register user without number phone"""

        hp = HomePage(self.driver)
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.click_create_btn()
        rp = RegisterPage(self.driver)
        rp.choose_gender(gender)
        rp.fill_name(first_name)
        rp.fill_surname(last_name)
        rp.fill_password(password)
        rp.choose_day(day)
        rp.choose_month(month)
        rp.choose_year(year)
        rp.accept_newsletter()
        rp.accept_specialOffers()
        rp.fill_company(company)
        rp.fill_address(address)
        rp.fill_city(city)
        rp.choose_state(state)
        rp.fill_postalCode(postal_code)
        rp.fill_addInfo(add_info)
        rp.fill_alias(alias)
        rp.click_registerButton()
        rp.check_numberPhone_error()

    @data(*utils.get_data(correct_data))
    @unpack
    def test_correct_registration(self, gender, first_name, last_name, email, password, day, month, year, company, address, city, state, postal_code, add_info, home_phone, mobile_phone, alias):
        """Attempt to register user with correct data"""

        hp = HomePage(self.driver)
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.click_create_btn()
        rp = RegisterPage(self.driver)
        rp.choose_gender(gender)
        rp.fill_name(first_name)
        rp.fill_surname(last_name)
        rp.fill_password(password)
        rp.choose_day(day)
        rp.choose_month(month)
        rp.choose_year(year)
        rp.accept_newsletter()
        rp.accept_specialOffers()
        rp.fill_company(company)
        rp.fill_address(address)
        rp.fill_city(city)
        rp.choose_state(state)
        rp.fill_postalCode(postal_code)
        rp.fill_addInfo(add_info)
        rp.fill_homePhone(home_phone)
        rp.fill_mobilePhone(mobile_phone)
        rp.fill_alias(alias)
        #rp.click_registerButton() -> blocked


if __name__=="__main__":
    unittest.main(verbosity=2)
