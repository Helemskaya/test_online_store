from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class LoginPage(Base):
    """Класс содержащий локаторы и методы для страницы Авторизации"""
    def __init__(self, driver):
        super().__init__(driver)

    url = 'https://vasko.ru/'  # url тестируемого сайта
    login_test_user = 'maria@google.com'
    password_all = '123456'

    # Locators
    login_button = "//a[@id='loginBtn']"
    user_name = "//input[@id='loginInput']"
    password = "//input[@id='passwordInput']"
    authorization_button = "(//button[@class='btn btn_primary'])[1]"
    user_preview_button = "//a[@id='userPreviewBtn']"
    test_word = "//b[contains(text(), 'Выход')]"

    # Getters
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def get_authorization_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.authorization_button)))
    def get_user_preview_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_preview_button)))

    def get_test_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.test_word)))

    # Actions
    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Input user name')
    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')
    def click_authorization_button(self):
        self.get_authorization_button().click()
        print('Click authorization button')
    def click_user_preview_button(self):
        self.get_user_preview_button().click()
        print('Click user preview button')

    # Methods
    def authorization(self):
        """Авторизация в системе"""
        self.driver.get(self.url)
        self.driver.maximize_window()   # РАСКОМЕНТИТЬ НИЖЕ!!!
        self.get_current_url()
        self.click_login_button()
        self.input_user_name(self.login_test_user)    # вызов метода по вводу информации в поле Логин
        self.input_password(self.password_all)   # вызов метода по вводу информации в поле Пароль
        self.click_authorization_button()   # клик по кнопке Войти
        self.click_user_preview_button()
        self.assert_word(self.get_test_word(), 'Выход')
