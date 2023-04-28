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

import urllib.request 


# service = Service("D:\\ImportDataFinance-UDEMY\\process_data\\scraper\\chromedriver.exe")

# # Set options to make browsing easier
# options = webdriver.ChromeOptions()
# options.add_argument("disable-infobars")
# options.add_argument("start-maximized")
# options.add_argument("disable-dev-shm-usage")
# options.add_argument("no-sandbox")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_argument("disable-blink-features=AutomationControlled")

# driver = webdriver.Chrome(service=service,options=options)

driver = webdriver.Chrome(r"chromedriver.exe")
driver.get("https://finance.vietstock.vn")
time.sleep(15)

main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle

driver.find_element(by="xpath", value="/html/body/div[2]/div[11]/div[2]/div/div/div/div/div[4]/button").click()
time.sleep(5)

main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle

# gmail: 

driver.find_element(by="xpath", value="/html/body/div[2]/div[8]/div/div/div/form/div[1]/div[2]/div[4]/a").click()
time.sleep(40)

# ["AAS","AAT","AAV","ABB","ABC","ABI","ABR","ABS","ABT"] chuẩn

# stock_list = ["A32","ACE"]
stock_list = ["A32","ACE","ACS","AG1","AGE","AGX","AMP","ANT","APL","APT","ASA","ATB","AVF","B82","BAF","BAL","BBH","BBM","BBT","BCA","BCB","BCP","BCV","BEL","BHG","BHK","BHP","BHT","BIG","BIO","BKH","BLN","BLT","BMD","BMF","BMG","BMJ","BMN","BNA","BNW","BQB","BRS","BSA","BSD","BSP","BT1","BTD","BTG","BTN","BTU","BVL","BVN","BWA","C12","C21","C22","CAR","CBS","CCP","CCV","CDH","CDR","CE1","CEG","CEN","CFM","CGV","CI5","CIP","CK8","CKA","CMI","CMK","CMM","CMN","CMT","CMW","CNA","CNC","CNN","CPA","CPH","CT3","CTN","CVP","CH5","CHC","CHS","DAS","DC1","DCG","DCR","DCS","DCH","DDH","DDM","DFC","DFF","DHN","DKC"]

for s in stock_list:
    
    # CDKT
    try:
        driver.get(f"https://finance.vietstock.vn/{s}/tai-chinh.htm?tab=CDKT")
        time.sleep(2)

        dropdwn = driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[2]")


        dd = Select(dropdwn)
        dd.select_by_value("NAM")

        time.sleep(1)

        dropdwn2 = driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[3]")

        dd2 = Select(dropdwn2)
        dd2.select_by_value("1000000")

        driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/button").click()
        time.sleep(2)

        driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/a[2]").click()
        time.sleep(2)
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


        driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/button").click()
        time.sleep(3)

        driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/a[2]").click()
        time.sleep(3)
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


        driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/button").click()
        time.sleep(3)

        driver.find_element(by="xpath", value="/html/body/div[1]/div[12]/div/div[5]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/a[2]").click()
        time.sleep(3)
    except:
        continue








