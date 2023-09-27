# python -m pytest -v --driver Chrome --driver-path \chromedriver.exe tests

from pages.RstID_page import RstIdPage

def test_open_page(web_browser):

    page = RstIdPage(web_browser)

    assert page.get_current_url() == 'https://b2c....ount_b2c/page'

def test_login_valid_email(web_browser):

    page = RstIdPage(web_browser)

    page.tab_email.click()
    page.username.send_keys('owcaf@mailto.plus')
    page.password.send_keys('Test123456')
    page.btn_login.click()

    assert page.get_current_url() == 'https://b2c....account_b2c/#/'

def test_login_invalid_email(web_browser):

    page = RstIdPage(web_browser)

    page.tab_email.click()
    page.username.send_keys('sddfgg')
    page.password.send_keys('Test123456')
    page.btn_login.click()


    assert 'Неверный логин или пароль' in page.get_page_source()

def test_go_page_forgot_pass(web_browser):

    page = RstIdPage(web_browser)
    page.btn_forgot_pass.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=fDKtZVFrLqI'

def test_go_to_page_registr(web_browser):

    page = RstIdPage(web_browser)
    page.btn_register.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=fDKtZVFrLqI'