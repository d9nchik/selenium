from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# For detail instructions look here: 👀 https://sites.google.com/a/chromium.org/chromedriver/getting-started
# and here https://selenium-python.readthedocs.io/getting-started.html

# TODO:  before run of this project download right chrome driver
#  👉 https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome('./chromedriver')

driver.get("http://www.google.com")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("d9nich")
elem.send_keys(Keys.RETURN)
assert "Danylo Halaiko" in driver.page_source
elem = driver.find_element_by_css_selector(
    'a[href="https://github.com/d9nchik"]')
elem.click()
assert 'Ask me about Java, Python, Golang, JavaScript, Kotlin, TypeScript, C++' in driver.page_source
driver.close()
