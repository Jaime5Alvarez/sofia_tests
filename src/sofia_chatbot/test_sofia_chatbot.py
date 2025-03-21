from playwright.sync_api import Page, Playwright, expect
import re
from src.lib.auth import get_auth_file, is_logged_in, make_logged_in
def test_sofia_chatbot(playwright: Playwright, page: Page) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    
    # Verificar si ya existe un archivo de estado de autenticación
    if not is_logged_in():
        make_logged_in(page, context)

    # Cargar el estado de autenticación existente
    context = browser.new_context(storage_state=get_auth_file())
    page = context.new_page()
    page.goto("https://sofia.insudpharma.com/")
    
    # Continuar con la prueba después del inicio de sesión
    page.get_by_role("button", name="Go").first.click()
    page.get_by_role("textbox", name="Send a message...").click()
    page.get_by_role("textbox", name="Send a message...").fill("hello world")
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).first.click()
    expect(page.get_by_role("main")).to_contain_text("hello world")

    # ---------------------
    context.close()
    browser.close()

