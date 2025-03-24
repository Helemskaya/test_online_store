import allure
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

fake = Faker("en_US")

class ClientInformationPage(Base):
    """Класс страницы с информацией пользователя"""
    def __init__(self, driver):
        super().__init__(driver)

    fake_contact_person = fake.name_female()
    fake_email = fake.email()
    fake_phone_number = '9876543210124'

    # Locators
    contact_person = "//input[@id='input-15']"
    email = "//input[@id='input-16']"
    phone_number = "//input[@id='input-17']"
    forth_button = "//button[@class='btn btn_primary btn_wide show-on-tablet']"

    # Getters
    def get_contact_person(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.contact_person)))
    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))
    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))
    def get_forth_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.forth_button)))

    # Actions
    def input_contact_person(self, contact_person):
        self.get_contact_person().send_keys(contact_person)
        print('Input contact person')
    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Input email')
    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print('Input phone number')
    def click_forth_button(self):
        self.get_forth_button().click()
        print('Click forth button')

    # Methods
    def input_contact_information(self):
        """Заполнить контактную информацию клиента"""
        with allure.step("Input contact information"):
            Logger.add_start_steep(method='input_contact_information')
            self.get_current_url()
            self.input_contact_person(self.fake_contact_person)
            self.input_email(self.fake_email)
            self.input_phone_number(self.fake_phone_number)
            self.click_forth_button()
            self.assert_url('https://vasko.ru/personal/order/confirm/')
            Logger.add_end_step(url=self.driver.current_url, method='input_contact_information')