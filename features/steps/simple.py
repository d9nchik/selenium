from behave import *
from selenium.webdriver.common.keys import Keys


# More about scenario outline 👀 here https://jenisys.github.io/behave.example/tutorials/tutorial04.html

@given("I have access to the internet")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("https://www.google.com")
    assert "Google" in context.driver.title


@step('I have entered {nickname} in google search')
def step_impl(context, nickname):
    """
    :type context: behave.runner.Context
    """
    assert nickname != ''
    elem = context.driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(nickname)
    elem.send_keys(Keys.RETURN)


@step('page contains {realName}')
def step_impl(context, realName):
    """
    :type context: behave.runner.Context
    """
    assert realName in context.driver.page_source


@when("I click on first github link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elem = context.driver.find_element_by_css_selector(
        'a[href^="https://github.com"]')
    elem.click()


@then('it would contain {learningSkills}')
def step_impl(context, learningSkills):
    """
    :type context: behave.runner.Context
    """
    assert learningSkills in context.driver.page_source
