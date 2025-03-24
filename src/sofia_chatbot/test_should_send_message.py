from playwright.sync_api import Playwright, expect
import re
from src.lib.setup import setup_playwright

def test_should_send_message(playwright: Playwright) -> ...:
    setup = setup_playwright(playwright)

    setup.page.goto("https://sofia.insudpharma.com/sofia_chatbot")
    
    setup.page.get_by_role("textbox", name="Send a message...").click()
    setup.page.get_by_role("textbox", name="Send a message...").fill("hello world")
    setup.page.get_by_role("button").filter(has_text=re.compile(r"^$")).first.click()
    expect(setup.page.get_by_role("main")).to_contain_text("hello world")