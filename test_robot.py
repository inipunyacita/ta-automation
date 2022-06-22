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

    options = Options()
    options.headless = True
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
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
