#Importing Required Libraries
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


#opening the browser
driver=webdriver.Firefox()
driver.get("https://jqueryui.com/selectable/")

#maximizing the window for better view
driver.maximize_window()

elem= driver.find_element(By.CLASS_NAME,"ui-selectable")


e=driver.find_element(By.XPATH,'//*[@id="selectable"]')



























''' elem1= driver.find_element(By.ID,'id="draggable"')
elem2 = driver.find_element(By.ID,'id="droppable"')
action= ActionChains(driver)
action.drag_and_drop(source=elem1, target=elem2).perform() '''