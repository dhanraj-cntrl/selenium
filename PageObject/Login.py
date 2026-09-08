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


#private variable -- __a can be accessible within class itself
#i have oop concept in my login class Where i kept all locator is inside class and related operation as well. That we
#called it as encapsulation. Where as self.obe.set_user_name where all business logic is kept inside class called as abstraction.
#constructor is being used which user driver which is passed from test cases.
#where in fixture we can see polymorphism - that is same method different behaviour through diff browser.

#
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Exception cant divide by zero")
# else:
#     print("in a else block")
# finally:
#     print("finally")

