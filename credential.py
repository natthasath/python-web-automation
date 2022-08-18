from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import requests
import certifi
import time

print(certifi.where())

browser = webdriver.Edge(EdgeChromiumDriverManager().install())
url = 'https://reg.nida.ac.th/registrar/login.asp'

def login():
    browser.get(url)
    browser.find_element_by_id('f_uid').send_keys('')
    browser.find_element_by_id ('f_pwd').send_keys('')
    browser.find_element_by_id('login_submit').click()
    time.sleep(30)

    browser.close()

login()