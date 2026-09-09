from selenium import webdriver
from selenium.webdriver.common.by import By



class SauceDemo:

    sauce_uname = "//*[@placeholder='Username']"
    sauce_pass="//*[@placeholder='Password']"
    sauce_click_button="//*[@class='submit-button btn_action']"
    saurce_item = "//*[contains(text(),'Sauce Labs Backpack')]"
    sauce_item_add_to_cart="(//button[contains(text(),'Add to cart')])[1]"
    sauce_check_item="//*[@class='shopping_cart_badge']"

    def __init__(self,driver):
        self.driver=driver

    def sauce_set_username(self,ss_username):
        self.driver.find_element(By.XPATH,self.sauce_uname).send_keys(ss_username)

    def sauce_set_password(self,ss_password):
        self.driver.find_element(By.XPATH,self.sauce_pass).send_keys(ss_password)

    def sauce_login(self):
        self.driver.find_element(By.XPATH,self.sauce_click_button).click()

    def set_sauceitem(self):
        self.driver.find_element(By.XPATH,self.saurce_item).click()

    def set_saiceitemaddtokart(self):
        self.driver.find_element(By.XPATH,self.sauce_item_add_to_cart).click()

    def check_kart(self):
        self.driver.find_element(By.XPATH,self.sauce_check_item).click()







