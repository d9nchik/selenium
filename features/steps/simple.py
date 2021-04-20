from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

use_step_matcher("re")

driver = webdriver.Chrome()


@given("I have access to the internet")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.get("http://www.google.com")
    assert "Gogle" in driver.title


@step("I have entered d9nich in google search")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("d9nich")
    elem.send_keys(Keys.RETURN)


@step('page contains "Danylo Halaiko"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert "Danylo Halaiko" in driver.page_source


@when("I click on first github link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elem = driver.find_element_by_css_selector(
        'a[href="https://github.com/d9nchik"]')
    elem.click()


@then("it would be d9nich github main page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert 'Ask me about Java, Python, Golang, JavaScript, Kotlin, TypeScript, C++' in driver.page_source
    driver.close()
