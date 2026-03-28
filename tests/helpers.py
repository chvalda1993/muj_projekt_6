from playwright.sync_api import Page, expect

def refuse_cookies(page: Page):
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


def add_product_to_cart_and_open_cart(page: Page, product_url: str):
    id_add_to_cart_button = "buttonAddToCart"
    id_popup_advanced_order = "popupAdvancedOrder"
    id_button_continue_to_cart = "buttonPopupCart"

    page.goto(product_url)
    refuse_cookies(page)

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