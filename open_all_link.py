# # import asyncio
# # from urllib import response
# # import time
# # from time import perf_counter
# # import requests
# # from bs4 import BeautifulSoup as bs
# # from get_all_link import all_link_otherpage
# # from lxml import etree

# # url = 'dev.apindotrainingcenter.com'
# # credent = 'apindo:9VIiV!QqvPQ8UJ!1lN@'
# # username = 'apindo'
# # password = '9VIiV!QqvPQ8UJ!1lN'
# # protocol = 'https://'
# # # all_link_otherpage(protocol, credent, url)
# # list_a = all_link_otherpage(protocol, credent, url)


# # def open_all_link():
# #     for a in list_a:
# #         page = requests.get(a, auth=(username, password))
# #         soup = bs(page.text, 'lxml')
# #         dom = etree.HTML(str(soup))
# #         title = dom.xpath('//meta[@name="description"]/@content')
# #         if (title):
# #             msg = 'ditemukan'
# #         else:
# #             msg = 'tidak ditemukan'
# #         print(f'halaman {a} meta desc = {msg} content = {title}')


# # open_all_link()

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
