from bs4 import BeautifulSoup
from selenium import webdriver
import re

url = "https://www.skipthedishes.com/"

browser = webdriver.Chrome()
browser.get(url + "kingston/restaurants" +  "?search=pizza")
html = browser.page_source

soup = BeautifulSoup(html, "lxml")

searchResults = []
for resto in soup.find_all("a", class_="restaurant-list"):
    content = resto.findAll('div', class_="list-content")
    headings = content[0].find_all("div")
    ratings = content[1].find_all("div")

    searchResults.append({
        'name': headings[0].string,
        'address': headings[1].string,
        'rating': ratings[0].string,
        'href': resto["href"]
    })

searchResults.reverse()

browser.get(url + searchResults[0]["href"])
html = browser.page_source

soup = BeautifulSoup(html, "lxml")

pizzas = []
sizeFilter = "small"
for row in soup.find_all('div', class_="row menu-group"):
    categoryName = row.find('h3', class_="category-name").string.lower()

    if categoryName.find("pizza") == -1:
        continue

    if categoryName.find(sizeFilter) == -1:
        continue

    prices = []
    for priceRow in row.find_all('td', 'menu-item-price'):
        prices.append(re.findall("\d+\.\d+", priceRow.div.strong.string)[0])

    print(prices)
