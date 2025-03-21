from playwright.sync_api import Browser, BrowserContext, Page, Playwright
from src.constants import Constants
from src.lib.auth import make_logged_in

class Setup:
    def __init__(self, browser: Browser, context: BrowserContext):
        self.browser = browser
        self.context = context

def setup_playwright(playwright: Playwright, page: Page) -> Setup:
    browser = playwright.chromium.launch(headless= Constants().HEADLESS_MODE)
    context = make_logged_in(page, browser)

    return Setup(browser, context)

