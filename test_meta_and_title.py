import asyncio
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link
from lxml import etree
from time import perf_counter

# url = 'solar-studio.timedoor-host.my.id'
# usercredent = 'solarstudio'
# passcredent = 'solarstudio2021'
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
                    str(data_a[i]) + ' | Meta Desc Terdapat lorem'
                # break
            else:
                msg = ', '.join(title) + ' | ' + \
                    str(data_a[i]) + ' | Meta Desc Sesuai'
        elif (len(meta_title) == 0):
            msg = ', '.join(title) + ' | ' + \
                str(data_a[i]) + ' | Meta Title Tidak Ada'
        elif (len(meta_desc) == 0):
            msg = ', '.join(title) + ' | ' + \
                str(data_a[i]) + ' | Meta Desc Tidak Ada'
        else:
            msg = ', '.join(title) + ' | ' + \
                str(data_a[i]) + ' | Tidak sesuai'
        data_title_and_desc = ', '.join(
            meta_title) + " | " + str(data_a[i])
        list_meta.append(str(msg))
        list_title.append(str(data_title_and_desc))
    # check sesuai/tidak
    if ('tidak sesuai' in str(list_meta).lower()):
        if ('lorem' in str(list_meta).lower()):
            status_title = 'Terdapat lorem'
            status_meta = 'Terdapat lorem'
        else:
            status_title = 'Terdapat tidak sesuai'
            status_meta = 'Terdapat tidak ada'
    elif ('tidak ada' in str(list_meta).lower()):
        status_meta = 'Terdapat tidak ada'
        status_title = 'Terdapat tidak ada'
    else:
        if ('tidak ditemukan' in pesan.lower()):
            status_meta = 'Error'
            status_title = 'Error'
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


# meta, title, status_meta, status_title, desc = cek_meta_and_title(
#     urlprefix, usercredent, passcredent, url)
# print(meta)
# print(status_meta)
# print(desc)
