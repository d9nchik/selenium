from selenium.webdriver.common.keys import Keys
import src.po.DefaultPO as d_po


class GooglePO(d_po.DefaultPO):
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
