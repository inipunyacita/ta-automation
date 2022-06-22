from cgitb import text
from lib2to3.pgen2 import driver
from operator import contains
from os import link
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time

# function
# check footer link homepage


def footer_href_check(urlprefix, urlcredent, url):

    # inizialitation
    msg = ''
    options = Options()
    linkhomepage = urlprefix + urlcredent + url
    options.headless = True
    driver = webdriver.Chrome(options=options)

    # start cek footer link in homepage
    driver.get(linkhomepage)
    try:
        driver.find_element(
            By.XPATH, '//a[contains(.,"PT. Timedoor Indonesia")]')
    except WebDriverException:
        msg = 'Belum sesuai, belum terdapat footer link pada homepage'
    else:
        msg = 'Sesuai, footer link sudah tersedia pada homepage'
    return msg

# check footer text homepage


def footer_text_check(urlprefix, urlcredent, url):
    # inizialitation
    msg = ''
    options = Options()
    linkhomepage = urlprefix + urlcredent + url
    options.headless = True
    driver = webdriver.Chrome(options=options)
    # start cek text credit in homepage
    driver.get(linkhomepage)
    try:
        driver.find_element(
            By.XPATH, '//a[contains(text(),"PT. Timedoor Indonesia")]')
    except:
        msg = 'Belum sesuai, belum terdapat text credit PT. Timedoor Indonesia pada homepage'
    else:
        msg = 'Sesuai, text credit sudah tersedia pada homepage'

    return msg


def footer_href_otherpage(urlprefix, urlcredent, url, urldirektori):

    # inizialitation
    msg = ''
    options = Options()
    otherlink = urlprefix + urlcredent + url + urldirektori
    options.headless = True
    driver = webdriver.Chrome(options=options)

    # start cek footer link in otherpage
    driver.get(otherlink)
    try:
        driver.find_element(
            By.XPATH, '//a[@href="https://timedoor.net"]')
    except:
        msg = 'Sesuai, footer link sudah tidak ada'
    else:
        msg = 'Belum Sesuai, footer link masih tersedia'
    return msg

# check footer text otherpage


def footer_text_otherpage(urlprefix, urlcredent, url, urldirektori):
    # inizialitation
    msg = ''
    options = Options()
    otherlink = urlprefix + urlcredent + url + urldirektori
    options.headless = True
    driver = webdriver.Chrome(options=options)
    # start cek text credit in otherpage
    driver.get(otherlink)
    try:
        driver.find_element(
            By.XPATH, '//p[contains(.,"PT. Timedoor Indonesia")]')
    except:
        msg = 'Belum sesuai, belum terdapat text credit PT. Timedoor Indonesia pada otherpage'
    else:
        msg = 'Sesuai, text credit sudah tersedia pada otherpage'

    return msg
