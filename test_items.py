import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_availability_of_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"))  
    assert button > 0, "Button is not found!"