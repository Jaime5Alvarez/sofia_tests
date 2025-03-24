from playwright.sync_api import Browser, BrowserContext, Page, Playwright
from src.constants import Constants
from src.lib.auth import get_auth_file, is_logged_in, make_logged_in

class Setup:
    def __init__(self, browser: Browser, context: BrowserContext, page: Page):
        self.browser = browser
        self.context = context
        self.page = page

def setup_playwright(playwright: Playwright) -> Setup:
    browser = playwright.chromium.launch(headless= False)
    if is_logged_in():
        context = browser.new_context(storage_state=get_auth_file())
        page = context.new_page()
        return Setup(browser, context, page)
    context, page = make_logged_in(browser)
    return Setup(browser, context, page)


