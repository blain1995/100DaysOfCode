from bs4 import BeautifulSoup
import requests
import lxml
from smtplib import SMTP
import os

my_email = os.environ.get("MY_EMAIL")
my_pass = os.environ.get("EMAIL_PASS")
# --------------------- Make initial request ---------------------
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

item_url = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_r=a426ad6f-ea6d-43c8-b7f2-f2370cbf05b1&pd_rd_w=kmQhK&pd_rd_wg=6sbOH&pf_rd_r=B3T664XJ0XM3BGDZT2MM&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pd_rd_i=B01NBKTPTS&psc=1"
response = requests.get(url=item_url, headers=headers)
response.raise_for_status()
data = response.text

# -------------------------- Make Soup --------------------------
soup = BeautifulSoup(data, "lxml")
price = soup.find(name="span", id="priceblock_ourprice").text
price = float(price.split("$")[1])
print(price)

# ------------------- Check if price below set -------------------
target_price = 100

if price < target_price:
    with SMTP(host="smtp.gmail.com", port=587) as client:
        client.starttls()
        client.login(user=my_email, password=my_pass)
        client.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg=f"Subject: New amazon low price! \n\nYour item price has fallen below the target price.\nYou"
                            f"can find the url here: {item_url}")
