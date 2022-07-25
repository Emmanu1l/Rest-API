import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://aliexpress.ru/item/1005001793146113.html?spm=a2g2w.productlist.i0.2.55d759456pkAFe&sku_id=12000017592912041"

headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36"
}
page = requests.get(url=PRODUCT_URL, headers=headers)
# print(page.content)

soup = BeautifulSoup(page.content, "lxml")
title = soup.find("h1", class_="ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Heading__heading__1mk5o0 ali-kit_Heading__size-xxl__1mk5o0 Product_Name__productTitleText__hntp3").get_text()
print(title)
price = soup.find("span", class_="ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 price ali-kit_Price__size-xl__12ybyf Product_Price__current__1uqb8 product-price-current").get_text()
price = int(price.replace(" ",""))
print(price, type(price))