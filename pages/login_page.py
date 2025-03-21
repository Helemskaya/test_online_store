from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):
    """Класс содержащий локаторы и методы для страницы Авторизации"""
    def __init__(self, driver):
        super().__init__(driver)

    url = 'https://www.pleza.ru/'  # url тестируемого сайта
    login_standart_user = 'maria'
    password_all = '123456'

    # Locators
    log_in = "//a[@href='/login/?backurl=%2F']"
    user_name = "//input[@name='USER_LOGIN']"
    password = "//input[@name='USER_PASSWORD']"
    login_button = "//input[@value='Войти']"
    main_word = "//a[@href='/personal/profile/?backurl=%2F']"

    # Getters
    def get_log_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.log_in)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def click_log_in(self):
        self.get_log_in().click()
        print('Click log in')

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Input user name')
    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')
    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    # Methods
    def authorization(self):
        """Авторизация в системе"""
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_log_in()
        self.input_user_name(self.login_standart_user)    # вызов метода по вводу информации в поле Логин
        self.input_password(self.password_all)   # вызов метода по вводу информации в поле Пароль
        self.click_login_button()   # клик по кнопке Войти
        self.assert_word(self.get_main_word(), 'Мария')
