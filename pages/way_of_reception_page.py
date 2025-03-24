import allure
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

fake = Faker("en_US")

class WayReceptionPage(Base):
    """Класс страницы с информацией о способе получения товара"""
    def __init__(self, driver):
        super().__init__(driver)

    fake_profile_name = fake.name()
    fake_street = fake.street_name()
    fake_house_number = fake.building_number()

    # Locators
    profile_name = "//input[@id='input-profile-name']"
    street = "//input[@id='input-7']"
    house_number = "//input[@id='input-8']"
    continue_button = "//button[@class='btn btn_primary btn_wide show-on-tablet']"

    # Getters
    def get_profile_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_name)))
    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street)))
    def get_house_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.house_number)))
    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions
    def input_profile_name(self, profile_name):
        self.get_profile_name().send_keys(profile_name)
        print('Input profile name')
    def input_street(self, street):
        self.get_street().send_keys(street)
        print('Input street')
    def input_house_number(self, house_number):
        self.get_house_number().send_keys(house_number)
        print('Input house number')
    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click continue button')

    # Methods
    def input_reception_information(self):
        """Заполнить информацию о способе получения"""
        with allure.step("Input reception information"):
            Logger.add_start_steep(method='input_reception_information')
            self.get_current_url()
            self.input_profile_name(self.fake_profile_name)
            self.input_street(self.fake_street)
            self.input_house_number(self.fake_house_number)
            self.click_continue_button()
            self.assert_url('https://vasko.ru/personal/order/contacts/')
            Logger.add_end_step(url=self.driver.current_url, method='input_reception_information')