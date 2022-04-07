from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    global driver
    if browser=="edge":
        driver=webdriver.Edge(executable_path="C:\\edgedriver_win64\\msedgedriver.exe")
        print("launching the edge browser ")
    elif browser=="chrome":
        driver=webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
        print("launching the firefox browser")
        return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return  request.config.getoption("--browser")
