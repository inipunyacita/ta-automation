from cgitb import text
import re
import requests
from bs4 import BeautifulSoup as bs


url = 'http://apindo:9VIiV!QqvPQ8UJ!1lN@dev.apindotrainingcenter.com/'
page = requests.get(url)
soup = bs(page.text, 'lxml')
a = soup.find_all(href=re.compile("https://timedoor.net"))
aTxt = soup.find_all(string=re.compile("PT. Timedoor Indonesia"))
# check
if (len(a) == 1 and len(aTxt) == 1):
    print("footer link sesuai")
else:
    print("footer link tidak sesuai")
