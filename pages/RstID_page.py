from pages.base import WebPage
from pages.elements import WebElement

class RstIdPage(WebPage):

    def __init__(self, web_driver, url = ''):
        url = 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    tab_number = WebElement(id = 't-btn-tab-phone')
    tab_email = WebElement(id = 't-btn-tab-mail')
    tab_login = WebElement(id = 't-btn-tab-login')
    tab_ls = WebElement(id = 't-btn-tab-ls')

    username = WebElement(id = 'username')
    password = WebElement(id = 'password')

    btn_login = WebElement(id = 'kc-login')
    btn_forgot_pass = WebElement(id = 'forgot_password')
    btn_register = WebElement(id = 'kc-register')