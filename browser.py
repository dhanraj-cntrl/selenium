import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture
# def setup():
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()


# @pytest.fixture(params=["Chrome","Edge","Firefox"])
# def setup(request):
#     browser=request.param
#     if browser=="Chrome":
#         driver=webdriver.Chrome()
#     elif browser=="Edge":
#         driver=webdriver.Edge()
#     elif browser=="Firefox":
#         driver=webdriver.Firefox()
#     yield driver
#     driver.quit()

@pytest.fixture(params=["Chrome","Edge","Firefox"])
def setup(request):
    browser=request.param
    if browser=="Chrome":
        options=webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver=webdriver.Chrome(options=options)
        # driver=webdriver.Chrome()
    elif browser=="Edge":
        options=webdriver.EdgeOptions()
        options.add_argument("--headless")
        driver=webdriver.Edge(options=options)
        #driver=webdriver.Edge()
    elif browser=="Firefox":
        options=webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver=webdriver.Firefox(options=options)
        #driver=webdriver.Firefox()
    yield driver
    driver.quit()


file=open('C:\\Users\\DHANRAJ\\filehandling.txt','w')
file.write("This is my first line")
file.write("\nThis is my second line")
file.write("\nThis is my third line")

file.close()

# file=open("C:\\Users\\DHANRAJ\\filehandling.txt","r")
# # print(f.read())
# # print(f.read(10))
# print(file.readlines())


file.close()

file=open("C:\\Users\\DHANRAJ\\filehandling.txt","a")
file.write("\nThis is my fourth line")
file=open("C:\\Users\\DHANRAJ\\filehandling.txt","r")
print(file.read())

file.close()

#polymorphism
#method overiding
#method overloading

def is_name(name=None):
    if name is not None:
        print("Hello")
    else:
        print("HelloHello")
is_name("Dhanraj")

class RBI:
    def roi(self):
        print("9%")

class ICICI(RBI):
    def roi(self):
        print("10%")

ob1=ICICI()
ob1.roi()

import pytest

@pytest.fixture(params=["Chrome","Edge"])
def setup(request):
    browser=request.param
    if browser=="Chrome":
        driver=webdriver.Chrome()
    elif browser=="Edge":
        driver=webdriver.Edge()
    yield driver
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:

    username="//*[@name='username']"
    pass_word="//*[@name='password']"
    login_button="//button[type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.XPATH,self.username).send_keys(username)





tup1 = ("python",True,10.5,12,[12,23,34])
#print(tup1.index(24))  #ValueError
print(tup1[2])


tup1 = (10)
print(type(tup1)) #<class 'int'>

#dictionary -mutable/key-value pair
#indexing by "key" is possible
#duplicate in key is not allowed

dict1 = {"name":"Dhanraj","age":23,"salary":230000,"name":"Dan"}
print(dict1)

#when same key appear duplicate dict replace first with latest
print(dict1["name"])
dict1["name"] = "Python"
print(dict1)
dict1["age"] = 32
print(dict1)
dict1["ages"] = 2300
print(dict1)


dict1.pop("age")
print(dict1)
dict1["year"] = 2000
print(dict1)
#dict1.pop("age")
print(dict1)

dict1.popitem()   #it remove last ele from dicti
print(dict1)

print(dict1.items())
print(dict1.keys())
print(dict1.values())
print(dict1.get("ages"))



# What is a dictionary in Python?
#mutable/ordered/indexing key
# How do you create a dictionary?
dict1={"name" : "Dhanraj"}
# What is the difference between a dictionary and a list?
#mutable/mutable
#duplicacy in key is not allowed/dupl allowed
#{}/[]
#order/order
#indexing/slicing is possible

# Can dictionary keys be duplicated?
#no
# What happens if duplicate keys are used?
dict1={"name" : "Dhanraj","age":23,"salary":23000,"name":"Dan","ages":23}
print(dict1)

# Can dictionary values be duplicated?
#yes

# Can a dictionary contain different data types?
#yes
# Can a dictionary be empty?
dict1={}
print(type(dict1))

# How do you access a dictionary value?
dict1={"name" : "Dhanraj","age":23,"salary":23000,"name":"Dan","ages":23}

print(dict1.items())
print(dict1.values())
print(dict1.get("ages"))
# How do you add a new key-value pair?
dict1["incent"] = 10000
print(dict1)

# How do you update an existing value?
dict1["ages"] = 23000
print(dict1)

# How do you delete a key-value pair?

# How do you check whether a key exists?
# How do you find the number of items in a dictionary?
# How do you iterate through a dictionary?
#popitem() -it rmeove last ele
#pop("key") -remove el on key

# Write a program to print all keys.
# Write a program to print all values.
print(dict1.values())
# Write a program to print both keys and values.
print(dict1.items())
# Write a program to find the length of a dictionary.
print(len(dict1))
# Write a program to count the frequency of characters in a string.

st= "welcome to india"

def is_freq():
    freq={}
    for i in st:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
ob1=is_freq()
print(ob1)


































