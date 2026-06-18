'''
xpath locator

1> Absolute XPATH --> right from html starting till the desired element
2> Relative XPATH --> //tagname[@attribute='value'] (or) //tagname[@attribute1='value' and @attribute2='value']
3> Relative XPATH --> //tagname[contains(@attribute,'value')]
4> Relative XPATH --> //tagname[text()='value'] --> Exact text match
5> Relative XPATH --> //tagname[contains(text(),'value')] --> Partial text match
6> Relative XPATH --> //tagname[starts-with(@attribute,'value')]  --> Index based XPATH --> (//tagname[@attribute='value'])[index]
'''
from playwright.sync_api import Page,expect
import time

def test_example(page:Page):
    page.goto("https://www.saucedemo.com/")
    
    # Absolute XPATH
    # page.locator("xpath=/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").fill("standard_user")
    # page.locator("xpath=/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input").fill("secret_sauce")
    # page.locator("xpath=/html/body/div/div/div[2]/div[1]/div/div/form/input").click()
    
    # Relative XPATH --> //tagname[@attribute='value']
    # page.locator("xpath=//input[@placeholder='Username' and @id='user-name']").fill("standard_user")
    # page.locator("xpath=//input[@data-test='password' and @name='password']").fill("secret_sauce")
    # page.locator("xpath=//input[@name='login-button' and @id='login-button']").click()
    
    # Relative XPATH --> //tagname[contains(@attribute,'value')]
    page.locator("xpath=//input[contains(@placeholder,'Username')]").fill("standard_user")
    page.locator("xpath=//input[contains(@data-test,'password')]").fill("secret_sauce")
    page.locator("xpath=//input[contains(@name,'login-button')]").highlight()
    page.locator("xpath=//input[contains(@name,'login-button')]").click()
    # page.locator("//div[contains(text(),'Sauce')]").first.click()
    
    page.locator(".inventory_item").filter(has_text="Sauce Labs Bike Light").get_by_role("button",name="Add to cart").click()    
    
    time.sleep(5)
    
    
    
    # page.locator("//*[@id='nav-logo-sprites']").click()

    time.sleep(5)