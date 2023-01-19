import asyncio
from bs4 import BeautifulSoup as bs
import requests
from lxml import etree
import time

# url = 'citananta.my.id/cakarentcar'
# usercredent = ''
# passcredent = ''
# urlprefix = 'https://'


def robot_check(urlprefix, url, usercredent, passcredent):
    msg = ''
    status = ''
    link = urlprefix + url
    
    try:
        page = requests.get(link, auth=(usercredent, passcredent))
        soup = bs(page.text, 'lxml')
        dom = etree.HTML(str(soup))
        robot = dom.xpath(
            "//meta[contains(@name,'robots') and contains(@content,'nofollow') and contains(@content,'noindex')]")
        # check if locator correct, it will be found
        if (robot):
            msg = 'Sesuai'
        else:
            msg = 'Tidak sesuai'
    except:
        msg = 'Tidak ditemukan'
    return msg


# print(robot_check(urlprefix, url, usercredent, passcredent))

async def send_async_robot(urlprefix, url, usercredent, passcredent):
    return robot_check(urlprefix, url, usercredent, passcredent)
