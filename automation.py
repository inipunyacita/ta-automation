from tracemalloc import start
from test_basic_auth import send_async_basic_auth
from test_robot import send_async_robot
from test_404_page import send_async_404
from test_footer_homepage import send_async_footer, send_async_other_footer
# from open_all_link import send_async_meta
# from test_footer_homepage import footer_text_check
# from test_footer_homepage import footer_href_otherpage
# from test_footer_homepage import footer_text_otherpage
from flask import Flask, render_template, request
from selenium.common.exceptions import WebDriverException
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
        await asyncio.to_thread(send_async_other_footer, urlprefix, usercredent, passcredent, url)
        # await asyncio.to_thread(send_async_meta, urlprefix, usercredent, passcredent, url)
    )
    # throw the time counter
    time_counter = perf_counter() - start_at

    return render_template("index.html", result=result, tc=time_counter)


if __name__ == "__main__":
    app.run(debug=True)
