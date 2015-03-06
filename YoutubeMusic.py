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
numSongs = raw_input("Number of submissions to fetch (only youtube links will be played):: ")

songListSubmissions = reddit.get_subreddit(subreddit).get_hot(limit=int(numSongs))
songList = [song for song in songListSubmissions]

print "\nSong List::"
printList(songList)

browser = webdriver.Firefox()

for song in songList:
    url = song.url

    if "youtube" in url:
        browser.get(url)
        time.sleep(getVideoLength(url)+5) #5 seconds accounting for ads

    elif "youtu.be" in url:
        browser.get(url)
        mod_url = browser.current_url[:browser.current_url.index('&')] #removing &feature=youtu.be part
        time.sleep(getVideoLength(mod_url)+5)
        
browser.quit()
