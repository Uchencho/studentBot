from selenium import webdriver
import time
from settings import PEAK_PASSWORD

def peak_reg(browser):
    '''
    Register as a student
    '''
    # Go to the webpage
    url = "https://sagittiform-forehea.000webhostapp.com/"
    browser.get(url)
    time.sleep(2)

    # Click the register button
    reg_btn_xpath = "//a[contains(text(), 'Register')]"
    reg_btn = browser.find_element_by_xpath(reg_btn_xpath)
    reg_btn.click()
    time.sleep(1)

    # Fill in the fields
    browser.find_element_by_name("email").send_keys("alozy@gmail.com")
    browser.find_element_by_name("signup-matricno").send_keys("EEG/2011/999")
    browser.find_element_by_name("signup-password").send_keys(PEAK_PASSWORD)
    browser.find_element_by_name("password2").send_keys(PEAK_PASSWORD)
    time.sleep(1.5)

    # Click the sign up button
    signUpBtn = browser.find_element_by_id('signbtn')
    signUpBtn.click()
    time.sleep(10)
    print("Finshed registeration\n\n")


def login(browser):
    '''
    Login student
    '''
    url = "https://sagittiform-forehea.000webhostapp.com/"
    browser.get(url)
    time.sleep(2)

    # Fill in matric number and password
    browser.find_element_by_id('matricno').send_keys("EEG/2011/999")
    browser.find_element_by_id('password').send_keys(PEAK_PASSWORD)
    time.sleep(2)

    # Click sign in button
    browser.find_element_by_class_name("typetwo").click()
    time.sleep(7)

    return str(browser.current_url), browser


def updateProfile(browser):
    '''
    Update Profile
    '''

    # Fill in matric number and password
    browser.find_element_by_id('firstname').send_keys("Ronaldo")
    browser.find_element_by_id('lastname').send_keys("Christiano")
    browser.find_element_by_id('department').send_keys("MicroBiology")
    browser.find_element_by_id('faculty').send_keys("Sciences")
    time.sleep(3)

    # Click sign in button
    browser.find_element_by_id("profilebtn").click()
    time.sleep(5)


if __name__ == "__main__":

    profile_update_url = "https://sagittiform-forehea.000webhostapp.com/profile.html"

    browser = webdriver.Chrome()
    next_url, current_browser = login(browser)
    if next_url == profile_update_url:
        updateProfile(current_browser)