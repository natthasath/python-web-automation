from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = webdriver.Edge(EdgeChromiumDriverManager().install())
# browser.get('https://www.xn--42caj4e6bk1f5b1j.com/')

# txt_email = browser.find_element_by_id('email')
# txt_email.send_keys(username)

# txt_email = browser.find_element_by_id('pass')
# txt_email.send_keys(password)

# btn_login = browser.find_element_by_id('loginbutton')
# btn_login.click()

# btn_check = browser.find_element_by_id('btn-check-rights')
# btn_check.click()

# btn_register = browser.find_element_by_id('dropdownMenuLink')
# btn_register.click()

# btn_people = browser.find_element_by_id('btn-register-people')
# btn_people.click()

browser.get('https://register.xn--42caj4e6bk1f5b1j.com/')

checkbox = browser.find_element_by_id('check_terms')
checkbox.Selected