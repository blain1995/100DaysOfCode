from selenium import webdriver

chrome_driver_path = "/Users/alex_blain/selenium/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# event = driver.find_element_by_class_name("medium-widget event-widget")
event_date = driver.find_elements_by_css_selector(".event-widget time")
event_name = driver.find_elements_by_css_selector(".event-widget li a")

events = {}
for n in range(len(event_date)):
    events[n]= {
        "time": event_date[n].text,
        "name": event_name[n].text
    }

print(events)
driver.quit()