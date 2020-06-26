from pages.base_page import BasePage
from locators import LoginPageLocators

class LoginPage(BasePage):
    def click_create_btn(self):
        self.driver.find_element(*LoginPageLocators.Create_btn).click()

    def fill_email(self, email):
        self.driver.find_element(*LoginPageLocators.Email_input).send_keys(email)

    def check_error(self):
        error = self.driver.find_element(*LoginPageLocators.CreateAccount_error)
        error_text = error.get_attribute('innerText')
        assert "Invalid email address." in error_text
