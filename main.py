import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

ACC_LANG="en-IN,en-US;q=0.9,en;q=0.8,hi;q=0.7"
USER_AGENT="YOUR AGENT"
URL="PRODUCT URL"

params={
    "User-Agent":USER_AGENT,
    "Accept-Language":ACC_LANG,
}

response=requests.get(url=URL, headers=params)
soup=BeautifulSoup(response.text, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
