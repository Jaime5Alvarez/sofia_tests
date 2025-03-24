from playwright.sync_api import Playwright, expect
from src.lib.setup import setup_playwright
from src.utils import get_mock_file_path

def test_should_translate_document(playwright: Playwright) -> ...:
    setup = setup_playwright(playwright)

    setup.page.goto("https://sofia.insudpharma.com/sofia_chatbot")

    setup.page.get_by_role("button", name="Translate a document I want").click()
    
    
 
    setup.page.get_by_role("combobox").filter(has_text="Source language").click()
    setup.page.get_by_text("Spanish (ES)").click()
    setup.page.get_by_role("combobox").filter(has_text="Target language").click()
    setup.page.get_by_text("English (EN-GB)").click()


    # Busca el input file cercano o relacionado
    file_input = setup.page.get_by_test_id("translate-box-input")
    file_input.set_input_files(get_mock_file_path())
    
    with setup.page.expect_download():
        setup.page.get_by_role("button", name="Translate").click()

    expect(setup.page.get_by_role("main")).to_contain_text("Document \"Valores_del_Real_Madrid_2024.pdf\" has been successfully translated from ES to EN-GB")

