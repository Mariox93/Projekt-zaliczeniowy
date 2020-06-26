from selenium.webdriver.common.by import By

class HomePageLocators():
    Login_btn = (By.CLASS_NAME, "login")

class LoginPageLocators():
    Create_btn = (By.NAME, "SubmitCreate")
    Email_input = (By.NAME, "email_create")
    CreateAccount_error = (By.XPATH, '//div[@class="alert alert-danger"]/ol')

class RegisterPageLocators():

    # YOUR PERSONAL INFORMATION SECTION
    GenderMr_rbtn = (By.ID, "id_gender1")
    GenderMrs_rbtn = (By.ID, "id_gender2")
    Name_input = (By.ID, "customer_firstname")
    Surname_input = (By.ID, "customer_lastname")
    Email_input = (By.ID, "email")
    Password_input = (By.ID, "passwd")
    Day_select = (By.NAME, "days")
    Month_select = (By.NAME, "months")
    Year_select = (By.NAME, "years")
    Newsletter_checkbox = (By.ID, "newsletter")
    SpecialOffers_checkbox = (By.ID, "optin")

    # YOUR ADDRESS SECTION
    FirstNameAddress_input = (By.ID, "firstname")
    LastNameAddress_input = (By.ID, "lastname")
    Company_input = (By.ID, "company")
    AddressFirstLine_input = (By.ID, "address1")
    City_input = (By.ID, "city")
    State_select = (By.ID, "id_state")
    PostalCode_input = (By.ID, "postcode")
    Country_select = (By.ID, "id_country")
    AdditionalInfo_input = (By.ID, "other")
    HomePhone_input = (By.ID, "phone")
    MobilePhone_input = (By.ID, "phone_mobile")
    Alias_input = (By.ID, "alias")
    Register_btn = (By.ID, "submitAccount")
    Register_error = (By.XPATH, '//div[@class="alert alert-danger"]/ol')
    Register_main_error = (By.XPATH, '//div[@class="alert alert-danger"]/p')