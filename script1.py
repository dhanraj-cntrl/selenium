from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import IGNORED_EXCEPTIONS

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
driver.maximize_window()

# driver.implicitly_wait(10)
element=driver.find_element(By.XPATH,"//*[contains(text(),'START') and @class='start']")


wait=WebDriverWait(driver,20)
ele=wait.until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'START') and @class='start']")))
ele.click()

wait = WebDriverWait(driver,
              20,
              poll_frequency=2,
              ignored_exceptions=[NoSuchElementException])

#diff error and exception
#type error
#attribute error
#ZeroDivisionerror
#ValueError
#IndexError
#NameError
#IndentationError
#FileNotFoundError


#Exception
#NoSuchElementException
#StaleElementException
#TimeoutException
#NoSuchWindowException
#NoSuchFrameException
#InvalidSelectorException
#InvalidAlertException


try:
    print(10/0)
except ZeroDivisionError:
    print("Division by zero")
else:
    print("Division")
finally:
    print("finally")

































