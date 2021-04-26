from behave import *


@given("I have access to the internet")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.google_po.open_google()
    assert "Google" in context.google_po.get_google_title()


@step('I have entered {nickname} in google search')
def step_impl(context, nickname):
    """
    :param nickname:
    :type context: behave.runner.Context
    """
    assert nickname != ''
    context.google_po.search(nickname)


@step('page contains {real_name}')
def step_impl(context, real_name):
    """
    :param real_name: 
    :type context: behave.runner.Context
    """
    assert real_name in context.google_po.get_page_source()


@when("I click on first github link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.google_po.open_first_search_result()


@then('it would contain {learning_skills}')
def step_impl(context, learning_skills):
    """
    :param learning_skills:
    :type context: behave.runner.Context
    """
    assert learning_skills in context.github_po.get_page_source()
