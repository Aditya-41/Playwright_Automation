'''
id = "searchBox" , #id --> css for that element is #searchBox
class = "searchBox" , #class --> css for that element is .searchBox
placeholder = "Search for a course" , #placeholder --> css for that element is [placeholder="Search for a course"]
Tag = "input" , #tag --> css for that element is input 
'''


import time

import playwright.sync_api as pw
from playwright.sync_api import Page,expect

def test_example(page:Page):
    
    page.goto("https://saucedemo.com/")
    
    # All Element by [[ Id ]]
    # page.locator("#user-name").fill("standard_user")
    # page.locator("#password").fill("secret_sauce")
    # page.locator("#login-button").click()
    
    # All Element by [[ Class ]]
    # page.locator(".input_error.form_input").first.fill("standard_user")
    # page.locator(".input_error.form_input").nth(1).fill("secret_sauce")
    # page.locator(".submit-button.btn_action").click()
    
    # All Element by [[ Placeholder ]]
    # page.locator("[placeholder='Username']").fill("standard_user")
    # page.locator("[placeholder='Password']").fill("secret_sauce")
    # page.locator("[data-test='login-button']").click()
    
    # All Element by [[ Tag ]]
    page.locator("input[placeholder='Username']").first.fill("standard_user")
    page.locator("input[placeholder='Password']").fill("secret_sauce")
    page.locator("input[data-test='login-button']").click()


    
    time.sleep(5)