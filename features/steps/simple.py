from behave import *
from selenium.webdriver.common.keys import Keys

# More about scenario outline 👀 here https://jenisys.github.io/behave.example/tutorials/tutorial04.html
from src.po import GooglePO as go
from src.po import GithubPO as git


@given("I have access to the internet")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    go.GooglePO().open_google(context.driver)
    assert "Google" in go.GooglePO().get_google_title(context.driver)


@step('I have entered {nickname} in google search')
def step_impl(context, nickname):
    """
    :type context: behave.runner.Context
    """
    assert nickname != ''
    go.GooglePO().search(context.driver, nickname)

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
    go.GooglePO().open_first_search_result(context.driver)


@then('it would contain {learningSkills}')
def step_impl(context, learningSkills):
    """
    :type context: behave.runner.Context
    """
    assert learningSkills in git.GithubPO().get_page_source(context.driver)
