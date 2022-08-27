import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrom")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None

    yield browser
    print("\nquit browser..")
    browser.quit()
