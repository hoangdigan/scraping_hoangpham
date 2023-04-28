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

import urllib.request 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# service = Service("D:\\ImportDataFinance-UDEMY\\process_data\\scraper\\chromedriver.exe")

# Set options to make browsing easier
options = webdriver.ChromeOptions()
# options.add_argument("disable-infobars")
# options.add_argument("start-maximized")
# options.add_argument("disable-dev-shm-usage")
# options.add_argument("no-sandbox")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_argument("disable-blink-features=AutomationControlled")

# driver = webdriver.Chrome(service=service,options=options)
driver = webdriver.Chrome(r"chromedriver.exe")
driver.maximize_window()
driver.get("http://127.0.0.1:5500/process_data/scraper/7.html")

page = driver.page_source

soup = BeautifulSoup(page, "html.parser")


# print(soup.prettify())

table = soup.find_all('table', id= "tbl-data-CDKT")
df = pd.read_html(str(table))[0]
df.to_excel("df2-1.xlsx")

# print(df)