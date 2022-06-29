from tracemalloc import start
from test_basic_auth import send_async_basic_auth
from test_robot import send_async_robot
from test_404_page import send_async_404
from test_footer_homepage import send_async_footer
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
    start_at = perf_counter()
    output = request.form.to_dict()
    # Isi nama domain tanpa http atau https didalam tanda petik
    url = output["urlwebsite"]
    # Diisi dengan format username:password@
    urlprefix = output["urlprotocol"]
    # Disi dengan urlprefix http:// atau https:// |||| Tergantung status SSL pada web
    urlcredent = output["urlcredent"]

    # # check basic auth
    # report_basic_auth = await asyncio.to_thread(target=basic_auth, args=(urlprefix, url))

    # # check footer text & link credit in homepage
    # report_footer_homepage_check = await asyncio.to_thread(target=footer_homepage_check, args=(urlprefix, urlcredent, url))

    # # check robot nofollow & noindex
    # report_robot = await robot_check(urlprefix, url, urlcredent)

    result = await asyncio.gather(
        await asyncio.to_thread(send_async_basic_auth, urlprefix, url),
        await asyncio.to_thread(send_async_robot, urlprefix, url, urlcredent),
        await asyncio.to_thread(send_async_footer, urlprefix, urlcredent, url),
        await asyncio.to_thread(send_async_404, urlprefix, urlcredent, url)
    )
    print(result)
    print(f"time counter : {perf_counter() - start_at}")
    time_counter = perf_counter() - start_at
    # # check 404 page
    # report_404_page = page_404_checker(urlprefix, urlcredent, url)

    # # check footer text credit in otherpage
    # report_footer_text_otherpage = footer_text_otherpage(
    #     urlprefix, urlcredent, url, urldirektori)

    # # check footer link credit in otherpage
    # report_footer_link_otherpage = footer_href_otherpage(
    #     urlprefix, urlcredent, url, urldirektori)

    # print('--------------------------------------------------')
    # print('STATUS TESTER CHECKLIST :')
    # print('--------------------------------------------------')
    # print(f"Basic Auth : {report_basic_auth}")
    # # print(f"Robot Check | Nofollow & noindex : {report_robot}")
    # # print(f"404 Page Check : {report_404_page}")
    # print(f"Homepage Footer Text & Link : {report_footer_homepage_check}")
    # # print(f"Otherpage Footer Text: {report_footer_text_otherpage}")
    # # print(f"Otherpage Footer Link: {report_footer_link_otherpage}")
    # # print('--------------------------------------------------')

    return render_template("index.html", result=result, tc=time_counter)


if __name__ == "__main__":
    app.run(debug=True)
