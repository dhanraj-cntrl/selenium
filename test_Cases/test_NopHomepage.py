import pytest
from pygments.lexers import python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.HomePageNop import NOP
from selenium.webdriver.support.ui import Select

class Test_001_HomepageNOP:

    username="student"
    password="Password123"
    test_url = "https://practicetestautomation.com/practice-test-login/"
    blog_spotURl= "https://testautomationpractice.blogspot.com/2018/09/automation-form.html"

    #@pytest.mark.skip
    def test_LoginNOP(self,setup):
        self.driver=setup
        setup.get(self.test_url)
        self.ob2=NOP(self.driver)
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.presence_of_element_located((By.XPATH,self.ob2.user_name)))
        self.ob2.set_usernmae(self.username)
        self.ob2.set_password(self.password)
        self.ob2.Click_login()
        actual_title=self.driver.title
        if actual_title == "Logged In Successfully | Practice Test Automation":
            assert True
        else:
            assert False



    def test_blogSpot(self,setup):
        self.driver=setup
        self.driver.get(self.blog_spotURl)
        self.ob3=NOP(self.driver)
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.presence_of_element_located((By.XPATH,self.ob3.Blg_dropdown)))
        self.element=self.driver.find_element(By.XPATH,self.ob3.Blg_dropdown)
        self.all_dropdown=Select(self.element)
        for i in self.all_dropdown.options:
            print(i.text)





