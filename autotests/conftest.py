from typing import Any, Generator
from playwright.sync_api import sync_playwright
from playwright.sync_api._generated import Browser, BrowserContext, Page
from pytest import fixture


from tools.report import Report

@fixture(scope="session")
def browser() -> Generator[Browser, Any, None]:
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@fixture
def context(browser: Browser) -> Generator[BrowserContext, Any, None]:
    context: BrowserContext = browser.new_context()
    yield context
    context.close()


@fixture
def page(context: BrowserContext) -> Generator[Page, Any, None]:
    page: Page = context.new_page()
    yield page
    Report(page=page).add_screenshot_to_report(name='Окно после теста')
    page.close()
