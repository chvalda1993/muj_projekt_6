from playwright.sync_api import Page, expect
import pytest

def refuse_cookies(page):
    id_cookie_bar = "siteCookies__form"
    id_cookie_settings = "cookiesSettings"
    id_button_refuse = "buttonCookiesTurnOff"

    cookie_bar = page.locator(f"div.{id_cookie_bar}")

    if cookie_bar.is_visible():
        settings_button = page.locator(f"button[data-testid='{id_cookie_settings}']")
        settings_button.click()

        refuse_button = page.locator(f"button[data-testid='{id_button_refuse}']")
        expect(refuse_button).to_be_visible()
        refuse_button.click()

def add_product_to_cart_and_open_cart(page: Page):
    page.goto("https://www.kancelar24.cz/zbozi/kancelarska-zidle-ramiro--cerna/")

    refuse_cookies(page)
    
    id_add_to_cart_button = "buttonAddToCart"
    id_popup_advanced_order = "popupAdvancedOrder"
    id_button_continue_to_cart = "buttonPopupCart"

    product_form = page.locator("#product-detail-form")
    add_to_cart_button = product_form.locator(f"[data-testid='{id_add_to_cart_button}']")
    expect(add_to_cart_button).to_be_visible()
    product_name = page.locator("div.p-detail-inner-header > h1").inner_text().strip()
    add_to_cart_button.click()

    popup_advanced_order = page.locator(f"[data-testid='{id_popup_advanced_order}']")
    expect(popup_advanced_order).to_be_visible()

    button_continue_to_cart = page.locator(f"[data-testid='{id_button_continue_to_cart}']")
    expect(button_continue_to_cart).to_be_visible()
    button_continue_to_cart.click()

    return product_name


def test_odebrat_z_kosiku(page: Page):
    id_cart_product = "cartProductName"
    id_delete_button_cart = "buttonDeleteItem"
    id_empty_cart_title = "cartTitle"

    product_name = add_product_to_cart_and_open_cart(page)

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