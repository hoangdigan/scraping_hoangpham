"""
Note: APP chay ok, cần time.sleep(2), để download hết dữ liệu, mới lấy được page 2
đã test lay page 2 ok
find table(1)
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

folder_export = 'D:/ImportDataFinance-UDEMY/process_data/scraper/vietstock/'

driver=webdriver.Chrome(executable_path=r'D:\ImportDataFinance-UDEMY\process_data\scraper\chromedriver.exe')

# driver = webdriver.Chrome(r"chromedriver.exe")
driver.maximize_window()
driver.get("https://finance.vietstock.vn")
time.sleep(20)

driver.find_element(by="xpath", value="/html/body/div[2]/div[11]/div[2]/div/div/div/div/div[4]/button").click()
time.sleep(5)

# yahoomail: 

driver.find_element(by="xpath", value="/html/body/div[2]/div[8]/div/div/div/form/div[1]/div[1]/div[1]/input").send_keys("hoangdigan@yahoo.com")
time.sleep(3)

driver.find_element(by="xpath", value="/html/body/div[2]/div[8]/div/div/div/form/div[1]/div[1]/div[3]/input").send_keys("Net$zcbm97531")
time.sleep(3)

driver.find_element(by="xpath", value="/html/body/div[2]/div[8]/div/div/div/form/div[1]/div[2]/div[1]/button").click()
time.sleep(20)

# stock_list =["AAS","AAT","AAV","ABB","ABC","ABI","ABR","ABS","ABT"] # OK

stock_list = ['BPC', 'NVL','PDR','PGC','PMC','PSH','PSI','PSI','PTB','SAM','SCR','SDN','SGP','SHB','SHI','SHS','SJG','SSB','SSC','SSG','SSH','STB','VCI','VDS']

for s in stock_list:       
  
    try:
        driver.get(f"https://finance.vietstock.vn/{s}/ho-so-doanh-nghiep.htm")
        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
      
        table = soup.find_all('table')
             
        df = pd.read_html(str(table))[7]   
       

        list_row = ['Company', s]
        df.loc[len(df)] = list_row 

        print("df", df)
        filename = s + ".xlsx"
        df.to_excel(filename)

    except:
        continue
