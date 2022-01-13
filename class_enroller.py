#!/usr/bin/env python

# imports
from selenium import webdriver
import selenium
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
    WebDriverWait(driver, 10).until(EXP_COND.presence_of_element_located((By.ID, 'mcg_un')))
    WebDriverWait(driver, 10).until(EXP_COND.presence_of_element_located((By.ID, 'mcg_pw')))
    driver.find_element_by_id('mcg_un').send_keys(un)
    driver.find_element_by_id('mcg_pw').send_keys(pw)
    driver.find_element_by_id('mcg_un_submit').click()

def navigate_to_registration():
    # xpaths
    stu_mnu="//div[@class='pagebodydiv']//table//tbody//tr[2]//td[2]//a"
    reg_mnu="//table[@class='menuplaintable']//tbody//tr[2]//td[2]//a"
    quick_add="//table[@class='menuplaintable']//tbody//tr[3]//td[2]//a"
    sel_trm="//div[@class='pagebodydiv']//form//input"

    xpaths=[stu_mnu,reg_mnu,quick_add,sel_trm]

    for xpath in xpaths:
        WebDriverWait(driver, 10).until(EXP_COND.presence_of_element_located((By.XPATH, xpath)))
        driver.find_element_by_xpath(xpath).click()

  
login()
navigate_to_registration()

# driver.quit()
