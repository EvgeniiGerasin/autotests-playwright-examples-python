from pages.main_page.locators import Locators
from pages.task_base import TaskBase


class TaskMainPage(TaskBase):

    def check_open_main_page(self):
        """Проверка открытия главной страницы сайта
        """
        self.report.add_screenshot()
        self.expect(self.p.locator(Locators.title_products)).to_be_visible()

    def logout(self):

        self.p.click(Locators.button_action_menu)
        self.p.click(Locators.button_logout)
