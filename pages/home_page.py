from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager import chrome
from browser import Browser

class HomePage(Browser):
    FORM = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    FORGOT_PASSWORD = (By.XPATH, '//*[@id="content"]/ul/li[20]/a')
    GEOLOCATION = (By.XPATH, '//*[@id="content"]/ul/li[23]/a')


    def navigate_to_form(self):
        self.driver.get('https://the-internet.herokuapp.com/')
        sleep(2)
        self.driver.find_element(*self.FORM).click()

    def navigate_to_forgot_password(self):
        self.driver.get('https://the-internet.herokuapp.com/forgot_password')
        sleep(2)
        self.driver.find_element(*self.FORGOT_PASSWORD).click()

    def navigate_to_geolocation(self):
        self.driver.get('https://the-internet.herokuapp.com/geolocation')
        sleep(2)
        self.driver.find_element(*self.GEOLOCATION).click()

