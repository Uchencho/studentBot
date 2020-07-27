from selenium import webdriver
import time

browser = webdriver.Chrome()

url = "https://google.com"
browser.get(url)
time.sleep(2)
# Check for the name of the target element
"""
<input name="q" type="text">
"""

# Find the element named q and input in the text field Selenium Python
search_el = browser.find_element_by_name("q")
search_el.send_keys("Selenium Python")
time.sleep(1)

"""
<input type="submit">
<input name="btnK" type="submit">
"""

submit_btn_el = browser.find_element_by_css_selector(
    "input[type='submit']"
)
submit_btn_el.click()