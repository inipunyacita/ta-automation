import requests
from bs4 import BeautifulSoup as bs
from lxml import etree
from time import perf_counter
import re

# url = 'dev.littlegiantz.com'
# usercredent = 'littlegiantz'
# passcredent = 'littlegiantz2021'
# urlprefix = 'https://'


def all_link(urlprefix, usercredent, passcredent, url):
    list_a = []
    link = urlprefix + url
    try:
        page_content = requests.get(link, auth=(usercredent, passcredent))
        soup = bs(page_content.text, 'html.parser')
        header = soup.header
        a_body = header.find_all('a', href=re.compile(urlprefix + url))
    except:
        print('Locator tidak ditemukan')
    for a in a_body:
        list_a.append(a['href'])
    return list_a


def all_link_otherpage(urlprefix, usercredent, passcredent, url):
    # inizialitation
    list_a = all_link(urlprefix, usercredent, passcredent, url)
    link = urlprefix + url
    list_a_exception = [
        link,
        link + '/id/',
        link + '/',
        link + '/id',
        link + '/en',
        link + '/home',
        link + '/beranda',
    ]
    # data_diff berisi nilai yang diambil dari sebagian (difference) dari nilai di list_a yang tidak ada di list_a_exception
    data_diff = list(set(list_a).difference(set(list_a_exception)))
    return data_diff
