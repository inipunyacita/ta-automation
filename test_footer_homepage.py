import asyncio
import requests
import re
from bs4 import BeautifulSoup as bs
from get_all_link import all_link_otherpage
import soupsieve
# check homepage


def footer_homepage_check(urlprefix, usercredent, passcredent, url):

    # inizialitation
    msg = ''
    link = urlprefix + url
    page = requests.get(link, auth=(usercredent, passcredent))
    soup = bs(page.text, 'lxml')
    try:
        a = soup.find_all(href=re.compile("https://timedoor.net"))
        aTxt = soup.find_all(string=re.compile("PT. Timedoor Indonesia"))
        # check
        if (len(a) >= 1 and len(aTxt) >= 1):
            msg = "Sesuai"
        else:
            msg = "Tidak sesuai"
    except:
        print('scraping failed / not found')
    return msg


async def send_async_footer(urlprefix, usercredent, passcredent, url):
    return await asyncio.to_thread(footer_homepage_check, urlprefix, usercredent, passcredent, url)

# check other page


def footer_otherpage_check(urlprefix, usercredent, passcredent, url):
    msg2 = ''
    list_link = []
    list_link = all_link_otherpage(urlprefix, usercredent, passcredent, url)
    link = list_link[2]
    page = requests.get(link, auth=(usercredent, passcredent))
    soup = bs(page.text, 'lxml')
    a = soup.find_all(href=re.compile("https://timedoor.net"))
    aTxt = soup.find_all(string=re.compile("PT. Timedoor Indonesia"))
    # check
    if (len(a) == 0 and len(aTxt) == 1):
        msg2 = "Sesuai"
    else:
        msg2 = "Tidak sesuai"
    return msg2


async def send_async_other_footer(urlprefix, usercredent, passcredent, url):
    return await asyncio.to_thread(footer_otherpage_check, urlprefix, usercredent, passcredent, url)


# cek otherpage - belum jadi
"""
1. Proses nya scrap semua page html 
2. Cari yang a / nav
3. Masukin ke list/array
4. Ambil yang pertama (harus navigasi menu / halaman lain namun tetap pada website)
5. Tambah ke link
6. Akses lalu cek footer homepagenya dengan script yang udah ada di fungsi footer otherpage cek
"""
# def footer_otherpage_cek(urlprefix, urlcredent, url, urldirektori):

#      # inizialitation
#     msg = ''
#     link = urlprefix + urlcredent + url + urldirektori
#     page = requests.get(link)
#     soup = bs(page.text, 'lxml')
#     aTxt = soup.find_all(string=re.compile("PT. Timedoor Indonesia"))
#     # check
#     if (len(aTxt) >= 1):
#         msg = "Sesuai"
#     else:
#         msg = "Tidak sesuai"
#     return msg
