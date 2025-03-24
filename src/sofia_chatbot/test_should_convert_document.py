from playwright.sync_api import Playwright
from src.lib.setup import setup_playwright
from src.utils import get_mock_file_path

def test(playwright: Playwright) -> ...:
    setup = setup_playwright(playwright)

    setup.page.goto("https://sofia.insudpharma.com/sofia_chatbot")

    setup.page.get_by_role("button", name="I want to convert a document").click()
    setup.page.get_by_role("combobox").filter(has_text="Input Format").click()
    setup.page.get_by_text("PDF", exact=True).click()
    setup.page.get_by_role("combobox").filter(has_text="Output Format").click()
    setup.page.get_by_text("DOCX", exact=True).click()

    file_input = setup.page.get_by_test_id("file-converter-input")
    file_input.set_input_files(get_mock_file_path())
    
    with setup.page.expect_response(lambda response: response.status == 200 and "docs-converter/process/download" in response.url) as response_info:
        setup.page.get_by_role("button", name="Convert").click()
    response = response_info.value
    assert response.status == 200 