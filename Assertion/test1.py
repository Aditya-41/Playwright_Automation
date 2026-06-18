'''
Verification on browser using assertion
playwright uses expect library for assertion
i> General assertion --> will not wait for any element)
ii>locator assertion --> will wait for 5 sec for the element to be available in the DOM

Playwright has hard and soft assertion
1> Hard assertion --> if the assertion fails, the test will be failed and the execution will be stopped
2> Soft assertion --> if the assertion fails, the test will be failed but the execution will be continued

'''
from unicodedata import name

from playwright.sync_api import Page,expect
import time


def test1(page:Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    
    # expect(page).to_have_title("Swag Labs")
    # expect(page).to_have_url("https://www.saucedemo.com/")
    page.get_by_role("textbox",name="username").fill("student")
    page.get_by_role("textbox",name="password").fill("Password123")
    page.get_by_text("Submit").first.click()
    
    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    expect(page.locator("//h1[text()='Logged In Successfully']")).to_have_text("Logged In Successfully")
    # page.locator("//*[@id='loop-container']/div/article/div[2]/div/div/div/a").click()

    # page.get_by_role("button",id="submit").click()
    
    # expect(page.locator('#username')).to_be_visible()
    # expect(page.locator("//input[@name='username']")).to_contain_text("student")
    # expect(page.locator("//input[@name='username']")).to_be_editable()
    # expect(page.locator("//input[@id='password']")).to_be_visible()
    # expect(page.locator("//input[@id='password']")).to_contain_text("Password123")
    # expect(page.locator("//button[text()='Submit']")).to_be_enabled()
    

