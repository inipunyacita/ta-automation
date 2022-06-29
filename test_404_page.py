import asyncio
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from optparse import Option
from os import link
import os
from click import option
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time


def page_404_checker(urlprefix, urlcredent, url):
    # Inizialisation
    fortifor = '/hwahaiwhaiwjai'
    msg = ''
    status = ''
    link = urlprefix + urlcredent + url + fortifor
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=os.environ.get(
        "CHROMEDRIVER_PATH"), options=options)
    driver.get(link)
    try:
        driver.find_element(By.XPATH, '//title[contains(.,"Page Not Found")]')
    except WebDriverException:
        status = 'error'
    if (status == 'error'):
        msg = 'Tidak ada'
    else:
        msg = 'Tersedia'

    return msg


async def send_async_404(urlprefix, urlcredent, url):
    return await asyncio.to_thread(page_404_checker, urlprefix, urlcredent, url)
