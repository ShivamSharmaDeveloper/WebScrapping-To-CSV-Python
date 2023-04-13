from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.flipkart.com/search?q=samsung+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT&suggestionId=samsung+mobiles%7CMobiles&requestId=cbda61e5-bbbf-4c49-9d32-bb451a9aa363&as-searchtext=samsu"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

# Now let’s see how many HTML containers are present in this link:
containers = page_soup.findAll("div", {"class": "_13oc-S"})
print(len(containers))

# Let's check how much products we have
print(soup.prettify(containers[0]))

# Now let’s see the first item present in the page:
container = containers[0]
print(container.div.img["alt"])

# Now let’s have a look at the price of this smartphone:
price = container.findAll("div", {"class": "_30jeq3 _1_WHN1"})
print(price[0].text)

# Now let’s have a look at its ratings from its customers:
ratings = container.findAll("div", {"class": "gUuXy-"})
print(ratings[0].text)

# Now let’s create a CSV file and store all the mobile phones with their name, price and ratings:
filename = "products.csv"
f = open(filename, "w")
headers = "Product_Name, Pricing, Ratings \n"
f.write(headers)

# Now let’s have a look at what our CSV file has stored after the web scraping of Flipkart:
for container in containers:
    product_name = container.div.img["alt"]
    price_container = container.findAll(
        "div", {"class": "_30jeq3 _1_WHN1"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "gUuXy-"})
    rating = rating_container[0].text
    print("Product_Name:" + product_name)
    print("Price: " + price)
    print("Ratings:" + rating)
