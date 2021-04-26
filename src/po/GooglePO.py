from selenium.webdriver.common.keys import Keys


class GooglePO:
    def open_google(self, driver):
        driver.get("https://www.google.com")

    def get_google_title(self, driver):
        return driver.title

    def search(self, driver, term):
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys(term)
        elem.send_keys(Keys.RETURN)

    def open_first_search_result(self, driver):
        elem = driver.find_element_by_css_selector(
            'a[href^="https://github.com"]')
        elem.click()
