from selenium.webdriver.common.by import By
from time import sleep
from browser import Browser
import unittest


class SecurePage(Browser):
    LOGOUT_BTN = (By.XPATH, '//*[@id="content"]/div/a')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="content"]/div/a')

    def navigate_to_secure_page(self):
        self.driver.get('https://the-internet.herokuapp.com/secure')

    def logout_button(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()

    def logged(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).get_attribute()

