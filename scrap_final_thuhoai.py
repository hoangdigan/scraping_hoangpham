"""
Note: APP chay ok, cần time.sleep(2), để download hết dữ liệu, mới lấy được page 2
đã test lay page 2 ok
find table(1)

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

from bs4 import BeautifulSoup
import pandas as pd

service = Service(r"chromedriver.exe")
# service = Service('C:\Program Files\Chrome Driver\chromedriver.exe')

def get_driver():
    # Set options to make browsing easier
    # options = webdriver.ChromeOptions()
    # options.add_argument("disable-infobars")
    # options.add_argument("start-maximized")
    # options.add_argument("disable-dev-shm-usage")
    # options.add_argument("no-sandbox")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(r"chromedriver.exe")
    driver.get("http://127.0.0.1:5500/process_data/scraper/1.html")
    return driver


driver = get_driver()
time.sleep(5)

# Click on home link and wait 02 seconds
# element = driver.find_element(by="xpath", value="/html/body/div[2]/div[5]/div/div[1]/div/div/div[1]/div[2]/div[2]/a[8]").click()
# time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# print(soup)
table = soup.find('table')

# table = soup.find_all('table')
df = pd.read_html(str(table))[0]
# print(df)

df.to_excel("df25.xlsx")



