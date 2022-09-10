from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
import re
import json
def get_id_of_videos(home_link):
    #home_link = "https://www.youtube.com/user/zeemusiccompany/videos"
    html = uReq(home_link)
    #beutified_page = bs(html.read(),"html.parser")
    html_result = html.read().decode()
    print(html.read().decode())
    """ Getting video links """
    #v = re.findall(r"watch\?v=(\S{11})",beutified_page.decode())
    v = re.findall(r"watch\?v=(\S{11})",html_result)
    return v

link = "https://www.youtube.com/user/zeemusiccompany/videos"

html = uReq(link)
beutified_page = bs(html.read(),"html.parser")
data = re.search("var ytInitialData = ({.*});",str(beutified_page.prettify())).group(1)
json_data = json.loads(data)
print(beutified_page)