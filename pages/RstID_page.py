from pages.base import WebPage
from pages.elements import WebElement

class RstIdPage(WebPage):

    def __init__(self, web_driver, url = ''):
        url = 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)