class GithubPO:

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def get_page_source(self):
        return self.driver.page_source
