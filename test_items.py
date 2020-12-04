import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

def test_add_to_basket(browser):
    browser.get(link)

    basket_button = browser.find_element_by_css_selector(".btn-add-to-basket")

    time.sleep(30)

    assert basket_button is not None, "basket button not found"

