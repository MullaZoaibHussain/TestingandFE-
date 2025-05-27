#Importing Required Libraries
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#opening the browser
driver=webdriver.Firefox()
driver.get("http://www.amazon.in")

#maximizing the window for better view
driver.maximize_window()

#Giving a variable to find and click the search Bar
elem= driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
elem.click()

#send keys are used to send the data to variable of search
elem.send_keys("keyboard")
elem.send_keys (Keys.RETURN)
time.sleep(3)
#scrolling randomly 
driver.execute_script("window.scrollBy(0, 3000)")
#selection a random product
keyboard=driver.find_elements(By.XPATH, "//button")

if keyboard:
 K=random.choice(keyboard)
 K.click()
else:
  print("NO Responce")
#Adding the selected product to cart
cart=driver.find_element(By.ID, "nav-cart-text-container")
cart.click() 
#Payment
Payment=driver.find_element(By.NAME,"proceedToRetailCheckout")
Payment.click()