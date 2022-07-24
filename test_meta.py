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


def cek_meta(urlprefix, usercredent, passcredent, url):
    data_a, pesan = all_link(urlprefix, usercredent, passcredent, url)
    list_a_length = len(data_a)
    msg = ''
    status_meta = ''
    list_meta = []
    for i in range(list_a_length):
        try:
            page = requests.get(
                str(data_a[i]), auth=(usercredent, passcredent))
            soup = bs(page.text, "lxml")
            dom = etree.HTML(str(soup))
            meta_og_desc = dom.xpath(
                '//meta[@property="og:description"]/@content')
            meta_og_title = dom.xpath('//meta[@property="og:title"]/@content')
            meta_desc = dom.xpath('//meta[@name="description"]/@content')
            meta_title = dom.xpath('//meta[@name="title"]/@content')
            meta_desc_content_lorem = dom.xpath(
                '//meta[contains(@property,"og:description") and starts-with(@content, "Lorem") or starts-with(@content, "lorem")]')
        except:
            msg = str(data_a[i]) + ' | Tidak ditemukan'
            # break
        if (len(meta_title) == 1):
            if (len(meta_desc_content_lorem)):
                msg = str(data_a[i]) + ' | Meta Desc Terdapat lorem'
            elif (len(meta_desc) == 1):
                msg = str(data_a[i]) + ' | Meta title & description ada'
            elif (len(meta_og_desc) == 1):
                msg = str(data_a[i]) + ' | meta title & og:description ada'
            elif (len(meta_desc) == 0):
                msg = str(data_a[i]) + ' | Meta description tidak ada'
            elif (len(meta_og_desc) == 0):
                msg = str(data_a[i]) + ' | meta og:description tidak ada'
            else:
                msg = str(data_a[i]) + ' | meta description tidak sesuai'
        elif (len(meta_og_title) == 1):
            if (len(meta_desc_content_lorem)):
                msg = str(data_a[i]) + ' | meta description terdapat lorem'
            elif (len(meta_desc) == 1):
                msg = str(data_a[i]) + ' | meta og:title & description ada'
            elif (len(meta_og_desc) == 1):
                msg = str(data_a[i]) + ' | meta og:title & og:description ada'
            elif (len(meta_desc) == 0):
                msg = str(data_a[i]) + ' | meta description tidak ada'
            elif (len(meta_og_desc) == 0):
                msg = str(data_a[i]) + ' | meta og:description tidak ada'
            else:
                msg = str(data_a[i]) + ' | meta desc tidak sesuai'
        else:
            msg = str(data_a[i]) + ' | meta title / og:title tidak ada'
        # if ((len(meta_title) == 1 and len(meta_desc) == 1) or (len(meta_og_title) == 1 and len(meta_og_desc))):
        #     if (meta_desc_content_lorem):
        #         msg = ', '.join(title) + ' | ' + \
        #             str(data_a[i]) + ' | Meta Desc Terdapat lorem'
        #         # break
        #     else:
        #         msg = ', '.join(title) + ' | ' + \
        #             str(data_a[i]) + ' | Meta Title & Desc Sesuai'
        # elif (len(meta_title) == 0 or len(meta_og_title) == 0):
        #     msg = ', '.join(title) + ' | ' + \
        #         str(data_a[i]) + ' | Meta Title Tidak Ada'
        # elif (len(meta_desc) == 0 or len(meta_og_desc) == 0):
        #     msg = ', '.join(title) + ' | ' + \
        #         str(data_a[i]) + ' | Meta Desc Tidak Ada'
        # else:
        #     msg = ', '.join(title) + ' | ' + \
        #         str(data_a[i]) + ' | Tidak sesuai'
        list_meta.append(str(msg))

    # check sesuai/tidak
    if ('tidak ditemukan' in str(list_meta).lower()):
        status_meta = 'Locator tidak sama'
    elif ('tidak sesuai' in str(list_meta).lower()):
        status_meta = 'Terdapat tidak ada'
    elif ('lorem' in str(list_meta).lower()):
        status_meta = 'Terdapat lorem'
    elif ('tidak ada' in str(list_meta).lower()):
        status_meta = 'Terdapat tidak ada'
    else:
        if ('tidak ditemukan' in pesan.lower()):
            status_meta = 'Error'
        else:
            status_meta = 'Ada'
        # if ('tidak ditemukan' in pesan.lower()):
        #     status_meta = 'Error'
        #     status_title = 'Error'
        # else:
        #     status_meta = 'Ada'
        #     status_title = 'Ada'
    return list_meta, status_meta


async def send_async_meta_tag(urlprefix, usercredent, passcredent, url):
    return await asyncio.to_thread(cek_meta, urlprefix, usercredent, passcredent, url)

# starttime = perf_counter()
# data = cek_meta_and_title(urlprefix, usercredent, passcredent, url)
# print(data)
# print(f'end time = {perf_counter() - starttime}')


# meta, title, status_meta, status_title, desc = cek_meta_and_title(
#     urlprefix, usercredent, passcredent, url)
# print(meta)
# print(status_meta)
# print(desc)
