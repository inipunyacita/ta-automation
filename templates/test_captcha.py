import asyncio
from cgitb import html
from lxml import etree
import re
import requests
from bs4 import BeautifulSoup as bs

# url = 'leafybali.com/'
# usercredent = ''
# passcredent = ''
# urlprefix = 'http://'

def cek_captcha(urlprefix, usercredent, passcredent, url) :
    try:
        link = urlprefix + url
        page = requests.get(str(link), auth=(usercredent, passcredent))
        soup = bs(page.text, 'lxml')
        dom = etree.HTML(str(soup))
        scriptdata = dom.xpath('//script[contains(@src, "https://www.google.com/recaptcha/api.js")]')
        if(scriptdata):
            msg = 'Ada'
        else:
            msg = 'Tidak ada'
    except:
        msg = 'Error'
    return msg

async def send_async_cek_captcha(urlprefix, usercredent, passcredent, url):
    return cek_captcha(urlprefix, usercredent, passcredent, url)

# cek = cek_captcha(urlprefix, usercredent, passcredent, url)
# print(cek)