from playwright.sync_api import Page, expect
from helpers import add_product_to_cart_and_open_cart

PRODUCT_URL = "https://www.kancelar24.cz/zbozi/kancelarska-zidle-ramiro--cerna/"


def test_odebrat_z_kosiku(page: Page, clean_cart):
    id_cart_product = "cartProductName"
    id_delete_button_cart = "buttonDeleteItem"
    id_empty_cart_title = "cartTitle"

    product_name = add_product_to_cart_and_open_cart(page, PRODUCT_URL)

    cart_products = page.locator(f"[data-testid='{id_cart_product}']")
    expect(cart_products).to_be_visible()
    expect(cart_products).to_contain_text(product_name)

    cart_product_name = cart_products.inner_text().strip()
    assert product_name.lower() == cart_product_name.lower()

    cart_product_count = cart_products.count()
    assert cart_product_count == 1, f"V košíku má být 1 produkt, ale je jich tam {cart_product_count}."

    delete_button_cart = page.locator(f"[data-testid='{id_delete_button_cart}']")
    expect(delete_button_cart).to_be_visible()
    delete_button_cart.click()

    expect(cart_products).to_have_count(0)

    empty_cart_title = page.locator(f"[data-testid='{id_empty_cart_title}']")
    expect(empty_cart_title).to_be_visible()
    expect(empty_cart_title).to_have_text("Váš košík je prázdný")