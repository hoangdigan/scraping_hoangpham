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

stock_list = ['TOW','TPS','TQN','TQW','TS3','TSD','TSG','TTA','TTG','TTS','TUG','TV6','TVA','TVG','TVH','TVM','TVP','TW3','THD','THN','THP','THU','THW','TR1','TRS','TRT','UCT','UDL','UEM','UMC','UPC','UPH','USC','USD','VAB','VBG','VBH','VCE','VCT','VDB','VDN','VDT','VE9','VES','VFR','VGL','VGV','VHD','VGV','VHD','VIH','VIM','VIN','VIR','VKP','VIM','VIN','VIR','VKP','VLP','VMA','VMT','VNI','VNX','VNY','VNH','VPA','VPC','VPR','VPW','VSE','VST','VTA','VTD','VTI','VTJ','VTK','VTL','VTM','VTP','VTQ','VTS','VTV','VTX','VTZ','VTH','VTR','VUA','VVS','VW3','VWS','VXP','VXT','WCS','WSS','WTC','X20','X26','X77','XDC','XDH','XHC','XLV','XMC','XMD','XMP','XPH','YBC','YBM','YEG','YTC']# PSN, DKC

for s in stock_list:    
    # CDKT
    try: 
        driver.get(f"https://finance.vietstock.vn/{s}/tai-chinh.htm?tab=CDKT")
        time.sleep(5)

        dropdwn = driver.find_element_by_name("PeriodType")
       
        dd = Select(dropdwn)
        dd.select_by_value("NAM")

        time.sleep(3)

        dropdwn2 = driver.find_element_by_name("UnitDong")
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

        dropdwn = driver.find_element_by_name("PeriodType")       
        dd = Select(dropdwn)
        dd.select_by_value("NAM")

        time.sleep(3)
        dropdwn2 = driver.find_element_by_name("UnitDong")      
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

        dropdwn = driver.find_element_by_name("PeriodType")       
        dd = Select(dropdwn)
        dd.select_by_value("NAM")

        time.sleep(3)
        dropdwn2 = driver.find_element_by_name("UnitDong")
        dd2 = Select(dropdwn2)
        dd2.select_by_value("1000000")
        time.sleep(3)
        
        page1 = driver.page_source
        soup1 = BeautifulSoup(page1, "html.parser")
        try: 
            table1 = soup1.find_all('table', id= "tbl-data-LCTT-indirect")
            filename =  folder_export + s + "_LCTTTT.xlsx"
            # #tbl-data-LCTT-indirect
        except:
            table1 = soup1.find_all('table', id= "tbl-data-LCTT-direct")
            filename =  folder_export + s + "_LCTTGT.xlsx"
        df3 = pd.read_html(str(table1))[0]
        
        df3.to_excel(filename)
        # print(df3)
        
    except:
        continue
