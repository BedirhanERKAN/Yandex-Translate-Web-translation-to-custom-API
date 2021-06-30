from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from flask import Flask
from flask import request
import time
import urllib

app = Flask(__name__)

driver_path = r"CHROMEDRIVER PATH"
opts = Options()
opts.add_argument('--headless') 
opts.add_argument('--disable-logging') 
opts.add_argument("--log-level=3")

driver = webdriver.Chrome(chrome_options=opts,executable_path=driver_path)

def ceviri(metin):
    global driver
    
    driver.get("https://ceviri.yandex.com.tr/?lang=en-tr&text="+urllib.parse.quote(metin))
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return (soup.find('pre').text)


@app.route("/")
def hello_world():
    metin = request.args.get("metin")

    return ceviri(metin)

