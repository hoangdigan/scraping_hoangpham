"""
semi-auto: copy element from website => index.html => local host => lay data

"""


import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "http://127.0.0.1:5500/process_data/scraper/2.html"

page = requests.get(URL, verify=False)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.find(id="tbReleaseResult")

table = soup.find_all('table')
df = pd.read_html(str(table))[0]
df.to_excel("df2-1.xlsx")

print(df)
