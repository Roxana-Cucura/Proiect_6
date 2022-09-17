
from pages.login_page import LogInPage
from pages.home_page import HomePage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.sign_in_page = LogInPage()
    context.forgot_password_page = HomePage()



def after_all(context):
    context.browser.close()
