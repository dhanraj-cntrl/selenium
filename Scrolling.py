from idlelib import window

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#mouse_Action

wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'Copy Text')]")))

element=driver.find_element(By.XPATH,"//button[contains(text(),'Copy Text')]")

mouse_Actions=ActionChains(driver)
mouse_Actions.double_click(element).perform()
src=driver.find_element(By.XPATH,"//*[contains(text(),'Drag me to my target')]")
trg=driver.find_element(By.XPATH,"//*[contains(text(),'Drop here')]")

mouse_Actions.drag_and_drop(src,trg).perform()
# mouse_Actions.context_click()

#switch between window:
driver.find_element(By.XPATH,"//*[contains(text(),'New Tab')]").click()
print(driver.window_handles)
print(driver.current_url)

parent=driver.current_window_handle  #8B90D16A43AE07A87097FDAA7A0FD841

for i in driver.window_handles:
    driver.switch_to.window(i)
    if driver.title == "SDET-QA Blog":
        print(driver.current_url)


driver.switch_to.window(parent)
#table

rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
cols=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")

all_rows=len(rows)  #7
all_cols=len(cols)  #4

for r in range(2,all_rows+1):
    for c in range(1,all_cols+1):
        values=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td["+str(c)+"]")
        print(values.text)

#links:

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

for i in links:
    print(i.get_attribute("href"))

#scrolling by pixel
driver.execute_script("window.scrollBy(0,1000)","")

#scrolling till element
element=driver.find_element(By.XPATH,"//*[contains(text(),'Errorcode 503')]")

#driver.execute_script("arguments[0].scrollIntoView();","element")

#dropdown
from selenium.webdriver.support.select import Select

ele=driver.find_element(By.XPATH,"//select[@id='country']")
drop_down=Select(ele)

all_dropdown=drop_down.options
for i in all_dropdown:
    print(i.text)



driver.close()

import pytest

@pytest.fixture   #be default scope of fixture is function [function/class/module/session/package]
def setup():
    driver=webdriver.Chrome()   #setup
    driver.maximize_window()
    yield driver
    driver.close()               #teardown





