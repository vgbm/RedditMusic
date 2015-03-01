import praw
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

def printList(list):
    for l in list:
        print l.title

reddit = praw.Reddit(user_agent="Music Player")

subreddit = raw_input("Subreddit:: ")
numSongs = raw_input("Number of songs played:: ")

songListSubmissions = reddit.get_subreddit(subreddit).get_top(limit=int(numSongs))
songList = [song for song in songListSubmissions]

print "\nSong List::"
printList(songList)

browser = webdriver.Firefox()

for song in songList:
    url = song.url
    browser.get(url)

    if "youtube" in url:
        time.sleep(getVideoLength(url)+5) #accounting for ad length
    else:
        time.sleep(300) #sleep 5 min if cant get the time delay
        
browser.quit()
