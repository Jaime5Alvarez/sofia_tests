from playwright.sync_api import Playwright, expect
import re
from src.lib.setup import setup_playwright
import os

def test_should_run_metadata(playwright: Playwright) -> ...:
    setup = setup_playwright(playwright)

    setup.page.goto("https://sofia.insudpharma.com/apps/metadata")
    setup.page.get_by_role("textbox", name="Field name to extract").click()
    setup.page.get_by_role("textbox", name="Field name to extract").fill("name")
    setup.page.get_by_role("textbox", name="Field description to extract").click()
    setup.page.get_by_role("textbox", name="Field description to extract").fill("name of the document")
    setup.page.get_by_role("button", name="New field").click()
    setup.page.locator("div").filter(has_text=re.compile(r"^TextMultiple values$")).get_by_placeholder("Field name to extract").click()
    setup.page.locator("div").filter(has_text=re.compile(r"^TextMultiple values$")).get_by_placeholder("Field name to extract").fill("number of words")
    setup.page.locator("div").filter(has_text=re.compile(r"^TextMultiple values$")).get_by_placeholder("Field description to extract").click()
    setup.page.locator("div").filter(has_text=re.compile(r"^TextMultiple values$")).get_by_placeholder("Field description to extract").fill("number of words")
    setup.page.locator("div").filter(has_text=re.compile(r"^number of wordsTextMultiple values$")).get_by_role("combobox").click()
    setup.page.get_by_text("Integer number").click()
    setup.page.get_by_role("button", name="New field").click()
    setup.page.locator("div").filter(has_text=re.compile(r"^TextMultiple values$")).get_by_placeholder("Field name to extract").click()
    setup.page.locator("div").filter(has_text=re.compile(r"^TextMultiple values$")).get_by_placeholder("Field name to extract").fill("abstract")
    setup.page.locator("div").filter(has_text=re.compile(r"^TextMultiple values$")).get_by_placeholder("Field description to extract").click()
    setup.page.locator("div").filter(has_text=re.compile(r"^TextMultiple values$")).get_by_placeholder("Field description to extract").fill("abstract of this document")

    file_path = os.path.join(os.path.dirname(__file__), "../test_files/Valores_del_Real_Madrid_2024.pdf")

    file_input = setup.page.get_by_test_id("file-metadata-input")
    file_input.set_input_files(file_path)

    with setup.page.expect_response(lambda response: response.status == 200 and "bg-metadata/proxy" in response.url) as response_info:
        setup.page.get_by_role("button", name="Run all docs").click()
    
    response = response_info.value
    assert response.status == 200

    expect(setup.page.get_by_text("Metadata extracted")).to_be_visible()

