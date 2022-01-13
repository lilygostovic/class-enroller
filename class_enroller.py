#!/usr/bin/env python

# imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EXP_COND

# setup chrome driver
driver=webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("https://horizon.mcgill.ca/pban1/twbkwbis.P_WWWLogin")



# vars from user
un=''
pw=''
crn=''

def login():
    WebDriverWait(driver, 20).until(EXP_COND.presence_of_element_located((By.ID, 'mcg_un')))
    WebDriverWait(driver, 20).until(EXP_COND.presence_of_element_located((By.ID, 'mcg_pw')))
    driver.find_element_by_id('mcg_un').send_keys(un)
    driver.find_element_by_id('mcg_pw').send_keys(pw)
    driver.find_element_by_id('mcg_un_submit').click()
  
login()

driver.quit()
