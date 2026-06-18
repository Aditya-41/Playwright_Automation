'''
Browser _ Navigations
'''


from playwright.sync_api import Page,expect
import time

def test_example(page:Page):
    page.goto("https://lebyy.com/")
    page.locator("//a[text()='Services']").click()
    time.sleep(5)
    page.go_back()
    time.sleep(5)
    page.go_forward()
    time.sleep(5)
    page.reload()
    time.sleep(5)
    
    
    
    
    