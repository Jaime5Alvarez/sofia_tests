from playwright.sync_api import Playwright
from src.constants import Constants
from src.lib.setup import setup_playwright
from src.lib.sofia_chatbot.write_chat_message import write_chat_message

def test_should_send_message(playwright: Playwright) -> ...:
    setup = setup_playwright(playwright)

    setup.page.goto(f"{Constants().DOMAIN}/sofia_chatbot")
    
    write_chat_message(setup.page, "Hello, how are you?")

    assert True