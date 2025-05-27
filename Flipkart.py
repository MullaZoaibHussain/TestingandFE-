#Importing Required Libraries
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#opening the browser
driver=webdriver.Firefox()
driver.get("https://www.flipkart.com/")

#maximizing the window for better view
driver.maximize_window()

#Giving a variable to find and click the search Bar
elem= driver.find_element(By.CLASS_NAME,'Pke_EE')
elem.click()


#send keys are used to send the data to variable of search
elem.send_keys("keyboard")
elem.send_keys (Keys.RETURN)
time.sleep(3)

#scrolling randomly 
driver.execute_script("window.scrollBy(0, 3456)")

#selection a random product
keyboard=driver.find_elements(By.XPATH, "/html/body/div/div/div[3]/div[1]/div[2]/div[9]/div/div[2]/div/a[2]")

if keyboard:
 K=random.choice(keyboard)
 K.click()
else:
  print("NO Responce")

#Adding the selected product to cart
cart=driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button")
cart.click() 

#Payment
Placetoorder=driver.find_element(By.CLASS_NAME,"/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/form/button")
Placetoorder.click()