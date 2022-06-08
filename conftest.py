import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавить аргумент в командную строку
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    # Взять аргумент, введенный в командной строке
    browser_language = request.config.getoption("language")

    options = Options()
    # Добавить новый язык в конфигурацию браузера
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)

    yield browser

    print("\nquit browser..")
    browser.quit()
