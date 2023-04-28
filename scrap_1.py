from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service("D:\\ImportDataFinance-UDEMY\\process_data\\scraper\\chromedriver.exe")

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver =    (service=service,options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output

def write_file(text):
  """Write input text into a text file"""
  filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
  with open(filename, 'w') as file:
    file.write(text)


def main():
    driver = get_driver()
    
    # Find and fill in username & password
    element = driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    element = driver.find_element(by="id", value="id_password").send_keys("automatedautomated"+ Keys.RETURN)
    time.sleep(2)

    # Click on home link and wait 02 seconds
    element = driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)

    # Scrap the temperature value
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)
   
    

print(main())