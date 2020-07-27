from settings import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD
from selenium import webdriver
import time

browser = webdriver.Chrome()

url = "http://www.instagram.com"
browser.get(url)
time.sleep(2)

username_el = browser.find_element_by_name("username")
password_el = browser.find_element_by_name("password")

username_el.send_keys(INSTAGRAM_USERNAME)
password_el.send_keys(INSTAGRAM_PASSWORD)
time.sleep(2)

submit_btn_el = browser.find_element_by_css_selector(
    "button[type='submit']"
)
submit_btn_el.click()