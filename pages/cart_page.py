from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.household_goods_page import verification_name_product, verification_price_product


class CartPage(Base):
    """Класс страницы корзины"""
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    cart_product_name = "//a[@href='/to_catalog/action_goodDesc/id_1807713/']"
    cart_product_price = "//div[@class='basket-price']"
    cart_total_price = "//div[contains(text(), 'Общая стоимость товаров: 32 500₽')]"
    make_order_button = "//a[@class='btn btn_primary basket-submit__btn']"

    # Getters
    def get_cart_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_product_name)))
    def get_cart_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_product_price)))
    def get_cart_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_total_price)))
    def get_make_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.make_order_button)))

    # Actions
    def assert_cart_product_price(self, result):
        """Проверка значения цены товара в корзине"""
        self.value_cart_product_price = self.get_cart_product_price().text
        assert f"Цена: {self.value_cart_product_price}" == result
        print('Good cart product price')
    def assert_cart_total_price(self):
        """Проверка итоговой цены товара в корзине"""
        value_cart_total_price = self.get_cart_total_price().text
        assert value_cart_total_price == f"Общая стоимость товаров: {self.value_cart_product_price}"
        print('Good total cart product price')
    def click_make_order_button(self):
        self.get_make_order_button().click()
        print('Click make order button')

    # Methods
    def product_confirmation(self):
        """Подтверждение выбора товара"""
        self.get_current_url()
        self.assert_word(self.get_cart_product_name(), verification_name_product)
        self.assert_cart_product_price(verification_price_product)
        self.assert_cart_total_price()
        self.get_screenshot()
        self.click_make_order_button()
        self.assert_url('https://vasko.ru/personal/order/delivery/')