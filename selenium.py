
import os
import re
from selenium.webdriver.support.select import Select 
from selenium import webdriver

driver = webdriver.Chrome(r"D:\chromedriver.exe")

url='http://www.tageo.com/index-e-ch-cities-CN.htm'

data=[]

driver.get(url)
data.append(driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/table/tbody/tr[3]/td/font/font/table").text)

list_city.append(re.split('\n',data)[1:])
    
with open('your_file.txt', 'w') as f:
    for i in list_city:
        f.write("%s\n" % i)
        
