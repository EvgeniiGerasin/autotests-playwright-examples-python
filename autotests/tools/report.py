import allure
from playwright.sync_api._generated import Page


class Report:

    def __init__(self, page: Page) -> None:
        self.p: Page = page

    def add_screenshot_to_report(self, name: str = 'Скриншот экрана'):
        self.p.wait_for_load_state(state='domcontentloaded')
        allure.attach(
            body=self.p.screenshot(type='png'),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
