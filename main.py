from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os

URL = 'https://www.amazon.co.uk/dp/B08HB1TWCN/ref=gw_uk_desk_h1_aucc_lsr_th_kifmay_noprice?pf_rd_r=728QXAJRDDN2NA7PX' \
      '6TF&pf_rd_p=028314a7-2ae8-4838-b3b6-3b1560c63634'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.93 Safari/537.36',
    "Accept-Language": 'en-GB,en-US;q=0.9,en;q=0.8',
}

target_price = 65.00

EMAIL = os.environ['MY_EMAIL']
PASS = os.environ['MY_PASS']

print(EMAIL)
print(PASS)

response = requests.get(url=URL, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, 'lxml')
price = float(soup.find(name='span', id='priceblock_ourprice').string.split('£')[1])

title = soup.title.string

print(title)

if price <= target_price:
    message = f"{title} is now {price}."

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASS)
        connection.sendmail(
            from_addr= 'pythontest384@gmail.com',
            to_addrs= 'delo384@outlook.com',
            msg=f"Subject:Amazon Price Alert\n\n{message}\n{URL}"
        )