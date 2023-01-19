import asyncio
import requests
from bs4 import BeautifulSoup as bs
from lxml import etree


def page_404_checker(urlprefix, usercredent, passcredent, url):
    # Inizialisation
    fortifor = '/hwahaiwhaiwjai'
    msg = ''
    status = ''
    link = urlprefix + url + fortifor
    # scraping started
    try:
        page = requests.get(link, auth=(usercredent, passcredent))
        soup = bs(page.text, 'lxml')
        dom = etree.HTML(str(soup))
        title = dom.xpath(
            '//title[contains(.,"Page")]')
        # check if locator correct, it will be found
        if (title):
            msg = 'Sesuai'
        else:
            msg = 'Tidak sesuai'
    except:
        msg = 'Tidak ditemukan'

    return msg


async def send_async_404(urlprefix, usercredent, passcredent, url):
    return page_404_checker(urlprefix, usercredent, passcredent, url)
