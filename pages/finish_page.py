import allure
from base.base_class import Base
from utilities.logger import Logger


class FinishPage(Base):
    """Класс финальной страницы сайта"""
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    # Getters

    # Actions

    # Methods
    def finish(self):
        """Скриншот финальной страницы"""
        with allure.step("Finish"):
            Logger.add_start_steep(method='finish')
            self.get_current_url()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='finish')