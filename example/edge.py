from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = webdriver.Edge(EdgeChromiumDriverManager().install())
browser.get('https://www.google.com/')