# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



# Open the file for reading
with open('urls.txt', 'r') as f:
    # Initialize an empty list to store the URLs
    urls = []

    # Read each line in the file
    for line in f:
        # Strip leading and trailing whitespace and append the URL to the list
        urls.append(line.strip())


text = []

# WebDriver Chrome
driver = webdriver.Firefox()

driver.get('https://program.reforge.com/c/product-series-eg/leading-a-product-strategy/from-product-management-to-product-leadership/crossing-the-canyon')
time.sleep(60)

file = open("All Product Strategy Text", "w" , encoding="utf-8")

for url in urls:
    # Target URL
    driver.get(str(url))
    # To load entire webpage
    

    # Printing the whole body text
    time.sleep(5)
    print(driver.find_element(By.XPATH, "/html/body").text)
    text.append(driver.find_element(By.XPATH, "/html/body").text)
    # Open a file in write mode
    # Split the URL on the "/" character, starting from the right side of the string
    #parts = url.rsplit("/", 1)

    # Write the text to the file
    file.write(driver.str(find_element(By.XPATH, "/html/body").text) + "\n")

    # Get the last item in the resulting list of parts
    #last_part = parts[-1]
    #file = open(str(last_part), "w")

    # Write the text to the file
    #file.write(driver.find_element(By.XPATH, "/html/body").text)

    # Close the file
    #file.close()

   





# Close the file
file.close()


print('closing now')
# Closing the driver
time.sleep(10)
driver.close()
