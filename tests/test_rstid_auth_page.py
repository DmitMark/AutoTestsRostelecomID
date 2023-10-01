# python -m pytest -v --driver Chrome --driver-path \chromedriver.exe tests\test_rstid_auth_page.py
import pickle

from pages.RstID_auth_page import RstIdAuthPage

def test_open_page(web_browser):
    # проверка открытия страницы авторизации и запись кукис для прямого открытия страницы регистрации

    page = RstIdAuthPage(web_browser)
    page.wait_page_loaded(timeout=10)

    pickle.dump(page.get_cookies(), open('my_cookies.txt', 'wb'))

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth' in page.get_current_url()
    assert 'Авторизация' in page.get_page_source()

def test_login_valid_email(web_browser):
    # проверка авторизации по валидной почте

    page = RstIdAuthPage(web_browser)

    page.tab_email.click()
    page.username.send_keys('owcaf@mailto.plus')
    page.password.send_keys('Test1234567')
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()
    assert 'Учетные данные' in page.get_page_source()

def test_login_invalid_email(web_browser):
    # проверка авторизации при использовании незарегистрированной почты

    page = RstIdAuthPage(web_browser)

    page.tab_email.click()
    page.username.send_keys('sddfgg@mail.com')
    page.password.send_keys('Test1234567')
    page.btn_login.click()

    assert 'Неверный логин или пароль' in page.get_page_source()

def test_login_valid_number(web_browser):
    # проверка авторизации испольуя валидный номер телефона

    page = RstIdAuthPage(web_browser)

    page.tab_number.click()
    page.username.send_keys('+7 456 456-45-64')
    page.password.send_keys('Test1234567')
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()
    assert 'Учетные данные' in page.get_page_source()

def test_login_invalid_number(web_browser):
    # проверка авторизации используя незарегистрированный номер

    page = RstIdAuthPage(web_browser)

    page.tab_number.click()
    page.username.send_keys('+7 999 456-45-64')
    page.password.send_keys('Test12345676465')
    page.btn_login.click()

    assert 'Неверный логин или пароль' in page.get_page_source()

def test_login_valid_login(web_browser):
    # проверка авторизации используя валиднй логин

    page = RstIdAuthPage(web_browser)

    page.tab_login.click()
    page.username.send_keys('validtest')
    page.password.send_keys('Test1234567')
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()
    assert 'Учетные данные' in page.get_page_source()

def test_login_invalid_login(web_browser):
    # проверка авториации используя невалидный логин

    page = RstIdAuthPage(web_browser)

    page.tab_login.click()
    page.username.send_keys('invalidtest')
    page.password.send_keys('Test1234567')
    page.btn_login.click()

    assert 'Неверный логин или пароль' in page.get_page_source()

def test_login_valid_ls(web_browser):
    # проверка авторизации используя валидный лицевой счет

    page = RstIdAuthPage(web_browser)

    page.tab_ls.click()
    page.username.send_keys('654565487979')
    page.password.send_keys('Test1234567')
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()
    assert 'Учетные данные' in page.get_page_source()

def test_login_invalid_ls(web_browser):
    # проверка авторизации используя невалидный лицевой счет

    page = RstIdAuthPage(web_browser)

    page.tab_ls.click()
    page.username.send_keys('79789654565487979')
    page.password.send_keys('Test1234567')
    page.btn_login.click()

    assert 'Неверный логин или пароль' in page.get_page_source()

def test_login_invalid_password(web_browser):
    # проверка авторизации по валидной почте и не валидном пароле

    page = RstIdAuthPage(web_browser)

    page.tab_email.click()
    page.username.send_keys('owcaf@mailto.plus')
    page.password.send_keys('Test123456764564')
    page.btn_login.click()

    assert 'Неверный логин или пароль' in page.get_page_source()

def test_auto_choice_auth_date(web_browser):
    # автоматическое переключение таба выбора аутентификации

    page = RstIdAuthPage(web_browser)

    page.username.send_keys('owcaf@mailto.plus')
    page.password.send_keys('Test1234567')
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()
    assert 'Учетные данные' in page.get_page_source()


def test_go_page_forgot_pass(web_browser):
    # проверка перехода на страницу восстановления пароля

    page = RstIdAuthPage(web_browser)
    page.btn_forgot_pass.click()

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials' in page.get_current_url()
    assert 'Восстановление пароля' in page.get_page_source()


def test_go_to_page_registr(web_browser):
    # проверка перехода на страницу регитрации

    page = RstIdAuthPage(web_browser)
    page.btn_register.click()

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration' in page.get_current_url()
    assert 'Регистрация' in page.get_page_source()

def test_go_to_help(web_browser):
    # проверка перехода на страницу помощи

    page = RstIdAuthPage(web_browser)
    page.btn_help.click()

    assert 'Ваш безопасный ключ к сервисам Ростелекома' in page.get_page_source()