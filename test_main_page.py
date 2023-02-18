from .page.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    pages = MainPage(browser, link)
    pages.open()
    pages.go_to_login_page()




