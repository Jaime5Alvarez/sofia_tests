from playwright.sync_api import Playwright, expect
import re
from src.constants import Constants
from src.lib.setup import setup_playwright

def test_should_render_sofia_chatbot(playwright: Playwright) -> ...:
    setup = setup_playwright(playwright)

    setup.page.goto(f"{Constants().DOMAIN}/sofia_chatbot")
    expect(setup.page).to_have_title(re.compile("Sofia Chatbot"))

