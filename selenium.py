
import os
import re
from selenium.webdriver.support.select import Select 
from selenium import webdriver

#download Chrome Extension in order to provide control of Chrome to python.
#link for downloading it is - http://chromedriver.chromium.org/downloads
driver = webdriver.Chrome(r"D:\chromedriver.exe")

#provide a webite for Web Scrapping any data from it automatically
url='http://www.tageo.com/index-e-ch-cities-CN.htm'

data=[]

driver.get(url)

#simplest method to get data is by using xpath of that element you want to extract
data.append(driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/table/tbody/tr[3]/td/font/font/table").text)

#basic Regular Expression to get data in an particular manner
list_city.append(re.split('\n',data)[1:])
   
#at last we can save the data in an excel,csv or text file
with open('your_file.txt', 'w') as f:
    for i in list_city:
        f.write("%s\n" % i)
        
