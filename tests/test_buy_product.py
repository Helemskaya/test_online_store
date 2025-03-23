import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.cart_page import CartPage
from pages.way_of_reception_page import WayReceptionPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.household_goods_page import HouseholdGoodsPage
from pages.сontact_information_page import ClientInformationPage

def test_buy_product(set_up):
    """Тест по покупке товара, включает в себя
    авторизацию, выбор товара, заполнение данных получателя"""

    options = webdriver.FirefoxOptions()
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    login = LoginPage(driver)
    login.authorization()   # Запуск метода авторизации пользователя

    hgp = HouseholdGoodsPage(driver)
    hgp.select_washing_machines()   # Запуск метода выбора товара

    cp = CartPage(driver)
    cp.product_confirmation() # Запуск метода проверки корзины товара

    wrp = WayReceptionPage(driver)
    wrp.input_reception_information()  # Запуск метода заполнения информации о способе получения товара

    cip = ClientInformationPage(driver)
    cip.input_contact_information()   # Запуск метода заполнения контактной информации клиента

    fp = FinishPage(driver)
    fp.finish()

    time.sleep(3)
    driver.quit()