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


def cek_alt_img(urlprefix, usercredent, passcredent, url):

    # all_link_otherpage(protocol, credent, url)
    list_a, pesan = all_link(urlprefix, usercredent, passcredent, url)
    list_a_length = len(list_a)
    msg = ''
    status_img = []
    starttime = perf_counter()
    for i in range(list_a_length):
        try:
            page = requests.get(
                str(list_a[i]), auth=(usercredent, passcredent))
            soup = bs(page.text, "lxml")
            dom = etree.HTML(str(soup))
            img_with_alt = dom.xpath('//img[contains(@alt," ")]')
            all_img = dom.xpath('//img')
            if (len(img_with_alt) != len(all_img)):
                msg = list_a[i] + ' | terdapat Tidak sesuai'
        except:
            msg = str(list_a[i]) + ' | Tidak ditemukan'
        status_img.append(msg)
    # check sesuai/tidak
    if ('tidak sesuai' in str(status_img).lower()):
        msg_status = 'Tidak sesuai'
    elif ('tidak ditemukan' in str(status_img).lower()):
        msg_status = 'Tidak ditemukan'
    else:
        msg_status = 'Sesuai'
    return msg_status, status_img


async def send_async_altimg(urlprefix, usercredent, passcredent, url):
    return await asyncio.to_thread(cek_alt_img, urlprefix, usercredent, passcredent, url)


# status, data_img = cek_alt_img(urlprefix, usercredent, passcredent, url)
# print(status)
# print(data_img)
