from playwright.sync_api import Page, expect
import pytest
from helpers import refuse_cookies

@pytest.fixture
def clean_cart(page: Page):
    id_delete_button_cart = "buttonDeleteItem"

    page.goto("https://www.kancelar24.cz/kosik/")
    refuse_cookies(page)

    delete_buttons = page.locator(f"[data-testid='{id_delete_button_cart}']")

    while delete_buttons.count() > 0:
        count_before = delete_buttons.count()
        delete_buttons.first.click()
        expect(delete_buttons).to_have_count(count_before - 1)
