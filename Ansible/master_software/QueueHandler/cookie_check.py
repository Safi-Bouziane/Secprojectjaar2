#! /usr/bin/env python3
from selenium import webdriver

url = "https://www.vrt.be/vrtnws/nl/"
splitedurl = url.split("/")
urlDomainwww = splitedurl[2]
urlDomain = urlDomainwww[3::]

driver = webdriver.Chrome()
driver.get(url)
cookies = driver.get_cookies()

# cookie = (cookies[1])
# cookieDomain = cookie.get("domain")
# print(cookieDomain)
firstpartyAmount = 0
thirdpartyAmount = 0
for cookie in cookies:
    cookieDomain = cookie.get("domain")
    if cookieDomain == urlDomain:
        firstpartyAmount += 1
    else:
        thirdpartyAmount +=1

print("the website uses " +str(firstpartyAmount) + " first party and " +str(thirdpartyAmount) + " third party cookies")


#/***************************************************************
#*
#* Copyright (Wouter Weemaes, Safi Bouziane, Kamil Grielens, Robbe Willeme) - All rights reserved. 
#*
#* Unauthorized use, copy, modify, merge, publish, distribute, sublicense, 
#* and/or sell any parts of the software/source code is strictly prohibited.
#* Proprietary and confidential
#* License: No license. 
#* Written by: (Wouter Weemaes) (wouterweemaes@outlook.com), (06/2022)
#*
#****************************************************************/
