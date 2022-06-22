from test_basic_auth import basic_auth
from test_robot import robot_check
from test_404_page import page_404_checker
from test_footer_homepage import footer_href_check
from test_footer_homepage import footer_text_check
from test_footer_homepage import footer_href_otherpage
from test_footer_homepage import footer_text_otherpage
from flask import Flask, render_template, request
from selenium.common.exceptions import WebDriverException

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/result", methods=['POST', "GET"])
def result():
    output = request.form.to_dict()
    # Isi nama domain tanpa http atau https didalam tanda petik
    url = output["urlwebsite"]
    # Diisi dengan format username:password@
    urlprefix = output["urlprotocol"]
    # Disi dengan urlprefix http:// atau https:// |||| Tergantung status SSL pada web
    urlcredent = output["urlcredent"]

    # check basic auth
    report_basic_auth = basic_auth(urlprefix, url)

    # check robot nofollow & noindex
    report_robot = robot_check(urlprefix, url, urlcredent)

    # check 404 page
    report_404_page = page_404_checker(urlprefix, urlcredent, url)

    # # check footer text credit in homepage
    # report_footer_text_check = footer_text_check(
    #     urlprefix, urlcredent, url)

    # # check footer link credit in homepage
    # report_footer_link_check = footer_href_check(
    #     urlprefix, urlcredent, url)

    # # check footer text credit in otherpage
    # report_footer_text_otherpage = footer_text_otherpage(
    #     urlprefix, urlcredent, url, urldirektori)

    # # check footer link credit in otherpage
    # report_footer_link_otherpage = footer_href_otherpage(
    #     urlprefix, urlcredent, url, urldirektori)

    print('--------------------------------------------------')
    print('STATUS TESTER CHECKLIST :')
    print('--------------------------------------------------')
    print(f"Basic Auth : {report_basic_auth}")
    print(f"Robot Check | Nofollow & noindex : {report_robot}")
    print(f"404 Page Check : {report_404_page}")
    # print(f"Homepage Footer Text: {report_footer_text_check}")
    # print(f"Homepage Footer Link: {report_footer_link_check}")
    # print(f"Otherpage Footer Text: {report_footer_text_otherpage}")
    # print(f"Otherpage Footer Link: {report_footer_link_otherpage}")
    # print('--------------------------------------------------')

    return render_template("index.html", rba=report_basic_auth, rr=report_robot, rfp=report_404_page)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
