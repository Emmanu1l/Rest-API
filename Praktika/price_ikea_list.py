import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.ikea.com/ru/ru/search/products/?q=комод"

headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36"
}
page = requests.get(url=PRODUCT_URL, headers=headers)
# print(page.content)

soup = BeautifulSoup(page.content, "lxml")
title = soup.find_all(
	"span", 
	class_="header-section__title notranslate"
)
for i,
print(title)
price = soup.find("span", class_="pip-price__integer").get_text()
price = int(price.replace(" ",""))
print(price, type(price))