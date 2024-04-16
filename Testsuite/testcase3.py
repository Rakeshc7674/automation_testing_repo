import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# don't enter anything in mandatory fields in regester an account
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()
time.sleep
driver.find_element(By.XPATH,"//a[@href='/register?returnUrl=%2F']").click()
firstname=driver.find_element(By.ID,"FirstName").send_keys("")
driver.find_element(By.ID,"LastName").send_keys("")
driver.find_element(By.NAME,"Email").send_keys("")
driver.find_element(By.NAME,"Password").send_keys("")
driver.find_element(By.NAME,"ConfirmPassword").send_keys("")
driver.find_element(By.ID,"register-button").click()
title=driver.title
print(title)
driver.save_screenshot('testcase3.png')
time.sleep(5)
driver.close()
