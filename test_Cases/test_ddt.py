from selenium import webdriver
import openpyxl
import readXl
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
path ="C:\\Users\\DHANRAJ\\OneDrive\\Documents\\sample.xlsx"
rows=readXl.getRowcount(path,'Sheet1')
cols=readXl.getColumncount(path,'Sheet1')

for r in range(2,rows+1):
    user_name=readXl.readData(path,'Sheet1',r,1)
    pass_Word=readXl.readData(path,'Sheet1',r,2)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//*[@placeholder='Username']").send_keys(user_name)
    driver.find_element(By.XPATH,"//*[@placeholder='Password']").send_keys(pass_Word)
    driver.find_element(By.XPATH,"//*[@type='submit']").click()
driver.quit()



