import asyncio
from cgitb import html
import string
from lxml import etree
import re
import requests
from bs4 import BeautifulSoup as bs

# url = 'dev.san-ei.co.id/'
# usercredent = ''
# passcredent = ''
# urlprefix = 'http://'

def cek_analitik(urlprefix, url, usercredent, passcredent):
    try:
        site = urlprefix + url
        data = requests.get(str(site), auth=(usercredent, passcredent))
        soup = bs(data.text, "lxml")
        head = soup.head
        dom = etree.HTML(str(head))
        scriptdata_g = dom.xpath('//script[contains(@src, "https://www.googletagmanager.com/gtag/js?id=")]')
        if (scriptdata_g):
            msg = 'Ada'
        else:
            msg = 'Tidak ada'
    except:
        msg = 'Error'
    return msg

async def send_async_analitik(urlprefix, url, usercredent, passcredent):
    return cek_analitik(urlprefix, url, usercredent, passcredent)

# data = cek_analitik(urlprefix, url, usercredent, passcredent)
# print(data)
