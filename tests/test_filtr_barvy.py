from playwright.sync_api import Page, expect
from helpers import refuse_cookies
import re

def test_filtr_barvy(page: Page):
    page.goto("https://www.kancelar24.cz/kategorie/kancelarske-zidle-a-kresla/")

    refuse_cookies(page)

    filtr_cerna = page.locator(".advanced-parameter[title='černá']")
    expect(filtr_cerna).to_be_visible()
    filtr_cerna.click()

    expect(page).to_have_url(re.compile(r"pv18=84"))
    
    listing = page.locator("[data-testid='productCards']")
    expect(listing).to_be_visible()

    product_names = listing.locator("[data-testid='productCardName']:visible")
    expect(product_names.first).to_be_visible()

    product_count = product_names.count()
    assert product_count > 0


    for i in range(product_count):
        text = product_names.nth(i).inner_text().strip()
        print(f"{i}: {text}")
        assert "černá" in text.lower(), f"Produkt neodpovídá filtru černá: {text}"
