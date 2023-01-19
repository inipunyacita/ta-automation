import asyncio
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link
from lxml import etree
from time import perf_counter

# url = 'timedooracademy.com/'
# usercredent = ''
# passcredent = ''
# urlprefix = 'https://'

def cek_title(urlprefix, usercredent, passcredent, url):
    data_a, pesan = all_link(urlprefix, usercredent, passcredent, url)
    list_a_length = len(data_a)
    msg = ''
    status_title = ''
    title = []
    filtered = []
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
        if (len(title) == 0):
            msg = str(data_a[i]) + ' | Tidak ada'
        list_title.append(str(msg))
        def filter_list(variable):
            letters = [
                str(data_a[i]) + ' | Tidak ditemukan',
                str(data_a[i]) + ' | Tidak ada'
            ]
            if (variable in letters):
                return True
            else:
                return False
        
        # using filter function
        exception = filter(filter_list, list_title)
        
        for i in exception:
            filtered.append(i)
    if ('tidak ditemukan' in str(list_title).lower()):
        status_title = 'Locator tidak ditemukan'
        return filtered, status_title
    elif ('tidak ada' in str(list_title).lower()):
        status_title = 'Terdapat tidak ada'
        return filtered, status_title
    else:
        if ('tidak ditemukan' in pesan.lower()):
            status_title = 'Error'
            return filtered, status_title
        elif ('tidak cocok' in pesan.lower()):
            status_title = 'Error ketika get all link'
            return filtered, status_title
        else:
            status_title = 'Ada'
            return list_title, status_title

async def send_async_title(urlprefix, usercredent, passcredent, url):
    return cek_title(urlprefix, usercredent, passcredent, url)

# a, b = cek_title(urlprefix, usercredent, passcredent, url)
# print(a)