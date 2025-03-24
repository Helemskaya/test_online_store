import datetime

class Base:
    """Базовый класс, содержащий универсальные методы """
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод проверки url"""
        get_url = self.driver.current_url
        print("Current url " + get_url)

    def assert_word(self, word, result):
        """Проверка значения текста"""
        value_word = word.text
        assert value_word == result
        print('Good value word')

    def get_screenshot(self):
        """Создание скриншота"""
        name_screenshot = f".\\screen\\screenshot_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".png"
        self.driver.save_screenshot(name_screenshot)
        print('Screenshot taken')

    def assert_url(self, result):
        """Проверка корректности URL"""
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')

