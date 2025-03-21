import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage


def test_buy_product(set_up):
    """Тест по покупке товара, включает в себя
    авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки"""

    options = webdriver.FirefoxOptions()
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    #driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    login = LoginPage(driver)
    login.authorization()   # Запуск метода авторизации пользователя

    mp = MainPage(driver)
    mp.select_products_1()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = ClientInformationPage(driver)
    cip.input_information()

    p = PaymentPage(driver)
    p.payment()

    f = FinishPage(driver)
    f.finish()

    time.sleep(3)
    driver.quit()