from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:

    user_name="//*[@placeholder='Username']"
    pass_word= "//*[@placeholder='Password']"
    login_button="//button[@type='submit']"
    #
    # __user_name="//*[@placeholder='Username']"
    # __pass_word= "//*[@placeholder='Password']"   #private Variable
    # __login_button="//button[@type='submit']"


    def __init__(self,driver):
        self.driver=driver

    def set_user_name(self,username):
        self.driver.find_element(By.XPATH,self.user_name).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.pass_word).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button).click()


