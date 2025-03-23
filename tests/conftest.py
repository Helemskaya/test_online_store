import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture() # добавление записи о начале и окончании теста
def set_up():
    print('\nStart test') # перед тестом
    yield
    print('\nFinish test') # после теста


