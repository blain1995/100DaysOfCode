import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

CHROMEDRIVER = "/Users/alex_blain/selenium/chromedriver"
spreadsheet_link = "https://docs.google.com/forms/d/e/1FAIpQLSeahGp9bv0m0Z75St8dS6vtO27N_ah7irQL-5rhpdnXin3xMw/viewform?usp=sf_link"

zoopla = "https://www.zoopla.co.uk/to-rent/property/newcastle-upon-tyne/?beds_min=1&price_frequency=per_month&price_max=900&q=Newcastle%20upon%20Tyne%2C%20Tyne%20%26%20Wear&results_sort=newest_listings&search_source=to-rent"

response = requests.get(url=zoopla)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

prices = soup.select(".css-1e28vvi-PriceContainer")
price_list = [price.text for price in prices]
print(price_list)

addresses = soup.select(".e2uk8e4")
address_list = [address.text.split("rent")[1] for address in addresses]
print(address_list)

links = soup.select(".e2uk8e4 href")
links_list = [f"https://www.zoopla.co.uk{address['href']}" for address in addresses]

driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
driver.get(url=spreadsheet_link)

for index in range(len(address_list)):
    time.sleep(2)
    address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address_list[index])

    price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price_list[index])

    link_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(links_list[index])

    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit_button.click()
    time.sleep(2)

    another_submission = driver.find_element_by_link_text("Submit another response")
    another_submission.click()