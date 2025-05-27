#Importing Required Libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#opening the browser
driver= webdriver.Firefox()
driver.get("http://www.amazon.in")
#maximizing the window for better view
driver.maximize_window()
time.sleep(3)
#Giving a variable to find and click the search Bar
elem =driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']")
elem.click()
#send keys are used to send the data to variable of search
elem.send_keys("keyboard") 
elem.send_keys (Keys.RETURN)
time.sleep(1)
#Selecting the first product
e=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div/a[2]')
e.click()
#Adding the product to cart
cart=driver.find_element(By.ID, 'add-to-cart-button')
cart.click()


