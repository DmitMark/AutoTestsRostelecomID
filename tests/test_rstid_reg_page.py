# python -m pytest -v --driver Chrome --driver-path \chromedriver.exe tests\test_rstid_reg_page.py
import pickle

from pages.RstID_registr_page import RstIdRegPage

# def test_reg_with_valid_data(web_browser):
#
#     page = RstIdRegPage(web_browser)
#     page.first_name.send_keys('Иван')
#     page.last_name.send_keys('Иванов')
#     page.address('enwowun@mailto.plus')
#     page.password('123test456')
#     page.password_confirm('123test456')
#
#     page.btn_register.click()
#
#     assert page.get_current_url() == ''
#
# def test_reg_without_data(web_browser):
#     page = RstIdRegPage(web_browser)
#
#     page.btn_register.click()
#
#     assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.get_page_source()
#     assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.get_page_source()
#     assert 'Длина пароля должна быть не менее 8 символов' in page.get_page_source()
#
def test_reg_with_invalid_first_name(web_browser):
    # при имени на латинице


    page = RstIdRegPage(web_browser)

    page.first_name.send_keys('Ivan')
    page.last_name.send_keys('Иванов')
    page.address('enwowun@mailto.plus')
    page.password('123test456')
    page.password_confirm('123test456')

    page.btn_register.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.get_page_source()


# def test_reg_with_invalid_first_name2(web_browser):
#     # при имени больше 30 символов(31)
#
#     page = RstIdRegPage(web_browser)
#     page.first_name.send_keys('ИванИванИванИванИванИванИванИва')
#     page.last_name.send_keys('Иванов')
#     page.address('enwowun@mailto.plus')
#     page.password('123test456')
#     page.password_confirm('123test456')
#
#     page.btn_register.click()
#
#     assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.get_page_source()
#
# def test_reg_with_invalid_last_name(web_browser):
#     # при фамилии на латинице
#
#     page = RstIdRegPage(web_browser)
#     page.first_name.send_keys('Иван')
#     page.last_name.send_keys('Ivanov')
#     page.address('enwowun@mailto.plus')
#     page.password('123test456')
#     page.password_confirm('123test456')
#
#     page.btn_register.click()
#
#     assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.get_page_source()
#
#
# def test_reg_with_invalid_last_name2(web_browser):
#     # при фамилии больше 30 символов
#
#     page = RstIdRegPage(web_browser)
#     page.first_name.send_keys('Иван')
#     page.last_name.send_keys('ИвановИвановИвановИвановИвановИ')
#     page.address('enwowun@mailto.plus')
#     page.password('123test456')
#     page.password_confirm('123test456')
#
#     page.btn_register.click()
#
#     assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.get_page_source()
#
# def test_reg_with_invalid_number(web_browser):
#
#     page = RstIdRegPage(web_browser)
#     page.first_name.send_keys('Иван')
#     page.last_name.send_keys('Иванов')
#     page.address('+69848464646648')
#     page.password('123test456')
#     page.password_confirm('123test456')
#
#     page.btn_register.click()
#
#     assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.get_page_source()
#
#
# def test_reg_with_invalid_mail(web_browser):
#     page = RstIdRegPage(web_browser)
#     page.first_name.send_keys('Иван')
#     page.last_name.send_keys('Иванов')
#     page.address('asdfsdfg@sdfsdg@dsfg@')
#     page.password('123test456')
#     page.password_confirm('123test456')
#
#     page.btn_register.click()
#
#     assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.get_page_source()
#
# def test_reg_with_invalid_password(web_browser):
#     # длина пароля менее 8 символов(7)
#
#     page = RstIdRegPage(web_browser)
#     page.first_name.send_keys('Иван')
#     page.last_name.send_keys('Иванов')
#     page.address('enwowun@mailto.plus')
#     page.password('123test')
#     page.password_confirm('123test')
#
#     page.btn_register.click()
#
#     assert 'Длина пароля должна быть не менее 8 символов' in page.get_page_source()
#
# def test_reg_with_invalid_password2(web_browser):
#     # пароль с бквами из кирилицы
#
#     page = RstIdRegPage(web_browser)
#     page.first_name.send_keys('Иван')
#     page.last_name.send_keys('Иванов')
#     page.address('enwowun@mailto.plus')
#     page.password('123test')
#     page.password_confirm('123test')
#
#     page.btn_register.click()
#
#     assert 'Длина пароля должна быть не менее 8 символов' in page.get_page_source()
#
#
# def test_reg_with_invalid_password_confirm(web_browser):
#     # длина пароля менее 8 символов(7)
#
#     page = RstIdRegPage(web_browser)
#     page.first_name.send_keys('Иван')
#     page.last_name.send_keys('Иванов')
#     page.address('enwowun@mailto.plus')
#     page.password('123test456')
#     page.password_confirm('456test65')
#
#     page.btn_register.click()
#
#     assert 'Пароли не совпадают' in page.get_page_source()