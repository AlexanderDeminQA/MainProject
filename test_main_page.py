from .page.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    pages = MainPage(browser, link)
    pages.open()
    pages.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_should_be_login_url(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_should_be_register_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_register_form()
