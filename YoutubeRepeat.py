from selenium import webdriver
from urllib2 import urlopen
from xml.dom.minidom import parseString
import time

def getVideoLength(songURL): #for youtube shit
    urlSeg = songURL[songURL.index('=')+1:]
    url = 'https://gdata.youtube.com/feeds/api/videos/{0}?v=2'.format(urlSeg)
    s = urlopen(url).read()
    d = parseString(s)
    e = d.getElementsByTagName('yt:duration')[0]
    a = e.attributes['seconds']
    v = int(a.value)

    return v

URL = raw_input("Enter the URL:: ")
browser = webdriver.Firefox()

delayTime = getVideoLength(URL)

while True:
    browser.get(URL)
    time.sleep(delayTime)
