from playwright.sync_api import Page, expect
from helpers import add_product_to_cart_and_open_cart

PRODUCT_URL = "https://www.kancelar24.cz/zbozi/kancelarska-zidle-ramiro--cerna/"


def test_pridat_do_kosiku(page: Page, clean_cart):
    id_cart_product = "cartProductName"

    product_name = add_product_to_cart_and_open_cart(page, PRODUCT_URL)

    cart_product = page.locator(f"[data-testid='{id_cart_product}']")
    expect(cart_product).to_be_visible()

    cart_product_name = cart_product.inner_text().strip()
    assert product_name.lower() == cart_product_name.lower()