from selenium import webdriver
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.ikea.com/ru/ru/p/skanevik-skonevik-komod-s-3-yashchikami-glyancevyy-belyy-30492176/"

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36",
	"Accept": "*/*",
	"Accept-language": "ru,en;q=0.9",
	"Upgrade-Insecure-Requests": "1",
	"Connection": "keep-alive",
}
driver = webdriver.Firefox(executable_path="./geckodriver")
driver.ger(PRODUCT_URL)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")
title = soup.find("span", class_="pip-header-section__title--big notranslate")
print(title.get_text())

driver.close()
driver.quit()