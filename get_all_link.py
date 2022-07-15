from csv import list_dialects
import http
import requests
from bs4 import BeautifulSoup as bs
from lxml import etree
from time import perf_counter
import re

# url = 'dev.littlegiantz.com'
# usercredent = 'littlegiantz'
# passcredent = 'littlegiantz2021'
# urlprefix = 'https://'


def all_link_otherpage(urlprefix, usercredent, passcredent, url):
    # inizialitation
    msg = ''
    list_a = []
    link = urlprefix + url
    try:
        page_content = requests.get(link, auth=(usercredent, passcredent))
        soup = bs(page_content.text, 'html.parser')
        body = soup.header
        a_body = body.find_all('a', href=re.compile(urlprefix + url))
    except:
        print('Locator tidak ditemukan')
    for a in a_body:
        list_a.append(a['href'])
    list_a_exception = [
        link,
        link + '/id/',
        link + '/',
        link + '/id',
        link + '/en',
        link + '/home',
        link + '/beranda',
    ]
    data = list(set(list_a).difference(set(list_a_exception)))
    return data


# a = 'dev.apindotrainingcenter.com'
# b = 'https://'
# c = 'apindo'
# d = '9VIiV!QqvPQ8UJ!1lN'
# list_a = all_link_otherpage(b, c, d, a)
# print(list_a)
# print(len(list_a))
