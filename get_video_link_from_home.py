import time

from bs4 import BeautifulSoup as bs
from scroll_page import Scroll_Page
import re
import requests
import json


def get_id_of_videos(home_link,count):
    l, i = 0, 1
    try:
        while l < count:
            html = Scroll_Page(home_link, i)
            time.sleep(20)
            v = re.findall(r"watch\?v=(\S{11})", html)
            res =[]
            [res.append(x) for x in v if x not in res]
            v= res
            scroll_length = len(v)
            if scroll_length == l:
                break;
            else:
                l = scroll_length
            i = i + 1
        if l > count:
            return v[0:count]
        else:
            return v
    except Exception as e:
        return "Something Wrong"

def title_of_channel(home_link):
    try:
        html = requests.get(home_link)
        html_result = bs(html.text, "html.parser")
        data = re.search(r"var ytInitialData = ({.*?});", str(html_result.prettify())).group(1)
        json_data = json.loads(data)
        ch_name = json_data['header']['c4TabbedHeaderRenderer']['title']
        ch_url = json_data['header']['c4TabbedHeaderRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
        ch_url=ch_url.split("/")[2]
        return ch_name,ch_url
    except Exception as e:
        return "Something Wrong"

def Total_Views(id):
    try:
        link = link = "https://www.youtube.com/watch?v="+id
        html = requests.get(link)
        html_result = bs(html.text, "html.parser")
        views = html_result.find("meta",itemprop="interactionCount")['content']
        return int(views)
    except Exception as e:
        return "NaN"

def Total_Likes(id):
    try:
        link = link = "https://www.youtube.com/watch?v=" + id
        html = requests.get(link)
        html_result = bs(html.text, "html.parser")
        data = re.search(r"var ytInitialData = ({.*?});", str(html_result.prettify())).group(1)
        json_data = json.loads(data)
        videoPIR =json_data['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
        likes_label = videoPIR['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
        likes_str = likes_label.split(' ')[0].replace(',','')
        likes = 0 if likes_str in ['No','NO','No'] else likes_str
        return int(likes)
    except Exception as e:
        return "NaN"
