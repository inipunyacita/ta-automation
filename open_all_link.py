import asyncio
from asyncio.windows_events import NULL
from ntpath import join
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link_otherpage
from lxml import etree
# from test_page_title import cek_page_title
from time import perf_counter
import json

# url = 'dev.littlegiantz.com'
# usercredent = 'littlegiantz'
# passcredent = 'littlegiantz2021'
# urlprefix = 'https://'


def open_all_link(urlprefix, usercredent, passcredent, url):

    # all_link_otherpage(protocol, credent, url)
    list_a = all_link_otherpage(urlprefix, usercredent, passcredent, url)
    list_a_length = len(list_a)
    msg = ''
    status_meta = ''
    status_title = ''
    list_meta = []
    list_title = []
    starttime = perf_counter()
    for i in range(list_a_length):
        try:
            page = requests.get(
                str(list_a[i]), auth=(usercredent, passcredent))
            soup = bs(page.text, "lxml")
            dom = etree.HTML(str(soup))
            title = dom.xpath('//title/text()')
            meta_desc = dom.xpath(
                '//meta[@property="og:description"]/@content')
            meta_title = dom.xpath('//meta[@property="og:title"]/@content')
            meta_desc_content_lorem = dom.xpath(
                '//meta[contains(@property,"og:description") and starts-with(@content, "Lorem") or starts-with(@content, "lorem")]')
        except:
            msg = 'Tidak ditemukan'
            # break
        if (len(meta_title) == 1 and len(meta_desc) == 1):
            if (meta_desc_content_lorem):
                msg = ', '.join(title) + ' | ' + \
                    str(list_a[i]) + ' | Terdapat lorem'
                # break
            else:
                msg = ', '.join(title) + ' | ' + str(list_a[i]) + ' | Ada'
        else:
            msg = ', '.join(title) + ' | ' + str(list_a[i]) + ' | Tidak sesuai'
        data_title_and_desc = ', '.join(
            meta_title) + " | "+', '.join(meta_desc)
        list_meta.append(str(msg))
        list_title.append(str(data_title_and_desc))
        # break
        # # print(meta_title)
        """Script berikut untuk cek halaman apa saja yang tersedia namun tidak dapat dideploy karena akan
        berpotensi menimbulkan timeout karena scraping link yang tidak memiliki batasan dan tergantugn web 
        # if (meta_desc and meta_title):
        #     msg = 'Meta desc untuk halaman' + str(meta_title) + 'tersedia'
        # elif (meta_desc):
        #     msg = 'Meta title tidak ditemukan untuk halaman : ' + str(title)
        # elif (meta_title):
        #     msg = 'Meta desc halaman ' + str(title) + ' tidak ditemukan'
        # else:
        #     msg = 'Meta title dan desc tidak ditemukan di halaman ' + \
        #         str(title)
        # list.append(msg)"""
    # check sesuai/tidak
    if ('tidak sesuai' in str(list_meta).lower()):
        status_meta = 'Tidak Ada'
        if ('lorem' in str(list_meta).lower()):
            status_title = 'Terdapat Lorem dan Tidak Sesuai'
        else:
            status_title = 'Terdapat Tidak Sesuai'
    else:
        status_meta = 'Ada'
        status_title = 'Sesuai'
    # print(f'end time = {perf_counter() - starttime}')
    # print(f'{list_a[0]}')
    return list_meta, list_title, status_meta, status_title


async def send_async_meta(urlprefix, usercredent, passcredent, url):
    return await asyncio.to_thread(open_all_link, urlprefix, usercredent, passcredent, url)
    # for a in list_a:
    #     page = requests.get(a, auth=(username, password))
    #     soup = bs(page.text, 'lxml')
    #     dom = etree.HTML(str(soup))
    #     title = dom.xpath('//meta[@name="description"]/@content')
    #     if (title):
    #         msg = 'ditemukan'
    #     else:
    #         msg = 'tidak ditemukan'
    #     print(f'halaman {a} meta desc = {msg} content = {title}')


# meta, title, status_meta, status_title = open_all_link(
#     urlprefix, usercredent, passcredent, url)
# print(meta)
# print(title)
# print(status_meta)
# print(status_title)
# from csv import list_dialects
# import http
# import requests
# from bs4 import BeautifulSoup as bs
# from time import perf_counter
# import re


# def all_link_otherpage(urlprefix, usercredent, passcredent, url):
#     # inizialitation
#     list_a = []
#     link = urlprefix + usercredent + ':' + passcredent + '@' + url
#     # start scraping
#     try:
#         page_content = requests.get(link)
#         soup = bs(page_content.text, 'lxml')
#         nav = soup.nav
#         a = nav.find_all('a')
#         print(a)
#     except:
#         print('scraping failed / not found')
#     # for a in nav.find_all('a', href=re.compile(urlprefix + url)):
#     #     list_a.append(a['href'])
#     #     list_a_exception = [
#     #         urlprefix + url,
#     #         urlprefix + url + '/',
#     #         urlprefix + url + '/home',
#     #         urlprefix + url + '/beranda'
#     #     ]
#     #     for i in range(0, len(list_a_exception)):
#     #         if list_a_exception[i] in list_a:
#     #             list_a.remove(list_a_exception[i])
#     return list_a


# a = 'dev.nitrajaya.co.id'
# b = 'https://'
# c = 'timedoor'
# d = 'NeverGiveUp2022'
# list_a = all_link_otherpage(b, c, d, a)
# print(list_a)
# print(len(list_a))
