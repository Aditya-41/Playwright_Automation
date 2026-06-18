'''
for any automation testing --> we need to identify unique attribute for the desired element n then we will ask our script to goto the page identify an element with this information n perform this action 

'''
# .get_by_role()

import re 
from playwright.sync_api import Page,expect


def test_example(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox",name="Username").fill("locked_out_user")
    page.get_by_role("textbox",name="Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()