from pages.auth.tasks import TaskAuth
from pages.main_page.tasks import TaskMainPage
from data.data import Stands

from playwright.sync_api._generated import Browser, BrowserContext, Page
from allure import epic, title, step


@epic('Страница входа')
class TestMainPage:

    @title('Открытие страницы')
    def test_open_page(self, browser: Browser, context: BrowserContext, page: Page):
        page.goto(Stands.url)
        task = TaskAuth(page=page)
        task.check_open_page()

    @title('Аутентификация')
    def test_auth(self, browser: Browser, context: BrowserContext, page: Page):
        page.goto(Stands.url)
        with step('Вход в систему'):
            task_auth = TaskAuth(page=page)
            task_auth.check_open_page()
            task_auth.login()
        with step('Проверка входа'):
            task_main_page = TaskMainPage(page=page)
            task_main_page.check_open_main_page()
