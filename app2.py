# write a python script to scrape all page url's for every page on reforge.com


# import libraries
import requests
from bs4 import BeautifulSoup
import re

# specify the url
url = 'https://program.reforge.com/c/product-series-eg/leading-a-product-strategy/from-product-management-to-product-leadership/crossing-the-canyon'

# query the website and return the html to the variable 'page'
page = requests.get(url)
print(page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

# find all links on page
links = soup.find_all('a')
print(links)

# create empty list to store links
urls = []

# loop through links and append to list
for link in links:
    urls.append(link.get('href'))

print(urls)

# create empty list to store page urls
page_urls = []

# loop through urls and append to list
for url in urls:
    if url is not None:
        if re.search('page', url):
            page_urls.append(url)

print(page_urls)

# create empty list to store page urls
page_urls_clean = []

