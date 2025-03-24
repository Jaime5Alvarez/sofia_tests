from playwright.sync_api import Page
from src.constants import Constants
from src.lib.sofia_chatbot.mock_custom_bot import MockCustomBot


def add_custom_bot_to_sidebar(page: Page, mock_custom_bot: MockCustomBot):
    page.goto(f"{Constants().DOMAIN}/sofia_chatbot/custom-bot/store")
    
    # Verificar que el bot está visible en la página antes de intentar añadirlo
    bot_card = page.locator("h3.font-semibold.text-lg", has_text=mock_custom_bot.name).first
    assert bot_card.is_visible(), f"El bot '{mock_custom_bot.name}' no está visible en la página"
    
    # Navegar hacia arriba para encontrar el contenedor del bot y luego buscar el botón dentro de él
    bot_container = bot_card.locator("xpath=./ancestor::div[contains(@class, 'rounded-lg')]")
    add_button = bot_container.locator("button", has_text="Add").first
    
    # Hacer clic en el botón y esperar a que se complete la solicitud
    with page.expect_response(lambda response: response.status == 200 and "api/custom-bot/added" in response.url) as response_info:
        add_button.click()
    
    response = response_info.value
    assert response.status == 200, "La solicitud para añadir el bot no fue exitosa"
    
    return True