from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators

class HomePage(BasePage):

    def click_zaloguj_btn(self):
        self.driver.find_element(*HomePageLocators.Login_btn).click()

    def _verify_page(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.Login_btn))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(HomePageLocators.Login_btn))
        assert "My Store" in self.driver.title
        print("Home page verification")