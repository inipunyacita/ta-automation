import time
import requests
import asyncio


def basic_auth(urlprefix, url):
    __credent = ''
    msg = ''
    r = ''

    try:
        r = requests.get(urlprefix + url, __credent)
    except:
        msg = 'Request gagal'

    if(r.status_code == 401):
        msg = 'Ada'
    elif(r.status_code == 200):
        msg = 'Tidak ada'
    return msg


async def send_async_basic_auth(urlprefix, url):
    return await asyncio.to_thread(basic_auth, urlprefix, url)
