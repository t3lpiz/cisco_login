# coding: utf-8
from selenium import webdriver
username = 'definiti username'
password = 'definiti parola'
driver = webdriver.Chrome()
driver.get('http://86.106.213.22:8080/home')
try:
    username = driver.find_element_by_name('username')
    username.send_keys(username)
    password = driver.find_element_by_name('password')
    password.send_keys(password)
    buton_ok = driver.find_element_by_xpath('//input[@type="submit"]')
    buton_ok.click()
except Exception:
    pass
driver.quit()
