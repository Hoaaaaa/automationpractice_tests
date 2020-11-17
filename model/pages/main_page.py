from selene import browser


class MainPage:
    __url = "http://automationpractice.com/"

    def open(self):
        browser.open_url(self.__url)
        return self
