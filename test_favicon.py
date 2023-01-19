import asyncio
from bs4 import BeautifulSoup as bs
import requests
from lxml import etree
import time

# url = 'dev.merthanaya.co.id/'
# usercredent = ''
# passcredent = ''
# urlprefix = 'https://'


def favicon_check(urlprefix, url, usercredent, passcredent):
    msg = ''
    status = ''
    link = urlprefix + url
    
    try:
        page = requests.get(link, auth=(usercredent, passcredent))
        soup = bs(page.text, 'lxml')
        dom = etree.HTML(str(soup))
        favicon = dom.xpath(
            "//link[contains(@rel,'icon')]")
        # check if locator correct, it will be found
        if (favicon):
            msg = 'Ada'
        else:
            msg = 'Tidak sesuai'
    except:
        msg = 'Tidak ditemukan'
    return msg


# print(favicon_check(urlprefix, url, usercredent, passcredent))

async def send_async_favicon(urlprefix, url, usercredent, passcredent):
    return favicon_check(urlprefix, url, usercredent, passcredent)
