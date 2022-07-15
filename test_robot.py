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
    # options = webdriver.ChromeOptions()
    # options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--headless')
    # options.add_argument('--incognito')
    # # options.add_argument('--no-sandbox')
    # driver = webdriver.Chrome(options=options)
    # # executable_path=os.environ.get(
    # #     "CHROMEDRIVER_PATH"),
    # driver.get(link)
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
    return await asyncio.to_thread(robot_check, urlprefix, url, usercredent, passcredent)
