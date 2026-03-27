from playwright.sync_api import Page, expect

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

def test_pridat_do_kosiku(page: Page):
    page.goto("https://www.kancelar24.cz/zbozi/kancelarska-zidle-ramiro--cerna/")

    refuse_cookies(page)

    id_add_to_cart_button = "buttonAddToCart"
    id_popup_advanced_order = "popupAdvancedOrder"
    id_button_continue_to_cart = "buttonPopupCart"
    id_cart_product = "cartProductName"

    product_form = page.locator("#product-detail-form")
    add_to_cart_button = product_form.locator(f"[data-testid='{id_add_to_cart_button}']")
    expect(add_to_cart_button).to_be_visible()
    product_name = page.locator("div.p-detail-inner-header > h1").inner_text()
    add_to_cart_button.click()

    popup_advanced_order = page.locator(f"[data-testid='{id_popup_advanced_order}']")
    expect(popup_advanced_order).to_be_visible()

    button_continue_to_cart = page.locator(f"[data-testid='{id_button_continue_to_cart}']")
    expect(button_continue_to_cart).to_be_visible()
    button_continue_to_cart.click()

    cart_product = page.locator(f"[data-testid='{id_cart_product}']")
    expect(cart_product).to_be_visible()
    cart_product_name = cart_product.inner_text()

    assert product_name.strip().lower() == cart_product_name.strip().lower()
