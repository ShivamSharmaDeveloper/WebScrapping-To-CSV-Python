from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

# The URL of the page we want to scrape
my_url = "https://www.flipkart.com/search?q=samsung+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT&suggestionId=samsung+mobiles%7CMobiles&requestId=cbda61e5-bbbf-4c49-9d32-bb451a9aa363&as-searchtext=samsu"

# Open a connection to the webpage
uClient = uReq(my_url)

# Read the HTML content of the page
page_html = uClient.read()

# Close the connection
uClient.close()

# Parse the HTML content using BeautifulSoup
page_soup = soup(page_html, "html.parser")

# Find all the containers that hold the information about each product
containers = page_soup.findAll("div", {"class": "_13oc-S"})

# Create a CSV file to store the scraped data
filename = "products.csv"
with open(filename, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Product_Name", "Pricing", "Ratings"])

    # Loop through each container and extract the product information
    for container in containers:
        product_name = container.div.img["alt"]

        price_container = container.findAll(
            "div", {"class": "_30jeq3 _1_WHN1"})
        price = price_container[0].text.strip()

        rating_container = container.findAll("div", {"class": "gUuXy-"})
        rating = rating_container[0].text
        print(rating)

        # Write the extracted information to the CSV file
        writer.writerow([product_name, price, rating])

# Print a message to indicate that the scraping is complete
print("Scraping is complete!")
