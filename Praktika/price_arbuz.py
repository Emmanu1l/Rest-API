from re import sub
from decimal import Decimal
import requests
from bs4 import BeautifulSoup

PRODUCT_URL_PEREKRESTOK = "https://www.perekrestok.ru/cat/367/p/arbuz-77410"

headers = {
    "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
}
page = requests.get(url=PRODUCT_URL_PEREKRESTOK, headers=headers)
#  print(page.content)

soup = BeautifulSoup(page.content, "lxml")
product_title = soup.find(
    "h1",
    class_="sc-fubCfw cqjzZF product__title"
).get_text()


product_price = soup.find("div", class_="price-new").get_text()
product_price = product_price.replace(",", ".")
product_price_int = Decimal(sub(r"[^\d\-.]", "", product_price))
#  print(price, type(price), price_int, type(price_int))


# --------------------------------------------
#             MAGNIT PRICE
#---------------------------------------------

PRODUCT_URL_MAGNIT = "https://magnit.ru/promo/3194641/?format[]=ms"

headers = {
    "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
}
page = requests.get(url=PRODUCT_URL_MAGNIT, headers=headers)
#  print(page.content)

soup = BeautifulSoup(page.content, "lxml")
magnit_title = soup.find(
    "div",
    class_="action__title"
).get_text()

magnit_price = soup.find("span", class_="label__price-integer").get_text()
#  price = int(price.replace(" ", ""))
magnit_price_int = sub(r"[^\d\-.]", "", magnit_price)

# --------------------------------------------
#               DATABASE
# --------------------------------------------

from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Price(Base):
    __tablename__ = "price"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    datetime = Column(DateTime)
    price = Column(String(64))
    price_int = Column(Numeric(10, 2))

    def __repr__(self):
        return f"{self.name} | {self.price}"

engine = create_engine("sqlite:///database.sqlite")
Base.metadata.create_all(engine)

session = Session(bind=engine)

def add_price(title, price, price_int, url):
    is_exist = session.query(Price).filter(
        Price.name==title
    ).order_by(Price.datetime.desc()).first()

    if not is_exist:
        session.add(
            Price(
                name=title,
		url=url,
                datetime=datetime.now(),
                price=price,
                price_int=price_int
            )
        )
        session.commit()
    else:
        if is_exist.price_int != price_int:
            session.add(
                Price(
                    name=title,
                    datetime=datetime.now(),
                    price=price,
                    price_int=price_int
                )
            )
            session.commit()


add_price(product_title, product_price, product_price_int, PRODUCT_URL_PEREKRESTOK)
add_price(magnit_title, magnit_price, magnit_price_int, PRODUCT_URL_MAGNIT)

items = session.query(Price).all()
for item in items:
    print(item)
