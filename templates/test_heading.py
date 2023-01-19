import asyncio
from tabnanny import check
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link
from lxml import etree
from time import perf_counter

# url = 'dev.apindotrainingcenter.com'
# usercredent = 'apindo'
# passcredent = '9VIiV!QqvPQ8UJ!1lN'
# urlprefix = 'https://'

# url = 'tunanta.merthanaya.co.id'
# usercredent = ''
# passcredent = ''
# urlprefix = 'https://'


def cek_heading(urlprefix, usercredent, passcredent, url):

    # all_link_otherpage(protocol, credent, url)
    list_a, pesan = all_link(urlprefix, usercredent, passcredent, url)
    list_a_length = len(list_a)
    msg = ''
    msg_status = ''
    filtered = []
    status_heading = []
    list_heading = []
    for i in range(list_a_length):
        data_text_h = []
        try:
            page = requests.get(
                str(list_a[i]), auth=(usercredent, passcredent))
            soup = bs(page.text, "lxml")
            h1 = soup.find_all("h1")
            list_heading = soup.find_all(["h1", "h2", "h3"])
            # h2 = soup.find_all("h2")
            if (len(list_heading) == 0):
                msg = str(list_a[i]) + ' | Heading tag Tidak ada'
            else:
                if (len(h1) == 0):
                    msg = str(list_a[i]) + ' | H1 Tidak ada'
                elif (len(h1) == 1):
                    msg = str(list_a[i]) + ' | ' + str(list_heading)
                else:
                    msg = str(list_a[i]) + ' | Tidak sesuai | h1 berjumlah bukan 1'
        except:
            msg = str(list_a[i]) + ' | Tidak ditemukan'
        
        status_heading.append(msg)
        def filter_list(variable):
            letters = [
                str(list_a[i]) + ' | Heading tag Tidak ada',
                str(list_a[i]) + ' | H1 Tidak ada',
                str(list_a[i]) + ' | Tidak sesuai | h1 berjumlah bukan 1', 
                str(list_a[i]) + ' | Tidak ditemukan'
            ]
            if (variable in letters):
                return True
            else:
                return False
        
        # using filter function
        exception = filter(filter_list, status_heading)
        
        for i in exception:
            filtered.append(i)
    #     # check sesuai/tidak
    if ('tidak sesuai' in str(status_heading).lower()):
        msg_status = 'Terdapat tidak sesuai'
        return msg_status, filtered
    elif ('tidak ada' in str(status_heading).lower()):
        msg_status = 'Terdapat tidak ada'
        return msg_status, filtered
    elif ('tidak ditemukan' in str(status_heading).lower()):
        msg_status = 'Terdapat tidak ditemukan'
        return msg_status, filtered
    else:
        if ('tidak ditemukan' in pesan.lower()):
            msg_status = 'Error'
            return msg_status, filtered
        elif ('tidak cocok' in pesan.lower()):
            msg_status = 'Error ketika get all link'
            return msg_status, filtered
        else:
            msg_status = 'Ada'
            return msg_status, status_heading
    


async def send_async_heading(urlprefix, usercredent, passcredent, url):
    return cek_heading(urlprefix, usercredent, passcredent, url)

# data, status = cek_heading(urlprefix, usercredent, passcredent, url)
# print(data)
# print(status)
