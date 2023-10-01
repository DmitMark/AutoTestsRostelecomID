import os, pickle

from pages.base import WebPage
from pages.elements import WebElement

class RstIdRegPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=aNdGAddiHHI'
        super().__init__(web_driver, url)
        for cookie in pickle.load(open(f'my_cookies.txt', 'rb')):
            web_driver.add_cookies(cookie)
        web_driver.refresh()

    first_name = WebElement(name='firstName')
    last_name = WebElement(name='lastName')
    address = WebElement(id='address')
    password = WebElement(id='password')
    password_confirm = WebElement(id='password-confirm')


    btn_register = WebElement(name='register')