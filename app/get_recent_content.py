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



#get content from medium

#save the links we wanna scrape


def set_medium_topic(topic):
    return "https://medium.com/tag/" + topic


product_management_medium = "product-management"

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
    #print(soup.prettify())
    b = soup.find_all('div', {"class": "ke kf kg kh ki l"})

    # get text from beautiful soup object and put it in a list
    text = []
    for i in b:
        text.append(i.text)

    # get href link from bs object and put in list
    c = soup.find_all('a', {"class": "ae af ag ah ai aj ak al am an ao ap aq ar as"})

    links = []
    for i in c:
        links.append(i.get('href'))


# remove all items that include the word signin from links

links2 = [i for i in links if 'signin' not in i]
#links2 = [i for i in links2 if '?' not in i]

# remove all duplicates form links2

links3 = list(dict.fromkeys(links2))



# finding the right div and class for all links
extract = soup.find_all('div', {"class": "q ab"})

#finding the right div and class for all text
extract2 = soup.find_all('div', {"class": "jx l"})

len(extract)
len(extract2)

# print length of extract and extract2

print(len(extract))
print(len(extract2))


# find h2 child of extract

titles = []

for i in extract2:
    titles.append(i.find('h2').text)

print(len(titles))

#find href from temp

links2 = []

for i in temp:
    links2.append(i.find('a').get('href'))

links = []

for i in extract:
    thing = i.find_all('div', {"class": "ab q"})
    for i in thing:
        links.append(i.find('a').get('href'))


print(len(links))


finallinks = ['https://www.medium.com' + i for i in links]



df = pd.DataFrame({'titles': titles, 'links': finallinks})

# scrape all text from each link in links4



content = []
for i in finallinks:
    url = i
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    content.append(soup.get_text())

df.to_csv('pmmediumdataframe.csv')









#get RSS content
import feedparser

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

rss_feed_url = 'https://www.producttalk.org/feed/'
articles = get_articles_from_rss_feed(rss_feed_url)

product_management_rss =   'https://blog.feedspot.com/product_management_rss_feeds/'

#parses a url using requests and beautifulsoup and returns links

def get_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    links = soup.find_all('a', class_='ext')
    return links

links = get_links(product_management_rss)

