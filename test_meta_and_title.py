import asyncio
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link
from lxml import etree
from time import perf_counter

# url = 'dev.littlegiantz.com'
# usercredent = 'littlegiantz'
# passcredent = 'littlegiantz2021'
# urlprefix = 'https://'


def cek_meta_and_title(urlprefix, usercredent, passcredent, url):
    data_a, pesan = all_link(urlprefix, usercredent, passcredent, url)
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
            msg = ', '.join(title) + ' | ' + \
                str(data_a[i]) + ' | Tidak ditemukan'
            # break
        if (len(meta_title) == 1 and len(meta_desc) == 1):
            if (meta_desc_content_lorem):
                msg = ', '.join(title) + ' | ' + \
                    str(data_a[i]) + ' | Terdapat lorem'
                # break
            else:
                msg = ', '.join(title) + ' | ' + \
                    str(data_a[i]) + ' | Sesuai'
        else:
            msg = ', '.join(title) + ' | ' + \
                str(data_a[i]) + ' | Tidak sesuai'
        data_title_and_desc = ', '.join(
            meta_title) + " | " + str(data_a[i]) + " | "+', '.join(meta_desc)
        list_meta.append(str(msg))
        list_title.append(str(data_title_and_desc))
    # check sesuai/tidak
    if ('tidak sesuai' in str(list_meta).lower()):
        status_meta = 'Terdapat tidak ada'
        if ('lorem' in str(list_meta).lower()):
            status_title = 'Terdapat lorem dan tidak Sesuai'
        else:
            status_title = 'Terdapat tidak ada'
    elif ('tidak ditemukan' in str(list_meta).lower()):
        status_meta = 'Terdapat tidak ditemukan'
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
# print(title)
# print(status_meta)
