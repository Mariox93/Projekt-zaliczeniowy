from pages.base_page import BasePage
from locators import RegisterPageLocators
from selenium.webdriver.support.ui import Select

class RegisterPage(BasePage):

    # YOUR PERSONAL INFORMATION SECTION

    def choose_gender(self, gender):
        if gender == "M":
            self.driver.find_element(*RegisterPageLocators.GenderMr_rbtn).click()
        else:
            self.driver.find_element(*RegisterPageLocators.GenderMrs_rbtn).click()

    def fill_name(self, name):
        self.driver.find_element(*RegisterPageLocators.Name_input).send_keys(name)

    def fill_surname(self, surname):
        self.driver.find_element(*RegisterPageLocators.Surname_input).send_keys(surname)

    def fill_email(self, email):
        self.driver.find_element(*RegisterPageLocators.Email_input).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*RegisterPageLocators.Password_input).send_keys(password)

    def choose_day(self, day):
        Select(self.driver.find_element(*RegisterPageLocators.Day_select)).select_by_value(day)

    def choose_month(self, month):
        Select(self.driver.find_element(*RegisterPageLocators.Month_select)).select_by_value(month)

    def choose_year(self, year):
        Select(self.driver.find_element(*RegisterPageLocators.Year_select)).select_by_value(year)

    def accept_newsletter(self):
        self.driver.find_element(*RegisterPageLocators.Newsletter_checkbox).click()

    def accept_specialOffers(self):
        self.driver.find_element(*RegisterPageLocators.SpecialOffers_checkbox).click()

    # YOUR ADDRESS SECTION

    def fill_firstName(self, firstName):
        self.driver.find_element(*RegisterPageLocators.FirstNameAddress_input).send_keys(firstName)

    def fill_lastName(self, lastName):
        self.driver.find_element(*RegisterPageLocators.FirstNameAddress_input).send_keys(lastName)

    def fill_company(self, company):
        self.driver.find_element(*RegisterPageLocators.Company_input).send_keys(company)

    def fill_address(self, address):
        self.driver.find_element(*RegisterPageLocators.AddressFirstLine_input).send_keys(address)

    def fill_city(self, city):
        self.driver.find_element(*RegisterPageLocators.City_input).send_keys(city)

    def choose_state(self, state):
        Select(self.driver.find_element(*RegisterPageLocators.State_select)).select_by_visible_text(state)

    def fill_postalCode(self, postalCode):
        self.driver.find_element(*RegisterPageLocators.PostalCode_input).send_keys(postalCode)

    def choose_country(self, country):
        Select(self.driver.find_element(*RegisterPageLocators.Country_select)).select_by_visible_text(country)

    def fill_addInfo(self, addInfo):
        self.driver.find_element(*RegisterPageLocators.AdditionalInfo_input).send_keys(addInfo)

    def fill_homePhone(self, homePhone):
        self.driver.find_element(*RegisterPageLocators.HomePhone_input).send_keys(homePhone)

    def fill_mobilePhone(self, mobilePhone):
        self.driver.find_element(*RegisterPageLocators.MobilePhone_input).send_keys(mobilePhone)

    def fill_alias(self, alias):
        self.driver.find_element(*RegisterPageLocators.Alias_input).send_keys(alias)
        self.driver.implicitly_wait(10)

    def click_registerButton(self):
        self.driver.find_element(*RegisterPageLocators.Register_btn).click()

    def check_password_error(self):
        error = self.driver.find_element(*RegisterPageLocators.Register_error)
        error_text = error.get_attribute('innerText')
        assert "passwd is invalid." in error_text

    def check_postalCode_error(self):
        error = self.driver.find_element(*RegisterPageLocators.Register_error)
        error_text = error.get_attribute('innerText')
        assert "The Zip/Postal code you've entered is invalid. It must follow this format: 00000" in error_text

    def check_numberPhone_error(self):
        error = self.driver.find_element(*RegisterPageLocators.Register_error)
        error_text = error.get_attribute('innerText')
        assert "You must register at least one phone number." in error_text

    def check_empty_form_error(self):
        error = self.driver.find_element(*RegisterPageLocators.Register_main_error)
        error_text = error.getText()
        assert "There are 6 errors" in error_text
