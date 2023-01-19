import asyncio
from tabnanny import check
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link
from lxml import etree
from time import perf_counter

# url = 'dev.littlegiantz.com'
# usercredent = 'littlegiantz'
# passcredent = 'littlegiantz2021'
# urlprefix = 'https://'

# url = 'tunanta.merthanaya.co.id'
# usercredent = ''
# passcredent = ''
# urlprefix = 'https://'


def cek_alt_img(urlprefix, usercredent, passcredent, url):

    # all_link_otherpage(protocol, credent, url)
    list_a, pesan = all_link(urlprefix, usercredent, passcredent, url)
    list_a_length = len(list_a)
    msg = ''
    msg_status = ''
    filtered = []
    img = []
    starttime = perf_counter()
    for i in range(list_a_length):
        try:
            page = requests.get(
                str(list_a[i]), auth=(usercredent, passcredent))
            soup = bs(page.text, "lxml")
            dom = etree.HTML(str(soup))
            img_with_alt = dom.xpath('//img/@alt')
            all_img = dom.xpath('//img')
            alt_without_value = dom.xpath('//img[@alt=""]')
            if (len(all_img) != 0):
                if (len(alt_without_value) == 0):
                    if (len(all_img) == len(img_with_alt)):
                        msg = str(list_a[i]) + ' | Sesuai'
                    elif (len(all_img) > len(img_with_alt)):
                        msg = str(list_a[i]) + ' | Terdapat tidak sesuai, img tanpa alt'
                    else:
                        msg = str(list_a[i]) + ' | terdapat Tidak Sesuai'
                elif (len(alt_without_value) > 0):
                    msg = str(list_a[i]) + ' | Terdapat tidak sesuai, Alt tidak berisi value'
                else:
                    msg = str(list_a[i]) + ' | Terdapat tidak sesuai, img tanpa alt'
            else:
                msg = str(list_a[i]) + ' | Image Tidak ada'         
        except:
            msg = str(list_a[i]) + ' | Tidak ditemukan'
        img.append(msg)

        def filter_list(variable):
            letters = [
                str(list_a[i]) + ' | Image Tidak ada',
                str(list_a[i]) + ' | terdapat Tidak Sesuai',
                str(list_a[i]) + ' | Tidak ditemukan',
                str(list_a[i]) + ' | Terdapat tidak sesuai, img tanpa alt',
                str(list_a[i]) + ' | Terdapat tidak sesuai, Alt tidak berisi value'
            ]
            if (variable in letters):
                return True
            else:
                return False
        
        # using filter function
        exception = filter(filter_list, img)
        
        for i in exception:
            filtered.append(i)
    # check sesuai/tidak
    if ('tidak sesuai' in str(img).lower()):
        msg_status = 'Terdapat tidak sesuai'
        return msg_status, filtered
    elif ('tidak ditemukan' in str(img).lower()):
        msg_status = 'Terdapat tidak ditemukan'
        return msg_status, filtered
    elif ('tidak ada' in str(img).lower()):
        msg_status = 'Terdapat tidak ada'
        return msg_status, filtered
    else:
        if ('tidak ditemukan' in pesan.lower()):
            msg_status = 'Error'
            return msg_status, filtered
        elif ('tidak cocok' in pesan.lower()):
            msg_status = 'Error ketika get all link'
            return msg_status, filtered
        else:
            msg_status = 'Sesuai'
            return msg_status, img
    


async def send_async_altimg(urlprefix, usercredent, passcredent, url):
    return cek_alt_img(urlprefix, usercredent, passcredent, url)


# status, data_img = cek_alt_img(urlprefix, usercredent, passcredent, url)
# print(status)
# print(data_img)
