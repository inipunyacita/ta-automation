import os
from telnetlib import STATUS
from urllib import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time


def robot_check(urlprefix, url, urlcredent):
    msg = ''
    status = ''
    link = urlprefix + urlcredent + url

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
        driver.find_element(
            By.XPATH, "//meta[contains(@name,'robots') and contains(@content,'nofollow') and contains(@content,'noindex')]")
    except WebDriverException:
        status = 'error'

    if (status == 'error'):
        msg = "Tidak ditemukan"
    else:
        msg = "Ditemukan"
    return msg
