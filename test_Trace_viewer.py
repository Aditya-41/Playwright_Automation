'''
Trace Viewer is a tool that allows you to visualize and analyze the execution of your playwright test runs.
It provides a detailed view of the test execution, including the sequence of actions, network requests, and other relevant information.
'''
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"about-sidebar-link\"]").click()
    page.get_by_text("x", exact=True).click()
