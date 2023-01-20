import requests
from bs4 import BeautifulSoup as bs
from lxml import etree
from time import perf_counter
import re

# url = 'balita.co/'
# usercredent = ''
# passcredent = ''
# urlprefix = 'https://'

# url = 'timedooracademy.com/'
# usercredent = ''
# passcredent = ''
# urlprefix = 'https://'

url = 'dev.mydaycation.id/'
usercredent = ''
passcredent = ''
urlprefix = 'https://'

def all_link(urlprefix, usercredent, passcredent, url):
    msg = ''
    list_a = []
    link = urlprefix + url
    try:
        page_content = requests.get(link, auth=(usercredent, passcredent))
        soup = bs(page_content.text, 'html.parser')
        body = soup.body
        for a in body.find_all('a', href=re.compile(url)):
            list_a.append(a['href'])
    except:
        msg = 'Locator tidak ditemukan'
    
    list_link = set(list_a)
    all_link = list(list_link)
    if (len(all_link) == 0):
        msg = 'Link tidak cocok'
    return all_link, msg


def all_link_otherpage(urlprefix, usercredent, passcredent, url):
    # inizialitation
    info = ''
    try:
        list_a, msg= all_link(urlprefix, usercredent, passcredent, url)
        link = urlprefix + url
        list_a_exception = [
            '#',
            link,
            link + '',
            link + '/id/',
            link + '/',
            link + '/id',
            link + '/home',
            link + '/id/beranda/',
            link + '/id/beranda',
            link + '/beranda',
            link + 'id/',
            link + 'id',
            link + 'en',
            link + '/en',
            link + 'en/',
            link + '/en/',
            link + 'sa',
            link + '/sa',
            link + 'sa/',
            link + '/sa/',
            link + 'bd',
            link + '/bd',
            link + 'bd/',
            link + '/bd/',
            link + 'in',
            link + '/in',
            link + 'in/',
            link + '/in/',
            link + 'jp',
            link + '/jp',
            link + 'jp/',
            link + '/jp/',
            link + 'my',
            link + '/my',
            link + 'my/',
            link + '/my/',
            link + 'eg',
            link + '/eg',
            link + 'eg/',
            link + '/eg/',
            link + 'ru',
            link + '/ru',
            link + 'ru/',
            link + '/ru/',
            link + 'sg',
            link + '/sg',
            link + 'sg/',
            link + '/sg/',
            link + 'vn',
            link + '/vn',
            link + 'vn/',
            link + '/vn/',
            link + 'home',
            link + 'id/beranda/',
            link + 'id/beranda',
            link + 'beranda',
            link + 'beranda/',
            '\n\n              \n                '+link+'\n              ',
            '\n\n              \n                '+link+'/\n'+'              ',
            '\n\t\t\t\t    \t\t\t              \t\t'+link+'\t\t              \t\t\t\t\t'+'    '
        ]
        # data_diff berisi nilai yang diambil dari sebagian (difference) dari nilai di list_a yang tidak ada di list_a_exception
        data_diff = list(set(list_a).difference(set(list_a_exception)))
    except:
        info = 'Locator tidak ditemukan'
    if (msg == 'Link tidak cocok'):
        info = 'Link tidak cocok'
    return data_diff, info

# data1, data2 = all_link(urlprefix, usercredent, passcredent, url)
# data3, data4 = all_link_otherpage(urlprefix, usercredent, passcredent, url)

# print(data1)
# print(data2)
# print(data3)
# print(data4)