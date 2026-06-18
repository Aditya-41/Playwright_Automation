import playwright.sync_api as pw
from playwright.sync_api import Page,expect
import time


def test_example(page:Page):
    # page.goto("https://www.udemy.com/")
    # time.sleep(2)
    # page.get_by_text("Log in").click()
    # time.sleep(2)
    
    # page.get_by_title
    
    # page.goto("https://www.bing.com/?cc=in")
    # time.sleep(2)
    # page.get_by_alt_text("© The Economic Times").first.click()
    # time.sleep(5)  
    
    page.goto("https://www.udemy.com/")
    time.sleep(2)
    page.get_by_test_id("browse-nav-item").first.click()
    time.sleep(5)
      