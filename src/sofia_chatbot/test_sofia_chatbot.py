from playwright.sync_api import Page, Playwright, expect
import re
from src.lib.setup import setup_playwright

def test_should_send_message(playwright: Playwright, page: Page) -> None:
    setup = setup_playwright(playwright, page)

    page = setup.context.new_page()
    page.goto("https://sofia.insudpharma.com/sofia_chatbot")
    
    page.get_by_role("textbox", name="Send a message...").click()
    page.get_by_role("textbox", name="Send a message...").fill("hello world")
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).first.click()
    expect(page.get_by_role("main")).to_contain_text("hello world")

    # ---------------------
    setup.context.close()
    setup.browser.close()
