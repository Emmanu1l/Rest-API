import requests

cookies = {
    'city_path': 'ekaterinburg',
    'lang': 'ru',
    'PHPSESSID': '9c0c39d5c128e5c78f4696934cb13849',
    'current_path': '62265cbc0dcc1dad884e1569a03ed0bc10728add82d27f5edcd4b218e09749b5a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A150%3A%22%7B%22city%22%3A%2283878977-f329-11dd-9648-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu0415%5Cu043a%5Cu0430%5Cu0442%5Cu0435%5Cu0440%5Cu0438%5Cu043d%5Cu0431%5Cu0443%5Cu0440%5Cu0433%22%2C%22method%22%3A%22geoip%22%7D%22%3B%7D',
    '_csrf': '518ee2c3f11624b35072f674c52a7fc7fbddc4c20a9ad54157aac591728c3bd9a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22hhvIl-FEP6Bi_pXfidFoeE-JliGGXS0a%22%3B%7D',
    'dnsauth_csrf': 'ca20b01a6c553b0f08cc215b1e6b6fdf96a804b1c258e63b0cceb1f6efceeeafa%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22dnsauth_csrf%22%3Bi%3A1%3Bs%3A36%3A%22f1891fba-c1e0-4866-b5a6-14655cb42a2b%22%3B%7D',
    'phonesIdent': '2955a57799c4c365a6271d97e9cf5f996a2b294f644b54994e2dc34fd8f6feb3a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22cb928f39-f5d1-420f-88a6-57817b170740%22%3B%7D',
    'rerf': 'AAAAAGLG8yO666BgAzCQAg==',
    'ipp_uid': '1657205539683/pJ25iYjBjslvNIRc/ptAkCM47yOORLlJTbr5uAg==',
    'ipp_key': 'v1657205539683/v33947245ba5adc7a72e273/oLnHvRG/rSTYog8CE/7XZw==',
    'rrpvid': '552848491662941',
    '_gcl_au': '1.1.993037849.1657205614',
    'rcuid': '62c6f3280bbf080001d5d11e',
    '_ga_FLS4JETDHW': 'GS1.1.1657205614.1.1.1657205960.0',
    '_ga': 'GA1.1.1149732382.1657205615',
    'cartUserCookieIdent_v3': 'be772f66fe27e57e00ec5f656ee585d24f6b7411c4660c6a448b3784ab454714a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22a15a7953-8ef6-3647-8b13-7af11dd0522a%22%3B%7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.dns-shop.ru/product/48bcd58ff2873330/trimmer-benzinovyj-carver-promo-pbc-43/no-referrer',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-Token': 'qsbP5JMH2cGS6Zlg-mCm7jkfi0zioSWI-1aokqqaMwXCrrmt_yqfhMLf2wmlEP6IUHvNI4fkCMKXP-_V8skDZA==',
    'content-type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.dns-shop.ru',
    'DNT': '1',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'city_path=ekaterinburg; lang=ru; PHPSESSID=9c0c39d5c128e5c78f4696934cb13849; current_path=62265cbc0dcc1dad884e1569a03ed0bc10728add82d27f5edcd4b218e09749b5a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A150%3A%22%7B%22city%22%3A%2283878977-f329-11dd-9648-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu0415%5Cu043a%5Cu0430%5Cu0442%5Cu0435%5Cu0440%5Cu0438%5Cu043d%5Cu0431%5Cu0443%5Cu0440%5Cu0433%22%2C%22method%22%3A%22geoip%22%7D%22%3B%7D; _csrf=518ee2c3f11624b35072f674c52a7fc7fbddc4c20a9ad54157aac591728c3bd9a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22hhvIl-FEP6Bi_pXfidFoeE-JliGGXS0a%22%3B%7D; dnsauth_csrf=ca20b01a6c553b0f08cc215b1e6b6fdf96a804b1c258e63b0cceb1f6efceeeafa%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22dnsauth_csrf%22%3Bi%3A1%3Bs%3A36%3A%22f1891fba-c1e0-4866-b5a6-14655cb42a2b%22%3B%7D; phonesIdent=2955a57799c4c365a6271d97e9cf5f996a2b294f644b54994e2dc34fd8f6feb3a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22cb928f39-f5d1-420f-88a6-57817b170740%22%3B%7D; rerf=AAAAAGLG8yO666BgAzCQAg==; ipp_uid=1657205539683/pJ25iYjBjslvNIRc/ptAkCM47yOORLlJTbr5uAg==; ipp_key=v1657205539683/v33947245ba5adc7a72e273/oLnHvRG/rSTYog8CE/7XZw==; rrpvid=552848491662941; _gcl_au=1.1.993037849.1657205614; rcuid=62c6f3280bbf080001d5d11e; _ga_FLS4JETDHW=GS1.1.1657205614.1.1.1657205960.0; _ga=GA1.1.1149732382.1657205615; cartUserCookieIdent_v3=be772f66fe27e57e00ec5f656ee585d24f6b7411c4660c6a448b3784ab454714a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22a15a7953-8ef6-3647-8b13-7af11dd0522a%22%3B%7D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

params = {
    'cityId': '24',
    'langId': 'ru',
    'v': '2',
}

data = 'data={"type":"product-buy","containers":[{"id":"as-uA1nGk","data":{"id":"48bcd58f-f287-11e6-a9e7-00155d03330d","params":{"showOneClick":true,"isCard":true}}}]}'

response = requests.post('https://www.dns-shop.ru/ajax-state/product-buy/', params=params, cookies=cookies, headers=headers, data=data)
#  print(response.json())
data = response.json()
title = data["data"]["states"][0]["data"]["name"]
price = data["data"]["states"][0]["data"]["price"]["current"]
print(title, price)
