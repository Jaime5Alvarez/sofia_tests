from playwright.sync_api import Page
import uuid
from src.constants import Constants
from src.lib.sofia_chatbot.mock_custom_bot import MockCustomBot
from src.utils import get_mock_file_path


def create_custom_bot(page: Page) -> MockCustomBot:

    mock_data = MockCustomBot(name=f"Test-{uuid.uuid4()}", description="My custom bot test description", instruction="My custom bot test instruction")

    page.goto(f"{Constants().DOMAIN}/sofia_chatbot")

    page.locator("body").click()
    page.get_by_role("button", name="Toggle Sidebar").click()
    page.get_by_role("list").filter(has_text="SOF.IAMore").get_by_role("button").click()
    page.get_by_role("menuitem", name="Create Agent New").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill(mock_data.name)
    page.get_by_role("textbox", name="Description").click()
    page.get_by_role("textbox", name="Description").fill(mock_data.description)
    page.get_by_role("textbox", name="Give instructions to your").click()
    page.get_by_role("textbox", name="Give instructions to your").fill(mock_data.instruction)

      
    file_input = page.locator("#file-upload")
    file_input.set_input_files(get_mock_file_path())

    with page.expect_response(lambda response: response.status == 200 and f"{Constants().DOMAIN}/sofia_chatbot/api/custom-bot" == response.url) as response_info:
        page.get_by_role("button", name="Save agent").click()
    
    response = response_info.value
    assert response.status == 200

    return mock_data