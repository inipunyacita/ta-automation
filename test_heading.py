import asyncio
from tabnanny import check
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link
from lxml import etree
from time import perf_counter

# url = 'dev.apindotrainingcenter.com'
# usercredent = 'apindo'
# passcredent = '9VIiV!QqvPQ8UJ!1lN'
# urlprefix = 'https://'

# url = 'citananta.my.id/cakarentcar'
# usercredent = ''
# passcredent = ''
# urlprefix = 'https://'


def cek_heading(urlprefix, usercredent, passcredent, url):

    # all_link_otherpage(protocol, credent, url)
    list_a, pesan = all_link(urlprefix, usercredent, passcredent, url)
    list_a_length = len(list_a)
    msg = ''
    msg_status = ''
    status_heading = []
    list_heading = []
    starttime = perf_counter()
    for i in range(list_a_length):
        try:
            page = requests.get(
                str(list_a[i]), auth=(usercredent, passcredent))
            soup = bs(page.text, "lxml")
            list_heading = soup.find_all(["h1", "h2", "h3"])
            h1 = soup.find_all("h1")
            h2 = soup.find_all("h2")
            if (len(h1) == 1):
                if (len(h2) < 1):
                    msg = str(list_a[i]) + \
                        ' | Tidak sesuai | h2 berjumlah bukan kurang dari 1'
                else:
                    msg = str(list_a[i]) + str(list_heading)
            else:
                msg = str(list_a[i]) + ' | Tidak sesuai | h1 berjumlah bukan 1'
        except:
            msg = str(list_a[i]) + ' | Tidak ditemukan'
        status_heading.append(msg)
        # check sesuai/tidak
    if ('tidak sesuai' in str(status_heading).lower()):
        msg_status = 'Terdapat tidak sesuai'
    elif ('tidak ditemukan' in str(status_heading).lower()):
        msg_status = 'Terdapat tidak ditemukan'
    else:
        if ('tidak ditemukan' in pesan.lower()):
            msg_status = 'Error'
        else:
            msg_status = 'Ada'
    return msg_status, status_heading


async def send_async_heading(urlprefix, usercredent, passcredent, url):
    return await asyncio.to_thread(cek_heading, urlprefix, usercredent, passcredent, url)

# data = cek_heading(urlprefix, usercredent, passcredent, url)
# print(data)
