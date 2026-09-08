from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.makemytrip.com/flights/?cmp=SEM|M|DF|B|Brand|B_M_Makemytrip_Search_Exact|Brand_Top_5_Exact|Expanded|&ef_id=:G:s&msclkid=22579ea37c95177e95e9f4371ffb32b7")

driver.implicitly_wait(10)

element=driver.find_element(By.XPATH,"//li[@data-cy='menu_Holidays']//a")

wait=WebDriverWait(driver,10)
stor=wait.until(EC.presence_of_element_located(element))

stor.click()

#fluent wait

wait1=WebDriverWait(driver,
              10,
              poll_frequency=2,
              ignored_exceptions=[NoSuchElementException])
driver.close()








