import asyncio
from lxml import etree
import re
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link

# url = 'dev.valtatech.com/'
# usercredent = ''
# passcredent = ''


def cek_https(usercredent, passcredent, site) :
    uc = usercredent
    pc = passcredent
    link = 'http://' + site
    r = requests.get(link, auth=(uc, pc))
    response_url = r.url
    if ('https://' in response_url):
        status = 'Sesuai'
    elif ('http://' in response_url):
        status = 'Tidak sesuai'
    else:
        status = 'Error'
    return status

async def send_async_https(usercredent, passcredent, url):
    return cek_https(usercredent, passcredent, url)

# cek = cek_https(usercredent, passcredent, url)
# print(cek)