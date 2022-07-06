import asyncio
import requests
from selenium.common.exceptions import WebDriverException
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
        title = dom.xpath('//title[contains(.,"Page Not Found")]')
        # check if locator correct, it will be found
        if (title):
            status = 'script sukses'
    except WebDriverException:
        status = 'scraping failed / not found'
    if (status == 'script sukses'):
        msg = 'Tersedia'
    else:
        msg = 'Tidak Ada'

    return msg


async def send_async_404(urlprefix, usercredent, passcredent, url):
    return await asyncio.to_thread(page_404_checker, urlprefix, usercredent, passcredent, url)
