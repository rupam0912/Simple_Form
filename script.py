from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get('https://rupam0912.github.io')

#browser.find_element_by_xpath("//input[@id ='submit_id']").click()

#a = browser.find_element_by_xpath("//input[@id ='naam_werkgever_ld']") 
#a.send_keys("")

import pandas as pd
df = pd.read_csv("data.csv")
r,c= df.shape;

for i in range(r) :
    a = browser.find_element_by_xpath("//input[@id ='naam_werkgever_ld']")
    b = browser.find_element_by_xpath("//input[@id ='plaats_werkgever_ld']")
    c = browser.find_element_by_xpath("//input[@id ='functie_ld']")
    d = browser.find_element_by_xpath("//input[@id ='startdate_job']")
    e = browser.find_element_by_xpath("//input[@id ='enddate_ld_job']")
    a.send_keys(df.iloc[i,0])
    b.send_keys(df.iloc[i,1])
    c.send_keys(df.iloc[i,2])
    d.send_keys(df.iloc[i,3])
    e.send_keys(str(df.iloc[i,4]))
    browser.find_element_by_xpath("//input[@id ='submit_id']").click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)
