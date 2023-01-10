# get content from the top RSS feeds in product management. This is assumed to be high quality content.

#import all libraries
import urllib.request
import requests
import bs4
from bs4 import BeautifulSoup



#save the links we wanna scrape
arificial_intelligence = "https://medium.com/tag/product-management"

from selenium import webdriver