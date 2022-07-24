import asyncio
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link
from lxml import etree
from time import perf_counter


def cek_title(urlprefix, usercredent, passcredent, url):
    data_a, pesan = all_link(urlprefix, usercredent, passcredent, url)
    list_a_length = len(data_a)
    msg = ''
    status_title = ''
    list_title = []
    for i in range(list_a_length):
        try:
            page = requests.get(
                str(data_a[i]), auth=(usercredent, passcredent))
            soup = bs(page.text, "lxml")
            dom = etree.HTML(str(soup))
            title = dom.xpath('//title/text()')
            msg = ', '.join(title) + " | " + str(data_a[i])
        except:
            msg = str(data_a[i]) + ' | Tidak ditemukan'
        list_title.append(str(msg))
    if ('tidak ditemukan' in str(list_title).lower()):
        status_title = 'Locator tidak ditemukan'
    else:
        if ('tidak ditemukan' in pesan.lower()):
            status_title = 'Error'
        else:
            status_title = 'Ada'
    return list_title, status_title


async def send_async_title(urlprefix, usercredent, passcredent, url):
    return await asyncio.to_thread(cek_title, urlprefix, usercredent, passcredent, url)
