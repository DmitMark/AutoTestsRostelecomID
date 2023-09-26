# python -m pytest -v --driver Chrome --driver-path \chromedriver.exe tests\test_rstid_page.py

from pages.RstID_page import RstIdPage

def test_open_page(web_browser):

    page = RstIdPage(web_browser)

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/'