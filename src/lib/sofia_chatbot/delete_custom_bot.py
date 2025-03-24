from src.constants import Constants

def delete_custom_bot(page, bot_name):
    page.goto(f"{Constants().DOMAIN}/sofia_chatbot")

    # Esperar a que el sidebar esté cargado
    page.wait_for_selector('div[data-sidebar="content"]')
    
    # Construir el selector para el botón de menú del bot específico
    menu_button_selector = f'div[data-sidebar="content"] li:has(a span:has-text("{bot_name}")) button[data-sidebar="menu-action"]'
    
    # Esperar a que el botón de menú esté disponible
    page.wait_for_selector(menu_button_selector, state='visible', timeout=10000)
    
    # Obtener el botón de menú
    menu_button = page.locator(menu_button_selector)
    
    # Verificar que el botón existe
    assert menu_button.is_visible(), f"El botón de menú para el bot '{bot_name}' no está visible"
    
    # Hacer clic en el botón de menú
    menu_button.click()
    
    # Esperar a que el menú se abra
    page.wait_for_selector('button[data-sidebar="menu-action"][data-state="open"]')

    page.get_by_role("menuitem", name="Edit Agent").click()

    page.get_by_role("button", name="Delete agent").click()

    with page.expect_response(lambda response: response.status == 200 and 
                                              response.request.method == "DELETE" and 
                                              f"{Constants().DOMAIN}/sofia_chatbot/api/custom-bot" in response.url) as response_info:
        page.get_by_role("button", name="Delete").click()

    # Verificar que la respuesta fue exitosa y usó el método DELETE
    assert response_info.value.status == 200, "La respuesta no tuvo estado 200"
    assert response_info.value.request.method == "DELETE", "La solicitud no usó el método DELETE"