'''
.get_by_label() Method is used to locate elements based on their associated label text.
This is particularly useful for form inputs where the label provides a clear description of the input field. 
By using .get_by_label(), you can easily interact with form elements without relying on less stable selectors like IDs or classes.
'''
from playwright.sync_api import Page,expect
import time


def test_example(page:Page):
    page.goto("https://www.salesforce.com/form/developer-signup/?=pb")
    page.get_by_label("First name").fill("Aditya")
    time.sleep(2)
    page.get_by_label("Last name").fill("Patil")
    page.get_by_label("Job title").fill("Software Engineer")
    page.get_by_label("Company").fill("netApp")
    page.get_by_label("Work email").fill("aditya.patil@netapp.com")
    
    time.sleep(5)
    
    
    
    
    
    
    

    
    

    