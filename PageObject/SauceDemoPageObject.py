from selenium import webdriver
from selenium.webdriver.common.by import By



class SauceDemo:

    sauce_uname = "//*[@placeholder='Username']"
    sauce_pass="//*[@placeholder='Password']"
    sauce_click_button="//*[@class='submit-button btn_action']"


    def __init__(self,driver):
        self.driver=driver

    def sauce_set_username(self,ss_username):
        self.driver.find_element(By.XPATH,self.sauce_uname).send_keys(ss_username)

    def sauce_set_password(self,ss_password):
        self.driver.find_element(By.XPATH,self.sauce_pass).send_keys(ss_password)

    def sauce_login(self):
        self.driver.find_element(By.XPATH,self.sauce_click_button).click()



