from lib2to3.pgen2 import driver
from nturl2path import url2pathname
from os import link
from sqlite3 import Time
from telnetlib import STATUS
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

import requests
import asyncio


def basic_auth(urlprefix, url):
    __credent = ''
    msg = ''
    r = ''

    try:
        r = requests.get(urlprefix + url, __credent)
    except WebDriverException:
        print('modul error')

    if(r.status_code == 401):
        msg = 'Tersedia'
    elif(r.status_code == 200):
        msg = 'Tidak Ada'
    return msg


async def send_async_basic_auth(urlprefix, url):
    return await asyncio.to_thread(basic_auth, urlprefix, url)
