import re
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
def get_id_of_videos(home_link,count):
    try:
        html = uReq(home_link)
        html_result = html.read().decode()
        v = re.findall(r"watch\?v=(\S{11})", html_result)
        return (v)
    except Exception as e:
        return "Something Wrong"

