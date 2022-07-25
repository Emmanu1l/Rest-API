from selenium import webdriver
from bs4 import BeautifulSoup

PRODUCT_URL = "https://aliexpress.ru/item/1005001793146113.html?spm=a2g2w.productlist.i0.2.55d759456pkAFe&sku_id=12000017592912041"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "Connection": "keep-alive",
}
driver = webdriver.Chrome(executable_path="/usr/bin/firefox")
driver.get(PRODUCT_URL)
print(driver.page_source)