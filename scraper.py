import requests
from bs4 import BeautifulSoup
import csv

csv = "journals.csv"

url = "https://sju.primo.exlibrisgroup.com/discovery/search?query=any,contains,Advances%20in%20Quantitative%20Analysis%20of%20Finance%20and%20Accounting&tab=Everything&search_scope=MyInst_and_CI&vid=01USCIPH_INST:SJU&offset=0"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

#print(soup)

print(page.text)

