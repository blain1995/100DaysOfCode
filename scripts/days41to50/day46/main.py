from selenium import webdriver

chrome_driver_path = "/Users/alex_blain/selenium/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_r=a426ad6f-ea6d-43c8-b7f2-f2370cbf05b1&pd_rd_w=kmQhK&pd_rd_wg=6sbOH&pf_rd_r=B3T664XJ0XM3BGDZT2MM&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pd_rd_i=B01NBKTPTS&psc=1")

price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)
driver.close()
