from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

CHROME_DRIVER_PATH = "/Users/alex_blain/selenium/chromedriver"
SIMILAR_ACCOUNT = "sciencesncl"
USERNAME = "blain1995"
PASSWORD = os.environ.get("INSTA_PASS")


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(url="https://www.instagram.com/")
        consent = self.driver.find_element_by_class_name("bIiDR")
        consent.click()

        time.sleep(3)

        user = self.driver.find_element_by_name("username")
        user.send_keys(USERNAME)

        insta_password = self.driver.find_element_by_name("password")
        insta_password.send_keys(PASSWORD)
        insta_password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(5)

        followers_link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_link.click()

        time.sleep(2)
        scr1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower()

bot.login()
bot.find_followers()
bot.follow()
