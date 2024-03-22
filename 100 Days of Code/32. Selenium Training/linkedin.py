from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

email = ""
password = ""

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome()
browser.set_window_size(1080,800)
browser.get("https://www.linkedin.com/jobs/search/?currentJobId=3682817296&keywords=python%20developer&location=Jakarta&origin=JOB_SEARCH_PAGE_LOCATION_SUGGESTION&refresh=true")

signupbutton = browser.find_element(By.CLASS_NAME, value="nav__button-secondary")
signupbutton.click()
time.sleep(15)

emailinput = browser.find_element(By.ID, value="username")
emailinput.send_keys(email)

passwordinput = browser.find_element(By.ID, value="password")
passwordinput.send_keys(password)

submitbutton = browser.find_element(By.CLASS_NAME, value="login__form_action_container")
submitbutton.click()
time.sleep(30)

