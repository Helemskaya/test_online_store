import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

verification_name_product = 'Фронтальная стиральная машина Candy CSW4 365D/2 Steam'
verification_price_product = 'Цена: 32 500₽'

class HouseholdGoodsPage(Base):
    """Класс бытовая техника для дома"""
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    goods_for_house = "//a[@title='Товары для дома']"
    washing_machines = "(//h2[@class='catalog-sections__title'])[1]"
    test_word = "(//a[contains(text(), 'Стиральные машины с фронтальной загрузкой')])[2]"
    filter_min_price = "(//input[@name='price_min'])[2]"
    filter_max_price = "(//input[@name='price_max'])[2]"
    apply_price_filter = "(//button[@class='btn btn_outline btn_primary filter__submit'])[4]"
    checkbox_manufacturer = "(//span[@class='checkbox__box'])[29]"
    apply_manufacturer = "(//button[@class='btn btn_outline btn_primary filter__submit'])[3]"
    with_dryer = "(//a[@class='filter__option filter__option_link'])[20]"
    select_product = "//button[@id='js-BuyProductList1807713']"
    product_name = "(//a[@href='/to_catalog/action_goodDesc/id_1807713/'])[4]"
    product_price = "(//div[@class='catalog-list__price'])[1]"
    cart = "//a[@id='basketBtn']"
    go_to_cart = "(//a[@href='/personal/cart/'])[2]"

    # Getters
    def get_goods_for_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.goods_for_house)))
    def get_washing_machines(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.washing_machines)))
    def get_test_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.test_word)))
    def get_filter_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_min_price)))
    def get_filter_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_max_price)))
    def get_apply_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_price_filter)))
    def get_checkbox_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_manufacturer)))
    def get_apply_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_manufacturer)))
    def get_with_dryer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.with_dryer)))
    def get_select_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product)))
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name)))
    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    # Actions
    def click_goods_for_house(self):
        self.get_goods_for_house().click()
        print('Click goods for house')
    def click_washing_machines(self):
        self.get_washing_machines().click()
        print('Click washing machines')
    def input_filter_min_price(self, min_price):
        self.get_filter_min_price().send_keys(Keys.CONTROL + "a")
        self.get_filter_min_price().send_keys(Keys.DELETE)
        self.get_filter_min_price().send_keys(min_price)
        print('Input min price')
    def input_filter_max_price(self, max_price):
        self.get_filter_max_price().send_keys(Keys.CONTROL + "a")
        self.get_filter_max_price().send_keys(Keys.DELETE)
        self.get_filter_max_price().send_keys(max_price)
        print('Input max price')
    def click_apply_price_filter(self):
        self.get_apply_price_filter().click()
        self.get_apply_price_filter().click() # необходимо нажать второй раз для установки фильтра
        print('Click apply price filter')
    def click_checkbox_manufacturer(self):
        self.get_checkbox_manufacturer().click()
        print('Click checkbox manufacturer')
    def click_apply_manufacturer(self):
        self.get_apply_manufacturer().click()
        print('Click apply manufacturer')
    def click_with_dryer(self):
        self.get_with_dryer().click()
        print('Click with dryer')
    def click_select_product(self):
        self.get_select_product().click()
        print('Click select product')
    def click_cart(self):
        self.get_cart().click()
        print('Click cart')
    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print('Click go to cart')

    # Methods
    def select_washing_machines(self):
        """Выбор товара по установленным фильтрам"""
        with allure.step("Select washing machines"):
            Logger.add_start_steep(method='select_washing_machines')
            self.get_current_url()
            self.click_goods_for_house()
            self.click_washing_machines()
            self.assert_word(self.get_test_word(), 'Стиральные машины с фронтальной загрузкой')
            self.input_filter_min_price(30000)
            self.input_filter_max_price(35000)
            self.click_apply_price_filter()
            self.click_checkbox_manufacturer()
            self.click_apply_manufacturer()
            self.click_with_dryer()
            self.get_screenshot()
            self.assert_word(self.get_product_name(), verification_name_product)
            self.assert_word(self.get_product_price(), verification_price_product)
            self.click_select_product()
            self.click_cart()
            self.click_go_to_cart()
            self.assert_url('https://vasko.ru/personal/cart/')
            Logger.add_end_step(url=self.driver.current_url, method='select_washing_machines')
