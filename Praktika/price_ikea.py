import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.ikea.com/ru/ru/p/skanevik-skonevik-komod-s-3-yashchikami-glyancevyy-belyy-30492176/"

headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36"
}
page = requests.get(url=PRODUCT_URL, headers=headers)
# print(page.content)

soup = BeautifulSoup(page.content, "lxml")
title = soup.find("span", class_="pip-header-section__title--big notranslate").get_text()
print(title)
price = soup.find("span", class_="pip-price__integer").get_text()
price = int(price.replace(" ",""))
print(price, type(price))