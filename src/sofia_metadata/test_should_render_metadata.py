from playwright.sync_api import Playwright, expect
from src.lib.setup import setup_playwright

def test_should_render_metadata(playwright: Playwright) -> ...:
    setup = setup_playwright(playwright)

    setup.page.goto("https://sofia.insudpharma.com/apps/metadata")
    expect(setup.page.get_by_text("Add your metadata")).to_be_visible()
