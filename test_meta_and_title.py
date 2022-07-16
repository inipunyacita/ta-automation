import asyncio
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link
from lxml import etree
from time import perf_counter

# url = 'dev.apindotrainingcenter.com'
# usercredent = 'apindo'
# passcredent = '9VIiV!QqvPQ8UJ!1lN'
# urlprefix = 'https://'


def cek_meta_and_title(urlprefix, usercredent, passcredent, url):
    data_a = all_link(urlprefix, usercredent, passcredent, url)
    list_a_length = len(data_a)
    msg = ''
    status_meta = ''
    list_meta = []
    status_title = ''
    list_title = []
    for i in range(list_a_length):
        try:
            page = requests.get(
                str(data_a[i]), auth=(usercredent, passcredent))
            soup = bs(page.text, "lxml")
            dom = etree.HTML(str(soup))
            title = dom.xpath('//title/text()')
            meta_desc = dom.xpath(
                '//meta[@property="og:description"]/@content')
            meta_title = dom.xpath('//meta[@property="og:title"]/@content')
            meta_desc_content_lorem = dom.xpath(
                '//meta[contains(@property,"og:description") and starts-with(@content, "Lorem") or starts-with(@content, "lorem")]')
        except:
            msg = 'Tidak ditemukan'
            # break
        if (len(meta_title) == 1 and len(meta_desc) == 1):
            if (meta_desc_content_lorem):
                msg = ', '.join(title) + ' | ' + \
                    str(data_a[i]) + ' | Terdapat lorem'
                # break
            else:
                msg = ', '.join(title) + ' | ' + str(data_a[i]) + ' | Ada'
        else:
            msg = ', '.join(title) + ' | ' + str(data_a[i]) + ' | Tidak sesuai'
        data_title_and_desc = ', '.join(
            meta_title) + " | "+', '.join(meta_desc)
        list_meta.append(str(msg))
        list_title.append(str(data_title_and_desc))
        # break
        # # print(meta_title)
        """Script berikut untuk cek halaman apa saja yang tersedia namun tidak dapat dideploy karena akan
        berpotensi menimbulkan timeout karena scraping link yang tidak memiliki batasan dan tergantugn web 
        # if (meta_desc and meta_title):
        #     msg = 'Meta desc untuk halaman' + str(meta_title) + 'tersedia'
        # elif (meta_desc):
        #     msg = 'Meta title tidak ditemukan untuk halaman : ' + str(title)
        # elif (meta_title):
        #     msg = 'Meta desc halaman ' + str(title) + ' tidak ditemukan'
        # else:
        #     msg = 'Meta title dan desc tidak ditemukan di halaman ' + \
        #         str(title)
        # list.append(msg)"""
    # check sesuai/tidak
    if ('tidak sesuai' in str(list_meta).lower()):
        status_meta = 'Terdapat Tidak Ada'
        if ('lorem' in str(list_meta).lower()):
            status_title = 'Terdapat Lorem dan Tidak Sesuai'
        else:
            status_title = 'Terdapat Tidak Sesuai'
    else:
        status_meta = 'Ada'
        status_title = 'Ada'
    return list_meta, list_title, status_meta, status_title


async def send_async_meta_title(urlprefix, usercredent, passcredent, url):
    return await asyncio.to_thread(cek_meta_and_title, urlprefix, usercredent, passcredent, url)

# starttime = perf_counter()
# data = cek_meta_and_title(urlprefix, usercredent, passcredent, url)
# print(data)
# print(f'end time = {perf_counter() - starttime}')


# meta, title, status_meta, status_title = cek_meta_and_title(
#     urlprefix, usercredent, passcredent, url)
# print(status_meta)
# print(status_title)
