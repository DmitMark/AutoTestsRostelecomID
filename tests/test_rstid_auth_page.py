# python -m pytest -v --driver Chrome --driver-path \chromedriver.exe tests

from pages.RstID_auth_page import RstIdAuthPage

def test_open_page(web_browser):

    page = RstIdAuthPage(web_browser)
    page.wait_page_loaded(timeout=10)

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth' in page.get_current_url()
    assert 'Авторизация' in page.get_page_source()

def test_login_valid_email(web_browser):

    page = RstIdAuthPage(web_browser)

    page.tab_email.click()
    page.username.send_keys('owcaf@mailto.plus')
    page.password.send_keys('Test1234567')
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()
    assert 'Учетные данные' in page.get_page_source()

def test_login_invalid_email(web_browser):

    page = RstIdAuthPage(web_browser)

    page.tab_email.click()
    page.username.send_keys('sddfgg')
    page.password.send_keys('Test1234567')
    page.btn_login.click()


    assert 'Неверный логин или пароль' in page.get_page_source()

def test_go_page_forgot_pass(web_browser):

    page = RstIdAuthPage(web_browser)
    page.btn_forgot_pass.click()

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials' in page.get_current_url()
    assert 'Восстановление пароля' in page.get_page_source()


def test_go_to_page_registr(web_browser):

    page = RstIdAuthPage(web_browser)
    page.btn_register.click()

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration' in page.get_current_url()
    assert 'Регистрация' in page.get_page_source()

def test_go_to_help(web_browser):

    page = RstIdAuthPage(web_browser)
    page.btn_help.click()

    assert 'Ваш безопасный ключ к сервисам Ростелекома' in page.get_page_source()