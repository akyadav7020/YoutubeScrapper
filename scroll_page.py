from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def Scroll_Page(link,i):
    try:
        option = Options()
        option.headless = True
        driver = webdriver.Chrome(service=Service(r'chromedriver.exe'), options=option)
        driver.get(link)
        time.sleep(5)
        for k in range(i):
            x = 2000 * k + 1
            driver.execute_script("window.scrollBy(0,{})".format(x), "")
            time.sleep(3)
        html = driver.page_source
        return html
    except Exception as e:
        return "Something Wrong"
