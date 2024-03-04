from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import requests
import certifi
import time

print(certifi.where())

browser = webdriver.Edge(EdgeChromiumDriverManager().install())
url = 'https://reg.nida.ac.th/registrar/login.asp'

def login():
    browser.get(url)
    browser.find_element(By.ID, 'f_uid').send_keys('')
    browser.find_element(By.ID, 'f_pwd').send_keys('')
    browser.find_element(By.ID, 'login_submit').click()
    time.sleep(30)

    browser.close()

login()