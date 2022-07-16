from test_basic_auth import send_async_basic_auth
from test_robot import send_async_robot
from test_404_page import send_async_404
from test_footer_homepage import send_async_footer, send_async_other_footer
from test_meta_and_title import send_async_meta_title
from test_heading import send_async_meta
from test_alt_img import send_async_altimg
from flask import Flask, render_template, request
from time import perf_counter
import asyncio
import time

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/result", methods=['POST', "GET"])
async def result():
    msg3 = ''
    start_at = perf_counter()
    output = request.form.to_dict()
    # Isi nama domain tanpa http atau https didalam tanda petik
    url = output["urlwebsite"]
    # Disi dengan urlprefix http:// atau https:// |||| Tergantung status SSL pada web
    urlprefix = output["urlprotocol"]
    # Diisi dengan username credentials
    usercredent = output["usercredent"]
    # Diisi dengan password credentials
    passcredent = output["passcredent"]

    # Call the function and wait the process

    result = await asyncio.gather(
        await asyncio.to_thread(send_async_basic_auth, urlprefix, url),
        await asyncio.to_thread(send_async_robot, urlprefix, url, usercredent, passcredent),
        await asyncio.to_thread(send_async_footer, urlprefix, usercredent, passcredent, url),
        await asyncio.to_thread(send_async_404, urlprefix, usercredent, passcredent, url),
        await asyncio.to_thread(send_async_other_footer, urlprefix, usercredent, passcredent, url),
        await asyncio.to_thread(send_async_meta_title, urlprefix, usercredent, passcredent, url),
        await asyncio.to_thread(send_async_meta, urlprefix, usercredent, passcredent, url),
        await asyncio.to_thread(send_async_altimg, urlprefix, usercredent, passcredent, url)
    )
    # throw the time counter
    time_counter = perf_counter() - start_at

    return render_template("index.html", result=result, tc=time_counter, userc=usercredent, passc=passcredent, urlp=urlprefix, site=url)


if __name__ == "__main__":
    app.run(debug=True)
