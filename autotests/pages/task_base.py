from playwright.sync_api._generated import Page
from playwright.sync_api import Expect, expect


class TaskBase:

    def __init__(self, page: Page) -> None:
        self.p: Page = page
        self.expect: Expect = expect
