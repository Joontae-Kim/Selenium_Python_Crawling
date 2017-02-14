# encoding line
#-*- coding: utf-8 -*-
# The standard library modules
import os, sys, time

# The wget module
import wget

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# if you want to use chrome, replace Firefox() with Chrome()
# driver = webdriver.Chrome()
chromedriver = "/Users/hivearena/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
url = ' - write specific website url - '
driver.get(url)

# click the a tag or button 
driver.find_element_by_css_selector(' - specific html element or attribute- ').click()
element = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.CLASS_NAME, " - specific html element or attribute- "))
)
# 완성본
li_grp = element.find_elements_by_class_name(' - specific html element or attribute- ')
print(ul_list)

print('End!')
driver.quit()