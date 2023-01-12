import requests
from bs4 import BeautifulSoup
import pandas as pd


global formattedjournal
formattedjournal = ""

csv = pd.read_csv("journals.csv")

journal_list = []
journal_list = csv['Journal'].tolist()

print(journal_list)
def formatjournal(journal):
    # Change journal format to add %20 in between each space
    formattedjournal = str(journal).replace(" ", "%20")
    return formattedjournal
def query():
    url = "https://sju.primo.exlibrisgroup.com/discovery/search?query=any,contains," + formattedjournal + "&tab=Everything&search_scope=MyInst_and_CI&vid=01USCIPH_INST:SJU&offset=0"
    page = requests.get(url)

for i in range(len(journal_list)):
    formatjournal(journal_list[i])
    query()