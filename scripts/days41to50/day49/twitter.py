from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/alex_blain/selenium/chromedriver"
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASS")


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        consent = self.driver.find_element_by_css_selector("#_evidon-banner-acceptbutton")
        consent.click()
        start_button = self.driver.find_element_by_css_selector(".start-button")
        start_button.click()
        time.sleep(60)
        download_speed = float(self.driver.find_element_by_class_name("download-speed").text)
        upload_speed = float(self.driver.find_element_by_class_name("upload-speed").text)
        speed_list = [download_speed, upload_speed]
        return speed_list

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/login")
        time.sleep(5)
        username = self.driver.find_element_by_name("session[username_or_email]")
        username.send_keys(TWITTER_EMAIL)

        password_input = self.driver.find_element_by_name("session[password]")
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_input.send_keys("FAKE TWITTER BOT TEST:\n'WHY IS MY INTERNET SO SLOW!'\nSent from my PyCharm session")

        time.sleep(2)
        tweet_send = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
        tweet_send.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
result = bot.get_internet_speed()
print(result)

if result[0] < PROMISED_DOWN or result[1] < PROMISED_UP:
    bot.tweet_at_provider()
