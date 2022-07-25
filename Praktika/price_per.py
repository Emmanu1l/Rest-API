from re import sub
from decimal import Decimal
import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.perekrestok.ru/cat/434/p/sok-biotta-bio-morkovnyj-pramogo-otzima-500ml-22410"

headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36"
}
page = requests.get(url=PRODUCT_URL, headers=headers)

soup = BeautifulSoup(page.content, "lxml")
titile = soup.find(
	"h1",
	class_="sc-fubCfw cqjzZF product__title"
).get_text()

print(title)

price = soup.find("div", class_="price-new").get_text()
price = price.replace(",", ".")
price_int = Decimal(sub(r"[^\d\-.]", "", price))
print(price, type(price), price_int, type(price_int))

from datetime import datetime
from sqlalchemy.org import Session
from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Price(Base):
	__tablename__ = "price"

	id = Column(Integer, primary_key=True)
	datetime = Column(DateTime)
	name = Column(String)
	price = Column(String(64))
	price_int = Column(Numeric(10, 2))
	
	def __repr__(self):
		return f"{self.name} | {self.price}"
engine = create_engine("sqlite:///database.sqlite")
Base.metadata.create_all(engine)

session = Session(bind=engine)

is_exits = session.query(Price).filter(Price.name==product_title).first()
if not is_exust:
	session.add(
		Price(
			name=product_title,
			datetime=datetime.now(),
			price=product_price,
			price_int=product_price_int)
		)
		session.commit()
	items = session.query(Price).all()
