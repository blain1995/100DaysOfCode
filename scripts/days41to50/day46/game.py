from selenium import webdriver
import time

chrome_driver_path = "/Users/alex_blain/selenium/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")

store_items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in store_items]

timeout = time.time() + 60*5
upgrade = time.time() + 5
while True:
    cookie.click()
    if time.time() > upgrade:
        all_prices = driver.find_elements_by_css_selector("#store b")
        items = []

        money = driver.find_element_by_id("money").text
        if "," in money:
            money.replace(",", "")
        money = int(money)

        for price in all_prices:
            price_text = price.text
            if price_text != "":
                cost = int(price_text.split("-")[1].strip().replace(",", ""))
                items.append(cost)

        upgrades_dict = {}
        for number in range(len(items)):
            upgrades_dict[items[number]] = item_ids[number]

        affordable_upgrades = {}
        for item_cost, id in upgrades_dict.items():
            if money > item_cost:
                affordable_upgrades[cost] = id

        highest = max(affordable_upgrades)
        print(highest)
        to_purchase = affordable_upgrades[highest]

        driver.find_element_by_id(to_purchase).click()

        upgrade = time.time() + 5
    if time.time() > timeout:
        cookies_per_second = driver.find_element_by_id("cps").text
        print(cookies_per_second)
        break
