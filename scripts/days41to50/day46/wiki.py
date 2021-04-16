from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/alex_blain/selenium/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_number = driver.find_element_by_css_selector("#articlecount a")
# # print(article_number.text)
# # article_number.click()
#
# # all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search_bar = driver.find_element_by_name("search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_name("fName")
first_name.send_keys("Alex")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Blain")

email = driver.find_element_by_name("email")
email.send_keys("fakeemail@gmail.com")

button = driver.find_element_by_css_selector("form button")
button.click()
