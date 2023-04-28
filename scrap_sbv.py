from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Edge(r"msedgedriver.exe")

s= "https://sbv.gov.vn/webcenter/portal/vi/menu/rm/ls/lsttlnh?centerWidth=80%25&leftWidth=20%25&rightWidth=0%25&showFooter=false&showHeader=false&_adf.ctrl-state=4qmpcn4ax_141&_afrLoop=18561333523976023"
driver.get(s)

fr ="/html/body/div[1]/div/form/div/div[3]/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr/td[2]/div/div/div[3]/div/div/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div[2]/span/input"
driver.find_element(by="xpath", value= fr).send_keys("01/01/2022")

to = "/html/body/div[1]/div/form/div[1]/div[3]/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr/td[2]/div/div/div[3]/div/div/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div/div[2]/span/input"
driver.find_element(by="xpath", value= to).send_keys("27/04/2023")

searchBtn = "/html/body/div[1]/div/form/div[1]/div[3]/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr/td[2]/div/div/div[3]/div/div/div/div/div[1]/div[2]/div/div[3]/div/div[3]/div/div/a"
driver.find_element(by="xpath", value= searchBtn).click()
time.sleep(5)

nextPage = "/html/body/div[1]/div/form/div[1]/div[3]/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr/td[2]/div/div/div[3]/div/div/div/div/div[1]/div[3]/div/div[1]/div/div[4]/table/tbody/tr/td/table/tbody/tr/td[9]/a"
driver.find_element(by="xpath", value= nextPage).click()
time.sleep(5)

for i in range (1,13):
    click_btn = driver.find_elements(by= By.LINK_TEXT, value ='Tải file excel')
    for btn in click_btn:
        btn.click()
        time.sleep(2)
    nextPage = "/html/body/div[1]/div/form/div[1]/div[3]/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr/td[2]/div/div/div[3]/div/div/div/div/div[1]/div[3]/div/div[1]/div/div[4]/table/tbody/tr/td/table/tbody/tr/td[9]/a"
    driver.find_element(by="xpath", value= nextPage).click()
    time.sleep(5)