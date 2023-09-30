from pages.base import WebPage
from pages.elements import WebElement

class RstIdResetPage(WebPage):

    def __init__(self, web_driver, url = ''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=AyPIZqPgoGY'
        super().__init__(web_driver, url)

    tab_number = WebElement(id = 't-btn-tab-phone')
    tab_email = WebElement(id = 't-btn-tab-mail')
    tab_login = WebElement(id = 't-btn-tab-login')
    tab_ls = WebElement(id = 't-btn-tab-ls')

    username = WebElement(id = 'username')
    btn_reset = WebElement(id = 'reset')
    btn_back_to_login = WebElement(id = 'reset-back')