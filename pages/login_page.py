from locators.locators import LoginLocators as ll
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def login_title(self):
        return self.driver.title

    def action_login(self, username, password):
        self.driver.find_element(*ll.input_username).send_keys(username)
        self.driver.find_element(*ll.input_password).send_keys(password)
        self.driver.find_element(*ll.login_btn).click()

    def action_logout(self):
        self.driver.find_element(*ll.hamburger_btn).click()
        self.wait.until(EC.element_to_be_clickable(ll.logout_btn)).click()
