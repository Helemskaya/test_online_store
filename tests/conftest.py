import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture() # добавление записи о начале и окончании теста
def set_up():
    print('\nStart test') # перед тестом
    yield
    print('\nFinish test') # после теста


@pytest.fixture(scope='module') # добавление записи о входе и выходе для модуля
def set_group():
    print('\nEnter system')
    yield
    print('\nExit system')

@pytest.fixture() # добавление записи о начале и окочании теста, открытие и закрытие браузера
def set_up_browser():
    print('\nStart test') # перед тестом

    options = webdriver.FirefoxOptions()
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    driver.maximize_window()

    yield driver

    print('\nFinish test') # после теста
    driver.quit()


