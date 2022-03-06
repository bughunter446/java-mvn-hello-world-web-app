from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest


target_url = "http://test-server:8080/"

print("########## Running the Selenium Script ##########")

@pytest.fixture(scope="session")
def get_driver():
    global driver
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield
    driver.close()

@pytest.mark.usefixtures("get_driver")
def test_data():
    driver.get(target_url)
    element = driver.find_element_by_tag_name("h2")
    print("########## Checking for Hello World on the page ##########")
    assert element.text == "Hello World!"

@pytest.mark.usefixtures("get_driver")
def test_body():
    element = driver.find_element_by_tag_name("p")
    print("########## Checking for Body content ##########")
    assert element.text == "This is a sample application"
