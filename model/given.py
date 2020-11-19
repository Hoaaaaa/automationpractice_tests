from selene import browser


class Given:
    __url = "http://automationpractice.com/"

    def at_main_page(self):
        browser.open_url(self.__url)
