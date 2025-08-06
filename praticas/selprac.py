from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.google.com/")
webElement = driver.find_element(By.NAME,"q")
webElement.send_keys("Selenium Webdriver" + Keys.ENTER)

time.sleep(30)
