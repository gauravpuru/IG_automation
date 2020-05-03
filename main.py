# Here we'll be importing some dependencies

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:\\Selenium_driver\\chromedriver.exe")          # Replace The file path of your selenium webdriver
browser.get("https://www.instagram.com/")
browser.maximize_window()
time.sleep(2)
email = browser.find_element_by_xpath("//input[@aria-label='Phone number, username, or email']")
email.send_keys("YOUR USERNAME HERE")                                         # Your UserName here, you can import from file or paste here
time.sleep(2)
passw = browser.find_element_by_xpath("//input[@aria-label='Password']")
passw.send_keys("YOUR PASSWOORD HERE"+Keys.ENTER)                             # Your Password here, you can paste or can import from file
time.sleep(7)
butt = browser.find_element_by_xpath("//button[contains(text(),'Not Now')]")
butt.click()
time.sleep(3)
html = browser.find_element_by_tag_name('html')
for i in range(50):
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
browser.quit()
