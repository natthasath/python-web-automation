from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import requests
import certifi
import time

print(certifi.where())

browser = webdriver.Edge(EdgeChromiumDriverManager().install())

with open('./website/checklist.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        browser.get(line)
        title = browser.title
        time.sleep(5)
        # r = requests.get(url=line, verify=False)

        try:
            r = requests.get(line)
            print(r.status_code)
        except requests.exceptions.SSLError as err:
            print('SSL Error. Adding custom certs to Certifi store...')
            cafile = certifi.where()
            with open('D:\Work\Certificate\\2020\\nida.ac.th.pem', 'rb') as infile:
                customca = infile.read()
            with open(cafile, 'ab') as outfile:
                outfile.write(customca)
            print('That might have worked.')
        # print(browser.get_log('browser'))