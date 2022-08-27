import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest
from selenium.webdriver.support.ui import Select

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    #try:
        browser.get(link)
        button = len(browser.find_elements(By.CLASS_NAME, "btn btn-lg btn-primary"))
        assert button > 0, '!!!НЕ НАШЕЛ!!!'