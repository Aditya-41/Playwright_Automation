from playwright.sync_api import Page, expect


def _click_with_wait(page: Page, locator, timeout: int = 10000) -> None:
    expect(locator).to_be_visible(timeout=timeout)
    locator.click()
    page.wait_for_timeout(300)


def _fill_with_wait(page: Page, locator, value: str, timeout: int = 10000) -> None:
    expect(locator).to_be_visible(timeout=timeout)
    locator.click()
    locator.fill(value)
    page.wait_for_timeout(300)


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/", wait_until="networkidle")

    username = page.locator('[data-test="username"]')
    password = page.locator('[data-test="password"]')
    login_button = page.locator('[data-test="login-button"]')
    backpack = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
    bike_light = page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')
    menu_button = page.get_by_role("button", name="Open Menu")
    inventory_link = page.locator('[data-test="inventory-sidebar-link"]')
    logout_link = page.locator('[data-test="logout-sidebar-link"]')

    _fill_with_wait(page, username, "standard_user")
    _fill_with_wait(page, password, "secret_sauce")
    _click_with_wait(page, login_button)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html", timeout=10000)

    _click_with_wait(page, backpack)
    _click_with_wait(page, bike_light)
    _click_with_wait(page, menu_button)
    _click_with_wait(page, inventory_link)
    _click_with_wait(page, logout_link)
