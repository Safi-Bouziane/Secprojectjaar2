#! /usr/bin/env python3
from selenium import webdriver

url = "https://www.vrt.be/vrtnws/nl/"

driver = webdriver.Chrome()
driver.get(url)

cookies = driver.get_cookies()
print(cookies)
