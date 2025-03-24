from playwright.sync_api import Page, expect
import re

def write_chat_message(page: Page, message: str):
    page.get_by_role("textbox", name="Send a message...").click()
    page.get_by_role("textbox", name="Send a message...").fill(message)
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).first.click()
    expect(page.get_by_role("main")).to_contain_text(message)