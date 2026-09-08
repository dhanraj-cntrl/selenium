from selenium import webdriver
from selenium.webdriver.common.by import By

class NOP:

    user_name= "//*[@name='username']"
    pass_word= "//*[@name='password']"
    Login_button="//button[@id='submit']"
    Blg_dropdown="//select[@class='form-control' and @id='country']"



    def __init__(self,driver):
        self.driver=driver

    def set_usernmae(self,username):
        self.driver.find_element(By.XPATH,self.user_name).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.pass_word).send_keys(password)

    def Click_login(self):
        self.driver.find_element(By.XPATH,self.Login_button).click()





