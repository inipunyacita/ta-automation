import asyncio
import requests
import re
from bs4 import BeautifulSoup as bs
from get_all_link import all_link_otherpage
# check homepage

# url = 'global-transparency.timedoor-host.web.id/id'
# usercredent = ''
# passcredent = ''
# urlprefix = 'https://'


def footer_homepage_check(urlprefix, usercredent, passcredent, url):

    # inizialitation
    msg = ''
    link = urlprefix + url
    try:
        page = requests.get(link, auth=(usercredent, passcredent))
        soup = bs(page.text, 'html.parser')
        footer = soup.footer
        a = footer.find_all(href=re.compile("https://timedoor.net"))
        a_with_slice = footer.find_all(
            href=re.compile("https://timedoor.net/"))
        aTxt = footer.find_all(string=re.compile("PT. Timedoor Indonesia"))
        # check
        if ((len(a) == 1 or len(a_with_slice) == 1) and len(aTxt) == 1):
            msg = "Sesuai"
        else:
            msg = "Tidak sesuai"
    except:
        msg = 'Tidak ada'
    return msg

# check other page


def footer_otherpage_check(urlprefix, usercredent, passcredent, url):
    msg = ''
    list_link = []
    list_link, pesan = all_link_otherpage(
        urlprefix, usercredent, passcredent, url)
    if (pesan == 'Locator tidak ditemukan'):
        msg = 'Scraping link gagal'
    try:
        link = list_link[0]
        page = requests.get(link, auth=(usercredent, passcredent))
        soup = bs(page.text, 'html.parser')
        footer = soup.footer
        a = footer.find_all(href=re.compile("https://timedoor.net"))
        a_with_slice = footer.find_all(href=re.compile("https://timedoor.net/"))
        aTxt = footer.find_all(string=re.compile(
            "PT. Timedoor Indonesia"))
        # check
        if ((len(a) == 0 and len(a_with_slice) == 0) and len(aTxt) == 1):
            msg = "Sesuai"
        else:
            msg = "Tidak sesuai"
    except:
        msg = 'Tidak ada'

    return msg

# hasil = footer_otherpage_check(urlprefix, usercredent, passcredent, url)
# print(hasil)


async def send_async_footer(urlprefix, usercredent, passcredent, url):
    return footer_homepage_check(urlprefix, usercredent, passcredent, url)


async def send_async_other_footer(urlprefix, usercredent, passcredent, url):
    return footer_otherpage_check(urlprefix, usercredent, passcredent, url)


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
