from playwright.sync_api import Page, Playwright, expect
import re
from src.lib.setup import setup_playwright
from src.constants import Constants

def test_should_render_sofia_chatbot(playwright: Playwright, page: Page) -> ...:
    setup = setup_playwright(playwright, page)

    page = setup.context.new_page()
    page.goto("https://sofia.insudpharma.com/sofia_chatbot")
    expect(page).to_have_title(re.compile("Sofia Chatbot"))


