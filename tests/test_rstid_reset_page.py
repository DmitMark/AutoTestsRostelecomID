# python -m pytest -v --driver Chrome --driver-path \chromedriver.exe tests\test_rstid_reset_page.py

from pages.RstID_reset_page import RstIdResetPage

def test_reset_valid_email(web_browser):
    # возможность сбросить пороль не вводя символы из капчи

    page = RstIdResetPage(web_browser)
    page.username.send_keys('sddfgg')
    page.btn_reset.click()

    assert 'Неверный логин или текст с картинки' in page.get_page_source()

def test_back_to_login(web_browser):
    # возврат на страницу авторизации

    page = RstIdResetPage(web_browser)
    page.btn_back_to_login.click()

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate' in page.get_current_url()

def test_go_to_help(web_browser):
    # проверка перехода на страницу помощи

    page = RstIdResetPage(web_browser)
    page.btn_help.click()

    assert 'Ваш безопасный ключ к сервисам Ростелекома' in page.get_page_source()




