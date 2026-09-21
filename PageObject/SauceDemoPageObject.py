from selenium import webdriver
from selenium.webdriver.common.by import By


class SauceDemo:

    user_name = "//*[@id='user-name']"
    pass_word="//*[@id='password']"
    click_button="//*[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def send_username(self,ss_username):
        self.driver.find_element(By.XPATH,self.user_name).send_keys(ss_username)

    def send_password(self,ss_password):
        self.driver.find_element(By.XPATH,self.pass_word).send_keys(ss_password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.click_button).click()





