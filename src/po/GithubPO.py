from selenium.webdriver.common.keys import Keys


class GithubPO:
    def get_page_source(self, driver):
        return driver.page_source
