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

stock_list = ["A32","ACE","ACS","AG1","AGE","AGX","AMP","ANT","APL","APT","ASA","ATB","AVF","B82","BAF","BAL","BBH","BBM","BBT","BCA","BCB","BCP","BCV","BEL","BHG","BHK","BHP","BHT","BIG","BIO","BKH","BLN","BLT","BMD","BMF","BMG","BMJ","BMN","BNA","BNW","BQB","BRS","BSA","BSD","BSP","BT1","BTD","BTG","BTN","BTU","BVL","BVN","BWA","C12","C21","C22","CAR","CBS","CCP","CCV","CDH","CDR","CE1","CEG","CEN","CFM","CGV","CI5","CIP","CK8","CKA","CMI","CMK","CMM","CMN","CMT","CMW","CNA","CNC","CNN","CPA","CPH","CT3","CTN","CVP","CH5","CHC","CHS","DAS","DC1","DCG","DCR","DCS","DCH","DDH","DDM","DFC","DFF","DHN","DKC"]

# stock_list =["ITA"]
for s in stock_list:    
    # CDKT
    try: 
        driver.get(f"https://finance.vietstock.vn/{s}/tai-chinh.htm?tab=CDKT")
        time.sleep(5)

        dropdwn = None
        while(dropdwn == None):

            dropdwn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[2]"))
            )
       
        dd = Select(dropdwn)
        dd.select_by_value("NAM")

        time.sleep(3)

        dropdwn2 = driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[3]")

        dd2 = Select(dropdwn2)
        dd2.select_by_value("1000000")

        time.sleep(3)
        driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[4]/div/div/table[2]/tbody/tr[6]/td[1]/div/a[1]").click()
        time.sleep(2)
        driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[4]/div/div/table[2]/tbody/tr[6]/td[1]/div/a[1]").click()
        time.sleep(2)
        driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[4]/div/div/table[2]/tbody/tr[6]/td[1]/div/a[1]").click()
        time.sleep(2)
        driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[4]/div/div/table[2]/tbody/tr[6]/td[1]/div/a[1]").click()
       
        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        table = soup.find_all('table', id= "tbl-data-CDKT")
        df = pd.read_html(str(table))[0]
        filename = folder_export + s + "_BCDKT.xlsx"
        df.to_excel(filename)
       
    except:
        continue

    # KQKD
    try:
        driver.get(f"https://finance.vietstock.vn/{s}/tai-chinh.htm?tab=KQKD")
        dropdwn = driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[2]")
        
        dd = Select(dropdwn)
        dd.select_by_value("NAM")

        time.sleep(2)

        dropdwn2 = driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[3]")
        time.sleep(2)
        dd2 = Select(dropdwn2)
        dd2.select_by_value("1000000")

        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        table = soup.find_all('table', id= "tbl-data-KQKD")
        df2 = pd.read_html(str(table))[0]
        filename =  folder_export + s + "_KQKD.xlsx"
        df2.to_excel(filename)        

    except:
        continue

    # LCTT
    try:
        driver.get(f"https://finance.vietstock.vn/{s}/tai-chinh.htm?tab=LC")
        time.sleep(3)
        dropdwn = driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[2]")
        dd = Select(dropdwn)
        dd.select_by_value("NAM")

        time.sleep(3)

        dropdwn2 = driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[3]")
        time.sleep(2)
        dd2 = Select(dropdwn2)
        dd2.select_by_value("1000000")
        time.sleep(3)
        page1 = driver.page_source
        soup1 = BeautifulSoup(page1, "html.parser")
        table1 = soup1.find_all('table', id= "tbl-data-LCTT-indirect")
        # #tbl-data-LCTT-indirect
        df3 = pd.read_html(str(table1))[0]
        filename =  folder_export + s + "LCTTGT.xlsx"
        df3.to_excel(filename)
        # print(df3)
        
    except:
        continue
