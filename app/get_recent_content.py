# get content from the top RSS feeds in product management. This is assumed to be high quality content.

#import all libraries
import urllib.request
import requests
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import numpy as np
import datetime



#get content from medium


def set_medium_topic(topic):
    return "https://medium.com/tag/" + topic


def scrape_medium(topic):
    driver = webdriver.Chrome('C:/Software Projects/chromedriver_win32/chromedriver.exe')
    driver.get(set_medium_topic(topic))

    # Web scrapper for infinite scrolling page 
    time.sleep(2)  # Allow 2 seconds for the web page to open
    scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break

    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
   
    #prettify res with beautiful soup
    soup = BeautifulSoup(res, 'lxml')

    # finding the right div and class for all links
    extract = soup.find_all('div', {"class": "q ab"})

    #finding the right div and class for all text
    extract2 = soup.find_all('div', {"class": "jx l"})

    titles = []
    for i in extract2:
        titles.append(i.find('h2').text)

    links = []
    for i in extract:
        thing = i.find_all('div', {"class": "ab q"})
        for i in thing:
            links.append(i.find('a').get('href'))

    content = []
    for i in finallinks:
        url = i
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        content.append(soup.get_text())

    finallinks = ['https://www.medium.com' + i for i in links]
    df = pd.DataFrame({'titles': titles, 'links': finallinks})
    df["content"] = content
    df.to_csv(topic + 'data'+ datetime.datetime.now() +'.csv')




#get RSS content

#rss feed directory url
rss_directory_url = 'https://blog.feedspot.com/rss_directory/'

def get_articles_from_rss_feed(rss_feed_url):
    feed = feedparser.parse(rss_feed_url)
    articles = []
    for entry in feed.entries:
        article = {}
        article['title'] = entry.title
        article['link'] = entry.link
        article['summary'] = entry.summary
        articles.append(article)
    return articles

productmanagement_rss_feed_url = 'https://www.producttalk.org/feed/'

articles = get_articles_from_rss_feed(productmanagement_rss_feed_url)

product_management_rss =   'https://blog.feedspot.com/product_management_rss_feeds/'

#parses a url using requests and beautifulsoup and returns links

def get_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    links = soup.find_all('a', class_='ext')
    return links

links = get_links(product_management_rss)

