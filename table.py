import pytest
from pygments.lexers import python
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
#
#
# driver=webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
#
# wait=WebDriverWait(driver,10)
# wait.until(EC.presence_of_element_located((By.XPATH,"//table[@name='BookTable']")))
#
# rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
# cols=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
#
# all_rows=len(rows)  #7
# all_cols=len(cols)  #4
#
# for r in range(2,all_rows+1):
#     for c in range(1,all_cols+1):
#         ele=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td["+str(c)+"]")
#         print(ele.text)
#     print()
#
#
#
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
print(driver.title)

wait=WebDriverWait(driver,10)
ele=wait.until(EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'New Tab')]")))
ele.click()

print(driver.window_handles)
parent=driver.current_window_handle

for i in driver.window_handles:
    if i!= parent:
        driver.switch_to.window(i)
        print(driver.current_url)

for i in driver.window_handles:
    driver.switch_to.window(i)
    if driver.title!="Automation Testing Practice: Data Entry Form":
        print(driver.current_url)

driver.switch_to.window(parent)
ele=driver.find_element(By.XPATH,"//select[@class='form-control' and @id='animals']")
drop_down=Select(ele)


for i in drop_down.options:
    print(i.text)

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

for i in links:
    print(i.get_attribute("href"))

from selenium.webdriver import ActionChains

mouse_actions=ActionChains(driver)
but=driver.find_element(By.XPATH,"//button[contains(text(),'Copy Text')]")

mouse_actions.double_click(but).perform()

wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'Drag me to my target')]")))

src=driver.find_element(By.XPATH,"//*[contains(text(),'Drag me to my target')]")
destin=driver.find_element(By.XPATH,"//*[@id='droppable']/p")

mouse_actions.drag_and_drop(src,destin).perform()


# for i in driver.window_handles:
#     driver.switch_to.window(i)
#     if driver.title!="Automation Testing Practice: Data Entry Form":
#         print(driver.current_url)

#ActionChains
#
# mouse_Action=ActionChains(driver)
# mouse_Action.double_click(ele).perform()
# mouse_Action.context_click(ele).perform()
# wait=WebDriverWait(driver,10)
# mouse_Action.move_to_element(ele).perform()
# mouse_Action.drag_and_drop(ele).perform()

#web table

rws=driver.find_elements(By.XPATH,"//*[@id='taskTable']//tr")
cls=driver.find_elements(By.XPATH,"//*[@id='taskTable']//th")

all_rws=len(rws)
all_cls=len(cls)

for r in range(2,all_rws+1):
    for c in range(1,all_cls+1):
        el=driver.find_element(By.XPATH,"//*[@id='taskTable']//tr["+str(r)+"]//td["+str(c)+"]")
        print(el.text)
    print()


#fixture:

import pytest

# @pytest.fixture:
# def setup():
#     driver=webdriver.Chrome()
#     yield driver
#     driver.close()



























driver.close()













