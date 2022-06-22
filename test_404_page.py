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
    options.add_argument('--incognito')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path=os.environ.get(
        "CHROMEDRIVER_PATH"), options=options)

    # Start
    try:
        driver.get(link)
    except WebDriverException:
        status = 'error'
    if (status == 'error'):
        msg = 'Script error'
    else:
        msg = 'Cek hasil pada browser yang otomatis terbuka & pastikan page 404 not found tersedia'

    return msg
