from selenium.webdriver.common.keys import Keys


class GooglePO:

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def open_google(self):
        self.driver.get("https://www.google.com")

    def get_google_title(self):
        return self.driver.title

    def search(self, term):
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys(term)
        elem.send_keys(Keys.RETURN)

    def open_first_search_result(self):
        elem = self.driver.find_element_by_css_selector(
            'a[href^="https://github.com"]')
        elem.click()

    def get_page_source(self):
        return self.driver.page_source
