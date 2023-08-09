import pytest
import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    used_browser = testdata["browser"]
    api_login = testdata["api_login"]
    login = testdata["login"]
    password = testdata["password"]
    other_post = testdata["other_post"]


@pytest.fixture(scope="session")
def browser():
    if used_browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def authorize():
    r = requests.post(url=api_login, data={'username': login, 'password': password})
    return r.json()['token']

@pytest.fixture()
def title_in_other_post():
    return other_post


