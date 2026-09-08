from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.Login import Login
import requests
class Test_001_Login:

    username= "Admin"
    password= "admin123"
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


    def test_loginPage(self,setup):
        self.driver=setup
        #self.driver.maximize_window()
        self.driver.get(self.url)
        self.ob1=Login(self.driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.ob1.user_name)))
        self.ob1.set_user_name(self.username)
        self.ob1.set_password(self.password)
        self.ob1.click_login()
        actual_title=self.driver.title
        if actual_title == "OrangeHRM":
            assert True
        else:
            assert False


    # def test_api(self,requests):
    #     response=requests.post("https://api.example.com/users")
    #     assert response.status_code == 201
    #     data = response.json()
    #     assert data["id"] ==101


