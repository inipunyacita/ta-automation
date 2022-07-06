from csv import list_dialects
import http
import requests
from bs4 import BeautifulSoup as bs
from lxml import etree
from time import perf_counter
import re


def all_link_otherpage(urlprefix, usercredent, passcredent, url):
    # inizialitation
    msg = ''
    list_a = []
    link = urlprefix + url
    page_content = requests.get(link, auth=(usercredent, passcredent))
    soup = bs(page_content.text, 'html.parser')
    nav = soup.header
    a = nav.find_all('a', href=re.compile(urlprefix + url))
    for a in nav.find_all('a', href=re.compile(urlprefix + url)):
        list_a.append(a['href'])
    list_a_exception = [
        urlprefix + url,
        urlprefix + url + '/',
        urlprefix + url + '/id',
        urlprefix + url + '/en',
        urlprefix + url + '/home',
        urlprefix + url + '/beranda'
    ]
    for i in range(0, len(list_a_exception)):
        if list_a_exception[i] in list_a:
            list_a.remove(list_a_exception[i])
    return list_a


# a = 'dev.littlegiantz.com/'
# b = 'https://'
# c = 'littlegiantz'
# d = 'littlegiantz2021'
# list_a = all_link_otherpage(b, c, d, a)
# print(list_a[2])
# print(len(list_a))
