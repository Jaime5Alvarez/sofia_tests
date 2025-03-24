from playwright.sync_api import Playwright, expect
from src.constants import Constants
from src.lib.setup import setup_playwright
from src.lib.sofia_chatbot.delete_custom_bot import delete_custom_bot
from src.lib.sofia_chatbot.write_chat_message import write_chat_message
from src.lib.sofia_chatbot.add_custom_bot_to_sidebar import add_custom_bot_to_sidebar
from src.lib.sofia_chatbot.create_custom_bot import create_custom_bot

def test_should_send_message(playwright: Playwright) -> ...:
    setup = setup_playwright(playwright)

    mock_custom_bot = create_custom_bot(setup.page)
    add_custom_bot_to_sidebar(setup.page, mock_custom_bot)

    setup.page.goto(f"{Constants().DOMAIN}/sofia_chatbot")

    # Esperar a que el sidebar esté cargado
    setup.page.wait_for_selector('div[data-sidebar="content"]')
    
    # Esperar específicamente a que el bot aparezca en el sidebar
    # Esto esperará hasta que el elemento sea visible, lo que ocurrirá después de que el fetch se complete
    setup.page.wait_for_selector(f'div[data-sidebar="content"] a span:has-text("{mock_custom_bot.name}")', 
                                state='visible', 
                                timeout=10000)  # Aumentar el timeout a 10 segundos o más si es necesario
    
    # Buscar el enlace del bot por su nombre
    bot_link = setup.page.locator(f'div[data-sidebar="content"] a span:has-text("{mock_custom_bot.name}")').first
    
    # Verificar que el bot existe en el sidebar
    assert bot_link.is_visible(), f"El bot '{mock_custom_bot.name}' no está visible en el sidebar"
    
    # Navegar hacia arriba para encontrar el elemento 'a' (enlace) que contiene el span
    bot_anchor = bot_link.locator("xpath=./ancestor::a")
    
    # Hacer clic en el enlace
    bot_anchor.click()
    
    # Esperar a que la página termine de cargar después del clic
    # Puedes esperar por un elemento que sabes que aparecerá cuando la página esté completamente cargada
    
    # También puedes esperar por un elemento específico que confirme que la página del chat está cargada
    # También buscar el nombre en el contenido principal de la página
    # Este selector busca el nombre del bot en el título principal
    heading = setup.page.get_by_role("heading", name=mock_custom_bot.name)
    expect(heading).to_be_visible()

    
    write_chat_message(setup.page, "Hello, how are you?")
    assert True

    delete_custom_bot(setup.page, mock_custom_bot.name)
