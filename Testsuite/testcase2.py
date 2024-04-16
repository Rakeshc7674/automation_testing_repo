import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
# Enter all the fields in regester an account
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep
driver.find_element(By.XPATH,"//a[@href='/register?returnUrl=%2F']").click()
radiobutton=driver.find_element(By.ID,"gender-male")
radiobutton.click()
print(radiobutton.is_selected())
firstname=driver.find_element(By.ID,"FirstName").send_keys("rakesh")
driver.find_element(By.ID,"LastName").send_keys("ram")
dropdown=Select(driver.find_element(By.NAME,"DateOfBirthDay"))
dropdown.select_by_visible_text('1')
dropdown=Select(driver.find_element(By.NAME,"DateOfBirthMonth"))
dropdown.select_by_visible_text('August')
dropdown=Select(driver.find_element(By.NAME,"DateOfBirthYear"))
dropdown.select_by_visible_text('1998')
driver.find_element(By.NAME,"Email").send_keys("rakesh1235@gmail.com")
driver.find_element(By.NAME,"Password").send_keys("ramesh123@")
driver.find_element(By.NAME,"ConfirmPassword").send_keys("ramesh123@")
driver.find_element(By.ID,"register-button").click()
title=driver.title
print(title)
driver.save_screenshot('testcase2.png')
time.sleep(5)
driver.close()
