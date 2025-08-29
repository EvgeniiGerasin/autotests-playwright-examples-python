from pages.auth.tasks import TaskAuth
from pages.main_page.tasks import TaskMainPage
from data.data import Stands

from playwright.sync_api._generated import Browser, BrowserContext, Page
from allure import epic, title, step


@epic('Главная страница сайта')
class TestMainPage:

    @title('Открытие страницы')
    def test_open_page(self, browser: Browser, context: BrowserContext, page: Page):
        page.goto(Stands.url)
        with step('Вход в систему'):
            task_auth = TaskAuth(page=page)
            task_auth.check_open_page()
            task_auth.login()
        with step('Проверка открытия окна'):
            task = TaskMainPage(page=page)
            task.check_open_main_page()

    @title('Выход из системы')
    def test_logout(self, browser: Browser, context: BrowserContext, page: Page):
        page.goto(Stands.url)
        with step('Вход в систему'):
            task_auth = TaskAuth(page=page)
            task_auth.check_open_page()
            task_auth.login()
        with step('Проверка открытия окна'):
            task_main = TaskMainPage(page=page)
            task_main.check_open_main_page()
        with step('Выход из системы'):
            task_main.logout()
        with step('Проверка выхода'):
            task_auth.check_open_page()
