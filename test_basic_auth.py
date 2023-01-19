import time
import requests
import asyncio

# url = 'solar-studio.timedoor-host.my.id/'
# usercredent = 'solarstudio'
# passcredent = 'solarstudio2021'
# urlprefix = 'https://'

def basic_auth(urlprefix, url):
    site = urlprefix + url
    headers = {
    'User-Agent': 'A',
    'From': 'developer@timedoor.net' 
    }
    msg = ''
    try:
        r = requests.get(site, headers=headers)
        if (r.status_code == 200):
            msg = 'Tidak ada'
        else:
            msg = 'Ada'
    except:
        msg = 'Request gagal'

    return msg


async def send_async_basic_auth(urlprefix, url):
    return basic_auth(urlprefix, url)

# result = basic_auth(urlprefix,url)
# print(result)
