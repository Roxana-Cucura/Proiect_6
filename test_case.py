import unittest

from pages.login_page import LogInPage
from pages.home_page import HomePage
from pages.secure_page import SecurePage
from browser import Browser



class Test(unittest.TestCase):
    sign_in_page = None

    def setUp(self):
        self.sign_in_page = LogInPage()
        self.sign_in_page.navigate_to_login_page()


    def home_page(self):
        self.sign_in_page = HomePage()
        self.sign_in_page.navigate_to_form()

    def login_page(self):
        self.sign_in_page = LogInPage()
        self.sign_in_page.navigate_to_login_page()

    def secure_page(self):
        self.sign_in_page = SecurePage()
        self.sign_in_page.navigate_to_secure_page()

    def tearDown(self):
        self.sign_in_page.close()

    def test_sign_in(self):
        pass


