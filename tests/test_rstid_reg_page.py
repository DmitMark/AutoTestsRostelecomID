# python -m pytest -v --driver Chrome --driver-path \chromedriver.exe tests\test_rstid_reg_page.py

from pages.RstID_registr_page import RstIdRegPage

# def test_reg_with_valid_data(web_browser):
#     # регистрация валидными данными (тест закомментирован, чтобы не плодить множество
#     # учеток. для этого теста нужен дополнительно метод для удаления учетной записи
#
#     page = RstIdRegPage(web_browser)
#     page.btn_register.click()
#     # переход на страницу регистрации
#
#
#     page.first_name.send_keys('Иван')
#     page.last_name.send_keys('Иванов')
#     page.address('enwowun@mailto.plus')
#     page.password('123Test456')
#     page.password_confirm('123Test456')
#
#     page.btn_reg.click()
#
#     assert page.get_current_url() == ''

def test_reg_without_data(web_browser):
    # попытка регистрации с пустыми полями(граничное значение)

    page = RstIdRegPage(web_browser)
    page.btn_register.click()
    # переход на страницу регистрации

    page.btn_reg.click()
    page.screenshot('test_reg_without_data')

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.get_page_source()
    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.get_page_source()
    assert 'Длина пароля должна быть не менее 8 символов' in page.get_page_source()

def test_reg_with_invalid_first_name(web_browser):
    # регистрация с именем на латинице

    page = RstIdRegPage(web_browser)
    page.btn_register.click()
    # переход на страницу регистрации


    page.first_name.send_keys('Ivan')
    page.last_name.send_keys('Иванов')
    page.address.send_keys('enwowun@mailto.plus')
    page.password.send_keys('123Test456')
    page.password_confirm.send_keys('123Test456')

    page.btn_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.get_page_source()


def test_reg_with_invalid_first_name2(web_browser):
    # регистрация при имени больше 30 символов(31, граничное значение)

    page = RstIdRegPage(web_browser)
    page.btn_register.click()
    # переход на страницу регистрации

    page.first_name.send_keys('ИванИванИванИванИванИванИванИва')
    page.last_name.send_keys('Иванов')
    page.address.send_keys('enwowun@mailto.plus')
    page.password.send_keys('123Test456')
    page.password_confirm.send_keys('123Test456')

    page.btn_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.get_page_source()

def test_reg_with_invalid_last_name(web_browser):
    # регистрация при фамилии на латинице

    page = RstIdRegPage(web_browser)
    page.btn_register.click()
    # переход на страницу регистрации

    page.first_name.send_keys('Иван')
    page.last_name.send_keys('Ivanov')
    page.address.send_keys('enwowun@mailto.plus')
    page.password.send_keys('123Test456')
    page.password_confirm.send_keys('123Test456')

    page.btn_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.get_page_source()


def test_reg_with_invalid_last_name2(web_browser):
    # регистрация при фамилии больше 30 символов(31, граничное значение)

    page = RstIdRegPage(web_browser)
    page.btn_register.click()
    # переход на страницу регистрации

    page.first_name.send_keys('Иван')
    page.last_name.send_keys('ИвановИвановИвановИвановИвановИ')
    page.address.send_keys('enwowun@mailto.plus')
    page.password.send_keys('123Test456')
    page.password_confirm.send_keys('123Test456')

    page.btn_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.get_page_source()

def test_reg_with_invalid_number(web_browser):
    # регистрация при невалидном номере телефона

    page = RstIdRegPage(web_browser)
    page.btn_register.click()
    # переход на страницу регистрации

    page.first_name.send_keys('Иван')
    page.last_name.send_keys('Иванов')
    page.address.send_keys('+69848464646648')
    page.password.send_keys('123Test456')
    page.password_confirm.send_keys('123Test456')

    page.btn_reg.click()

    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.get_page_source()


def test_reg_with_invalid_mail(web_browser):
    # регистрация при невалидном адресе почты)

    page = RstIdRegPage(web_browser)
    page.btn_register.click()
    # переход на страницу регистрации

    page.first_name.send_keys('Иван')
    page.last_name.send_keys('Иванов')
    page.address.send_keys('asdfsdfg@sdfsdg@dsfg@')
    page.password.send_keys('123Test456')
    page.password_confirm.send_keys('123Test456')

    page.btn_reg.click()

    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.get_page_source()

def test_reg_with_invalid_password(web_browser):
    # длина пароля менее 8 символов(7)

    page = RstIdRegPage(web_browser)
    page.btn_register.click()
    # переход на страницу регистрации

    page.first_name.send_keys('Иван')
    page.last_name.send_keys('Иванов')
    page.address.send_keys('enwowun@mailto.plus')
    page.password.send_keys('123Test')
    page.password_confirm.send_keys('123Test')

    page.btn_reg.click()

    assert 'Длина пароля должна быть не менее 8 символов' in page.get_page_source()

def test_reg_with_invalid_password2(web_browser):
    # пароль с буквами из кирилицы

    page = RstIdRegPage(web_browser)
    page.btn_register.click()
    # переход на страницу регистрации

    page.first_name.send_keys('Иван')
    page.last_name.send_keys('Иванов')
    page.address.send_keys('enwowun@mailto.plus')
    page.password.send_keys('123456Тест')
    page.password_confirm.send_keys('123456Тест')

    page.btn_reg.click()

    assert 'Пароль должен содержать только латинские буквы' in page.get_page_source()


def test_reg_with_invalid_password_confirm(web_browser):
    # при несовпадающих паролях

    page = RstIdRegPage(web_browser)
    page.btn_register.click()
    # переход на страницу регистрации

    page.first_name.send_keys('Иван')
    page.last_name.send_keys('Иванов')
    page.address.send_keys('enwowun@mailto.plus')
    page.password.send_keys('123Test456')
    page.password_confirm.send_keys('456Test65')

    page.btn_reg.click()

    assert 'Пароли не совпадают' in page.get_page_source()