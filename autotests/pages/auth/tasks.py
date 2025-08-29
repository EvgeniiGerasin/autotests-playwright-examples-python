from pages.auth.locators import Locators
from autotests.pages.task_base import TaskBase
from data.data import Users


class TaskAuth(TaskBase):

    def login(self, login: str = Users.login, password: str = Users.password):

        self.p.locator(Locators.input_login).fill(login)
        self.p.locator(Locators.input_password).fill(password)
        self.p.locator(Locators.button_login).click()

    def check_open_page(self):

        self.expect(self.p.locator(Locators.button_login)).to_be_visible()
