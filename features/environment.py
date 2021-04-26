from behave import fixture, use_fixture
from selenium import webdriver
from src.po import GithubPO, GooglePO


# Thanks to https://dzone.com/articles/using-the-behave-framework-for-selenium-bdd-testin

@fixture
def selenium_browser_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    driver = webdriver.Chrome()
    context.google_po = GooglePO.GooglePO(driver)
    context.github_po = GithubPO.GithubPO(driver)
    yield context
    # -- CLEANUP-FIXTURE PART:
    driver.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
