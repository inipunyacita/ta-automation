import asyncio
from cgitb import text
from gettext import find
from re import S
from tabnanny import check
import requests
from bs4 import BeautifulSoup as bs
from get_all_link import all_link_otherpage
from lxml import etree
from time import perf_counter

# url = 'solar-studio.timedoor-host.my.id'
# usercredent = 'solarstudio'
# passcredent = 'solarstudio2021'
# urlprefix = 'https://'

url = 'dev.valtatech.com/'
usercredent = ''
passcredent = ''
urlprefix = 'https://'


def cek_bc(urlprefix, usercredent, passcredent, url):

    # all_link_otherpage(protocol, credent, url)
    list_a, pesan = all_link_otherpage(
        urlprefix, usercredent, passcredent, url)
    list_a_length = len(list_a)
    msg = ''
    msg_status = ''
    filtered = []
    status_bc = []
    for i in range(list_a_length):
        data_textbc = []
        try:
            page = requests.get(
                str(list_a[i]), auth=(usercredent, passcredent))
            soup = bs(page.text, "lxml")
            ol = soup.find('ol', {'class': 'breadcrumb'})
            data = ol.find_all('li')
            for val in data:
                textbc = val.getText()
                bc = '' + str(textbc) + ' >'
                data_textbc.append(bc)
                if (len(data_textbc) < 2):
                    msg = str(list_a[i]) + ' | Tidak sesuai | ' + ' '.join(data_textbc)
                else:
                    msg = str(list_a[i]) + ' | ' + ' '.join(data_textbc)
            
        except:
            msg = str(list_a[i]) + ' | Tidak ditemukan '

        status_bc.append(msg)
        def filter_list(variable):
            letters = [
                str(list_a[i]) + ' | Tidak sesuai | ' + ' '.join(data_textbc),
                str(list_a[i]) + ' | Tidak ditemukan '
            ]
            if (variable in letters):
                return True
            else:
                return False
        
        # using filter function
        exception = filter(filter_list, status_bc)
        
        for i in exception:
            filtered.append(i)
    # check sesuai/tidak
    if ('tidak sesuai' in str(status_bc).lower()):
        msg_status = 'Terdapat tidak sesuai'
        return msg_status, filtered
    elif ('tidak ditemukan' in str(status_bc).lower()):
        msg_status = 'Terdapat tidak ditemukan'
        return msg_status, status_bc
    else:
        if ('tidak ditemukan' in pesan.lower()):
            msg_status = 'Error'
            return msg_status, filtered
        elif ('tidak cocok' in pesan.lower()):
            msg_status = 'Error ketika get all link'
            return msg_status, filtered
        else:
            msg_status = 'Ada'
            return msg_status, status_bc
    


async def send_async_bc(urlprefix, usercredent, passcredent, url):
    return cek_bc(urlprefix, usercredent, passcredent, url)

# status = cek_bc(urlprefix, usercredent, passcredent, url)
# print(status)

