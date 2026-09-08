from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

print(driver.current_window_handle)
parent=driver.current_window_handle


element=driver.find_element(By.XPATH,"//button[contains(text(),'New Tab')]")

wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'New Tab')]"))).click()

print(driver.window_handles)

for i in driver.window_handles:
    driver.switch_to.window(i)
    if driver.title=="Automation Testing Practice: Data Entry Form":
        print(driver.current_url)

        driver.implicitly_wait(10)
        ele=driver.find_element(By.XPATH,"//select[@class='form-control' and @id='colors']")

        drop_down=Select(ele)
        print(len(drop_down.options))
        for i in drop_down.options:
            print(i.text)

        rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")  #rows=7
        cols=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr//th")   #cols=4
        all_rows=len(rows)
        all_cols=len(cols)
        for r in range(2,all_rows+1):
            for c in range(1,all_cols+1):
                values=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td["+str(c)+"]")
                print(values.text)


driver.close()
