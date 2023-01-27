from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import requests
import certifi
import time

print(certifi.where())

browser = webdriver.Edge(EdgeChromiumDriverManager().install())
url = 'https://forms.office.com/Pages/ResponsePage.aspx?id=a-9d29iPPkqR3I2yUBpoIi-asz3_DWtMnJZIAkg7TPhURE9OQU5SVUswMEZNVkZJWFdCNFRCMFpJQiQlQCN0PWcu'

browser.get(url)
browser.find_element_by_xpath('.//input[@type="radio" and @value="นาย"]').click()
browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div/input').send_keys('ณัฐเศรษฐ์')
browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/div/input').send_keys('ศักดิ์ศุภนรา')
browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[5]/div/div[2]/div/div/input').send_keys('นักวิชาการคอม')
browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[6]/div/div[2]/div/div/input').send_keys('สำนักเทคโนโลยีสารสนเทศ')
browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[7]/div/div[2]/div/div/input').send_keys('1')
browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[8]/div/div[2]/div/div/div/input[1]').send_keys('4/2/2021')
browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[9]/div/div[2]/div/div/div/input[1]').send_keys('4/3/2021')
browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[10]/div/div[2]/div/div/input').send_keys('027273262')
browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[11]/div/div[2]/div/div/input').send_keys('ทดสอบ')
browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button/div').click()
browser.find_element_by_xpath('.//input[@type="radio" and @value="รับทราบ"]').click()
browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button[2]/div').click()
time.sleep(30)
