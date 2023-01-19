from test_basic_auth import send_async_basic_auth
from test_robot import send_async_robot
from test_404_page import send_async_404
from test_footer_homepage import send_async_footer, send_async_other_footer
from test_meta import send_async_meta_tag
from test_title import send_async_title
from test_heading import send_async_heading
from test_alt_img import send_async_altimg
from test_breadcrumb import send_async_bc
from test_captcha import send_async_cek_captcha
from test_https import send_async_https
from test_analytics import send_async_analitik
from test_favicon import send_async_favicon
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
    result = await asyncio.gather (
        send_async_basic_auth(urlprefix, url),
        send_async_robot(urlprefix, url, usercredent, passcredent),
        send_async_footer(urlprefix, usercredent, passcredent, url),
        send_async_404(urlprefix, usercredent, passcredent, url),
        send_async_other_footer(urlprefix, usercredent, passcredent, url),
        send_async_cek_captcha(urlprefix, usercredent, passcredent, url),
        send_async_https(usercredent, passcredent, url),
        send_async_meta_tag(urlprefix, usercredent, passcredent, url),
        send_async_title(urlprefix, usercredent, passcredent, url),
        send_async_heading(urlprefix, usercredent, passcredent, url),
        send_async_altimg(urlprefix, usercredent, passcredent, url),
        send_async_bc(urlprefix, usercredent, passcredent, url),
        send_async_analitik(urlprefix, url, usercredent, passcredent),
        send_async_favicon(urlprefix, url, usercredent, passcredent)
    )
    # throw the time counter
    time_counter = perf_counter() - start_at

    return render_template("index.html", result=result, tc=time_counter, userc=usercredent, passc=passcredent, urlp=urlprefix, site=url)
    
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5003)
