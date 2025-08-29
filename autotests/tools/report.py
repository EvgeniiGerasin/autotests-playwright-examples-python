import allure
from playwright.sync_api._generated import Page


class Report:

    def __init__(self, page: Page) -> None:
        self.p: Page = page

    def add_screenshot(self, name: str = 'Скриншот экрана'):
        self.p.wait_for_load_state(state='domcontentloaded')
        self.add_to_report(value=self.p.screenshot(type='png'), type='image/png', name=name)
    
    def add_to_report(self, value, type, name: str = 'Вложение',):
        """

        Args:
            value (any):
            type (str): 
                'image/png'
                'image/jpeg'
                'text/plain'
                'text/html'
                'application/json'
            name (str, optional): Defaults to 'Вложение'.
        """        
        allure.attach(
            body=value,
            name=name,
            attachment_type=type
        )
