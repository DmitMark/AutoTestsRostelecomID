
from pages.RstID_auth_page import RstIdAuthPage
from pages.elements import WebElement

class RstIdRegPage(RstIdAuthPage):


    first_name = WebElement(name='firstName')
    last_name = WebElement(name='lastName')
    address = WebElement(id='address')
    password = WebElement(id='password')
    password_confirm = WebElement(id='password-confirm')


    btn_reg = WebElement(name='register')