class BrowserGeneral:

    @staticmethod
    def open_page(browser, url):
        browser.get(url)

    @staticmethod
    def maximize_window(browser):
        browser.maximize_window()

    @staticmethod
    def vertical_scroll(browser, pixel):
        browser.execute_script("window.scrollBy(0,{})".format(pixel))

    @staticmethod
    def press_enter(ele):
        ele.send_keys('\ue007')
