# Import the `BeautifulSoup` and `requests` libraries
from bs4 import BeautifulSoup
import requests

# Define the URL of the website that you want to scrape
url = "https://program.reforge.com/programs/product-series-eg"

# Use the `requests` library to send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the response using the `BeautifulSoup` library
soup = BeautifulSoup(response.text, "html.parser")

# Find all of the `a` elements on the page that have an `href` attribute
links = soup.find_all("a", href=True)

# Iterate over the links
for link in links:
  # Get the `href` attribute of the link
  page_url = link["href"]

  # If the URL is a relative URL, convert it to an absolute URL
  if page_url.startswith("/"):
    page_url = url + page_url

  # Send a GET request to the page URL
  page_response = requests.get(page_url)

  # Parse the HTML content of the page using the `BeautifulSoup` library
  page_soup = BeautifulSoup(page_response)


    # Extract the text from the page using the `get_text()` method
page_text = page_soup.get_text()


# Define the path and filename for the file
# file_path = "data/page_{}.txt".format(page_number)

# Open the file for writing using the `w` mode
# with open(file_path, "w") as file:

