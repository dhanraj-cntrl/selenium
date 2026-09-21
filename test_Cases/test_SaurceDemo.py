from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.SauceDemoPageObject import SauceDemo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_101_Saurcedemo:

    ss_username="standard_user"
    ss_password="secret_sauce"
    ss_url = "https://www.saucedemo.com/"

    def test_ssLoginPage(self,setup):
        self.driver=setup
        self.driver.get(self.ss_url)
        self.ssob1=SauceDemo(self.driver)
        self.wait=WebDriverWait(self.driver,20)
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.ssob1.user_name)))
        self.ssob1.send_username(self.ss_username)
        self.ssob1.send_password(self.ss_password)
        self.ssob1.click_login()
        assert self.driver.title == "Swag Labs"

    def test_sauce_demo_addtokart(self,setup):
        self.driver=setup
        self.driver.get(self.ss_url)
        self.ssob1=SauceDemo(self.driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.ssob1.send_username())))
        self.ssob1.send_username(self.ss_username)
        self.ssob1.send_password(self.ss_password)
        self.ssob1.click_login()















