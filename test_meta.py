import asyncio
from cgitb import text
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link
from lxml import etree
from time import perf_counter

# url = 'dev.san-ei.co.id/'
# usercredent = ''
# passcredent = ''
# urlprefix = 'http://'


def cek_meta(urlprefix, usercredent, passcredent, url):
    data_a, pesan = all_link(urlprefix, usercredent, passcredent, url)
    list_a_length = len(data_a)
    msg = ''
    status_meta = ''
    filtered = []
    list_meta = []
    list_meta_title = []
    for i in range(list_a_length):
        meta_title = []
        meta_desc = None 
        meta_desc_content_lorem = None
        try:
            page = requests.get(str(data_a[i]), auth=(usercredent, passcredent))
            soup = bs(page.text, "lxml")
            dom = etree.HTML(str(soup))
            meta_og_desc = dom.xpath(
                '//meta[@property="og:description"]/@content')
            meta_og_title = dom.xpath('//meta[@property="og:title"]/@content')
            meta_desc = dom.xpath('//meta[@name="description"]/@content')
            meta_title = dom.xpath('//title/text()')
            meta_desc_content_lorem = dom.xpath(
                '//meta[contains(@property,"og:description") and starts-with(@content, "Lorem") or starts-with(@content, "lorem")]')
            list_meta_title.append(meta_title)
            if (len(meta_title) > 1):
                if (len(meta_desc_content_lorem)):
                    msg = str(data_a[i]) + ' | Meta Description Terdapat lorem'
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
            else:
                msg = str(data_a[i]) + ' | meta title tidak ada'
        except:
            msg = str(data_a[i]) + ' | Tidak ditemukan'
        list_meta.append(str(msg))
        
        def filter_list(variable):
            letters = [
                str(data_a[i]) + ' | Meta Description Terdapat lorem', 
                str(data_a[i]) + ' | Meta description tidak ada',
                str(data_a[i]) + ' | meta og:description tidak ada',
                str(data_a[i]) + ' | meta description tidak sesuai',
                str(data_a[i]) + ' | meta title tidak ada',
                str(data_a[i]) + ' | Tidak ditemukan'
            ]
            if (variable in letters):
                return True
            else:
                return False
        
        # using filter function
        exception = filter(filter_list, list_meta)
        
        for i in exception:
            filtered.append(i)
    
    # check sesuai/tidak
    if ('tidak ditemukan' in str(list_meta).lower()):
        status_meta = 'Locator tidak sama'
        return filtered, status_meta
    elif ('tidak sesuai' in str(list_meta).lower()):
        status_meta = 'Terdapat tidak sesuai'
        return filtered, status_meta
    elif ('lorem' in str(list_meta).lower()):
        status_meta = 'Terdapat lorem'
        return filtered, status_meta
    elif ('tidak ada' in str(list_meta).lower()):
        status_meta = 'Terdapat tidak ada'
        return filtered, status_meta
    else:
        if ('tidak ditemukan' in pesan.lower()):
            status_meta = 'Error'
            return filtered, status_meta
        elif ('tidak cocok' in pesan.lower()):
            status_meta = 'Error ketika get all link'
            return filtered, status_meta
        else:
            status_meta = 'Ada'
            return list_meta, status_meta
    


async def send_async_meta_tag(urlprefix, usercredent, passcredent, url):
    return cek_meta(urlprefix, usercredent, passcredent, url)

# a, b = cek_meta(urlprefix, usercredent, passcredent, url)
# print(a)
# print(b)
# starttime = perf_counter()
# data, status = cek_meta(urlprefix, usercredent, passcredent, url)
# print(data)
# print(status)
# print(f'end time = {perf_counter() - starttime}')


# meta, title, status_meta, status_title, desc = cek_meta_and_title(
#     urlprefix, usercredent, passcredent, url)
# print(meta)
# print(status_meta)
# print(desc)
