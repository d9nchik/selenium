from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def selenium_browser_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.driver = webdriver.Chrome('./chromedriver')
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
