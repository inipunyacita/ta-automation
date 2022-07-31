import asyncio
from gettext import find
from re import S
from tabnanny import check
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link_otherpage
from lxml import etree
from time import perf_counter

# url = 'solar-studio.timedoor-host.my.id'
# usercredent = 'solarstudio'
# passcredent = 'solarstudio2021'
# urlprefix = 'https://'

# url = 'dev.littlegiantz.com'
# usercredent = 'littlegiantz'
# passcredent = 'littlegiantz2021'
# urlprefix = 'https://'


def cek_bc(urlprefix, usercredent, passcredent, url):

    # all_link_otherpage(protocol, credent, url)
    list_a, pesan = all_link_otherpage(
        urlprefix, usercredent, passcredent, url)
    list_a_length = len(list_a)
    msg = ''
    msg_status = ''
    status_bc = []
    data = []
    starttime = perf_counter()
    for i in range(list_a_length):
        try:
            page = requests.get(
                str(list_a[i]), auth=(usercredent, passcredent))
            soup = bs(page.text, "lxml")
            ol = soup.ol
            data = ol.find_all('li')
            # print(list_a[i] + str(data))
            if (len(data) < 2):
                msg = str(list_a[i]) + ' | Tidak sesuai | ' + str(data)
            else:
                msg = str(list_a[i]) + ' | ' + str(data)
            # print(list_a[i])
            # print(data)
        except:
            msg = str(list_a[i]) + ' | Tidak ditemukan | ' + str(data)
        status_bc.append(msg)
        # check sesuai/tidak
        if ('tidak sesuai' in str(status_bc).lower()):
            msg_status = 'Terdapat tidak sesuai'
        elif ('tidak ditemukan' in str(status_bc).lower()):
            msg_status = 'Terdapat tidak ditemukan'
        else:
            msg_status = 'Ada'
    if ('tidak ditemukan' in pesan.lower()):
        msg_status = 'Error'
    return msg_status, status_bc


async def send_async_bc(urlprefix, usercredent, passcredent, url):
    return await asyncio.to_thread(cek_bc, urlprefix, usercredent, passcredent, url)

# status, data_bc, lista = cek_bc(urlprefix, usercredent, passcredent, url)
# print(status)
# print(lista)
# print(len(data_bc))
