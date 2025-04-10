import os

from playwright.sync_api import Browser, BrowserContext, Page

from src.constants import Constants

def is_logged_in() -> bool:
    auth_file = get_auth_file()
    if os.path.exists(auth_file):
        return True
    else:
        return False

def get_auth_file() -> str:
    auth_file = "auth_state.json"
    return auth_file

def make_logged_in(browser: Browser) -> tuple[BrowserContext, Page]:
    context = browser.new_context()
    page = context.new_page()

     # Realizar el proceso de inicio de sesión y guardar el estado
    page.goto(f"{Constants().DOMAIN}/login")
    page.get_by_role("link", name="Login").click()
    page.get_by_role("textbox", name="Enter your email, phone, or").fill(Constants().SOFIA_USER_EMAIL)
    page.get_by_role("button", name="Next").click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(Constants().SOFIA_USER_PASSWORD)
    page.get_by_role("textbox", name="Password").press("Enter")
    page.get_by_role("button", name="Yes").click()
        
    # Guardar el estado de autenticación para futuras pruebas
    context.storage_state(path=get_auth_file())

    return context, page