from selenium.webdriver.common.by import By
from time import sleep
from browser import Browser
import unittest


class LogInPage(Browser):
    USERNAME = (By.XPATH, '//*[@id="username"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BTN = (By.XPATH, '//*[@id="password"]')

    def navigate_to_login_page(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def username(self, username):
        username = self.driver.find_element(*self.USERNAME)
        username.send_keys(username)

    def password(self, password):
        password = self.driver.find_element(*self.PASSWORD)
        password.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def current_url(self):
        print(self.driver.current_url)

    def login_user(self, username, password):
        self.username(username)
        self.password(password)
        self.click_login_button()
