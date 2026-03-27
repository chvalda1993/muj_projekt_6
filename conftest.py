#import pytest
#from playwright.sync_api import Page, expect

#@pytest.fixture
#def refuse_cookies(page):
# id_cookie_bar = "siteCookies__form"
 #id_cookie_settings = "cookiesSettings"
 #id_button_refuse = "buttonCookiesTurnOff"

 #cookie_bar = page.locator(f"div.{id_cookie_bar}")

 #if cookie_bar.is_visible():
    #settings_button = page.locator(f"button[data-testid='{id_cookie_settings}']")
    #settings_button.click()

    #refuse_button = page.locator(f"button[data-testid='{id_button_refuse}']")
    #expect(refuse_button).to_be_visible()
    #refuse_button.click()

 #yield